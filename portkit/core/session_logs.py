# SPDX-License-Identifier: MIT
"""Offline decoding of an explicitly described set of capture files.

No physical addresses, transport, board defaults or full-ring reconstruction.
Raw/private output is only written to a new directory after input validation.
"""
import hashlib
import json
from pathlib import Path
import re

from .captures import read_exact_capture
from .ramoops import FORMAT, decode_console


def _session_layout(policy, console_policy, overrides):
    if not isinstance(policy, dict) or set(policy) != {
            'captures', 'size_variants', 'console', 'unordered_text'}:
        raise ValueError('Invalid session layout fields')
    captures, variants = policy['captures'], policy['size_variants']
    if (not isinstance(captures, dict) or not 1 <= len(captures) <= 32 or
            any(not isinstance(name, str) or not re.fullmatch(r'[a-z][a-z0-9_-]{0,31}', name)
                for name in captures) or
            any(type(size) is not int or not 0 < size <= 16 * 1024 * 1024
                for size in captures.values())):
        raise ValueError('Invalid capture names, count or sizes')
    if not isinstance(variants, dict) or not set(variants) <= set(captures):
        raise ValueError('Unknown capture in size variants')
    for name, choices in variants.items():
        if (not isinstance(choices, list) or not choices or
                any(type(size) is not int or not 0 < size <= 16 * 1024 * 1024 for size in choices) or
                len(set(choices)) != len(choices) or captures[name] not in choices):
            raise ValueError('Invalid declared size variants')
    if not isinstance(overrides, dict) or not set(overrides) <= set(variants):
        raise ValueError('Capture size override is not declared by the profile')
    sizes = dict(captures)
    for name, size in overrides.items():
        if type(size) is not int or size not in variants[name]:
            raise ValueError('Capture size override is outside the profile choices')
        sizes[name] = size
    if sum(sizes.values()) > 64 * 1024 * 1024:
        raise ValueError('Session exceeds the 64 MiB host capture budget')
    console, unordered = policy['console'], policy['unordered_text']
    if (not isinstance(console, dict) or set(console) != {'capture', 'offset'} or
            not isinstance(console['capture'], str) or console['capture'] not in sizes or
            type(console['offset']) is not int or console['offset'] < 0):
        raise ValueError('Invalid session console location')
    if (not isinstance(unordered, list) or any(not isinstance(name, str) for name in unordered) or
            len(set(unordered)) != len(unordered) or not set(unordered) <= set(sizes) or
            set(unordered) | {console['capture']} != set(sizes)):
        raise ValueError('Invalid or unused unordered capture references')
    if (not isinstance(console_policy, dict) or set(console_policy) != {
            'format', 'zone_size', 'signature', 'ecc'} or console_policy['format'] != FORMAT):
        raise ValueError('Unsupported console codec profile')
    codec = dict(console_policy)
    codec.pop('format')
    if (type(codec['zone_size']) is not int or not 12 < codec['zone_size'] <= 16 * 1024 * 1024 or
            type(codec['signature']) is not int or not 0 <= codec['signature'] < 2**32 or
            type(codec['ecc']) is not int or codec['ecc'] != 0 or
            console['offset'] + codec['zone_size'] > sizes[console['capture']]):
        raise ValueError('Invalid codec or console extends outside its capture')
    return sizes, dict(console), list(unordered), codec


def decode_session(prefix, *, policy, console_policy, size_overrides=None):
    """Return decoded private outputs and report, without creating any files."""
    sizes, console, unordered, codec = _session_layout(
        policy, console_policy, {} if size_overrides is None else size_overrides)
    raw, sources = {}, {}
    for name, size in sizes.items():
        path = Path(str(prefix) + '-' + name + '.bin')
        raw[name], sources[name] = read_exact_capture(path, expected_bytes=size)
    start = console['offset']
    log, console_report = decode_console(
        raw[console['capture']][start:start + codec['zone_size']], **codec)
    outputs = {'console.log': log}
    for name in unordered:
        # Readable fragments may be stale/partial; this does not order a ring.
        chunks = re.findall(rb'[\x09\x0a\x0d\x20-\x7e]{8,}', raw[name])
        outputs[name + '-unordered.txt'] = b'\n'.join(chunks) + b'\n'
    report = {'sources': sources, 'console': console_report, 'phone_access': False,
              'raw_inputs_modified': False, 'nonconsole_ring_order_reconstructed': False,
              'boot_correlation_requires_manual_review': True,
              'outputs': {name: hashlib.sha256(data).hexdigest() for name, data in outputs.items()}}
    return outputs, report


def write_decoded_session(output, outputs, report):
    """Publish already decoded private data into a new directory, never replace."""
    if (not outputs or any(not isinstance(name, str) or
                           not re.fullmatch(r'[a-z][a-z0-9_-]*\.(?:log|txt)', name)
                           for name in outputs)):
        raise ValueError('Invalid decoded output names')
    output = Path(output)
    output.mkdir(parents=True, exist_ok=False)
    for name, data in outputs.items():
        with (output / name).open('xb') as stream:
            stream.write(data)
    with (output / 'decode-report.json').open('x', encoding='utf-8') as stream:
        json.dump(report, stream, indent=2)
    return report
