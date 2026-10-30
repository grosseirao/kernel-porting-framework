# SPDX-License-Identifier: MIT
"""Inspect metadata of an explicit Android DT table v0, without selecting a PCB.

Offline only. Reports hashes/headers, not raw FDT properties or active identity.
No image modification, overlay application, transport or boot authorization.
Relative input/output paths use the explicit workspace root.
"""
import argparse
from pathlib import Path

from portkit.core.android_dt import parse_dt_table
from portkit.core.captures import read_exact_capture
from portkit.core.evidence import write_evidence
from portkit.profiles import _workspace_root


def main(argv=None, *, workspace=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--workspace', type=Path, default=workspace, required=workspace is None,
                        help='absolute existing workspace for relative input/output paths')
    parser.add_argument('--input', type=Path, required=True, help='existing Android DT table v0')
    parser.add_argument('--output', type=Path, required=True, help='new JSON metadata report')
    args = parser.parse_args(argv)
    try:
        root = _workspace_root(args.workspace)
        if not root.is_dir():
            raise ValueError('Expected an existing workspace directory')
        for name in ('input', 'output'):
            path = getattr(args, name)
            if not path.is_absolute():
                setattr(args, name, root / path)
        if args.output.exists() or args.output.is_symlink():
            raise FileExistsError('Select a new metadata report; existing output is preserved')
        data, source = read_exact_capture(args.input, expected_bytes=args.input.stat().st_size)
        rows = parse_dt_table(data)
        write_evidence(args.output, {
            'schema': 1, 'format': 'android-dt-table-v0', 'source': source,
            'entries': [entry for entry, _ in rows], 'active_entry_selected': False,
            'raw_properties_exported': False, 'phone_access': False, 'boot_authorized': False,
        })
    except (OSError, ValueError) as error:
        parser.error(str(error))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
