#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Check staged bytes and Git exclusions before a local source-only commit."""
from pathlib import Path
import re
import subprocess

ROOT = Path(__file__).resolve().parents[1]
BLOCKED_ROOTS = {'work', 'artifacts', 'sources', 'references', 'inventory', 'logs', '.state', 'status'}
BLOCKED_PARTS = {'private', 'local', 'out', 'backups', 'dumps', '__pycache__', '.git'}
BLOCKED_SUFFIXES = {'.img', '.bin', '.ko', '.elf', '.exe', '.dll', '.so', '.o', '.a',
                    '.key', '.pem', '.pub', '.gz', '.xz', '.zip', '.kdz', '.dz', '.dtb', '.dtbo'}


def staged_files():
    raw = subprocess.check_output(['git', 'ls-files', '--stage', '-z'], cwd=ROOT)
    for item in raw.split(b'\0'):
        if not item:
            continue
        metadata, name = item.split(b'\t', 1)
        mode, oid, stage = metadata.decode().split()
        if stage != '0' or mode not in ('100644', '100755'):
            raise ValueError('Symlink, submodule or conflicted index requires explicit review')
        yield name.decode('utf-8'), oid


def main():
    checked = 0
    for name, oid in staged_files():
        path = Path(name)
        if (path.parts[0] in BLOCKED_ROOTS or set(path.parts) & BLOCKED_PARTS or
                path.suffix.lower() in BLOCKED_SUFFIXES or
                path.name in {'authorized_keys', 'known_hosts', '.env', 'hwparam.json'}):
            raise ValueError(f'Forbidden index path: {name}')
        data = subprocess.check_output(['git', 'cat-file', 'blob', oid], cwd=ROOT)
        if len(data) > 1024 * 1024 or b'\0' in data:
            raise ValueError(f'Large or binary index entry: {name}')
        if re.search(rb'^-----BEGIN (?:RSA |EC |OPENSSH |DSA )?PRIVATE KEY-----\r?$', data, re.M):
            raise ValueError(f'Private key in index: {name}')
        # Do not print credential content if a mistakenly staged config is found.
        if re.search(rb'^\s*(?:psk|password|passwd)\s*=\s*["\'][^"\']+["\']\s*$', data, re.M):
            raise ValueError(f'Possible literal credential needs review: {name}')
        checked += 1
    probes = ['work/probe.json', 'artifacts/probe.c', '.env', 'boards/k40s/local/lab.json',
              'installer/private/wpa_supplicant.conf', 'tools/mtkclient/mtk.py',
              'sources/libhybris/README.md', 'kernel/generated.ko', 'initramfs/authorized_keys']
    for probe in probes:
        result = subprocess.run(['git', 'check-ignore', '-q', '--', probe], cwd=ROOT)
        if result.returncode != 0:
            raise ValueError(f'Exclusion missing: {probe}')
    print(f'SOURCE_ONLY: {checked} staged files checked; no binaries/private roots/keys; exclusions verified')


if __name__ == '__main__':
    main()
