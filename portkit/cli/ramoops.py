# SPDX-License-Identifier: MIT
"""Decode one existing console-only dump using an explicit board profile.

Offline only. Output includes private raw console contents; choose a new private
directory. Does not scan full pstore, infer a layout or access device memory.
"""
import argparse
import hashlib
from pathlib import Path

from portkit.core.captures import read_exact_capture
from portkit.core.evidence import write_evidence
from portkit.core.ramoops import FORMAT, decode_console
from portkit.profiles import load_board, _workspace_root


def main(argv=None, *, workspace=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--workspace', type=Path, default=workspace, required=workspace is None,
                        help='explicit absolute workspace for profile and capture paths')
    parser.add_argument('--board', required=True)
    parser.add_argument('--console-dump', type=Path, required=True)
    parser.add_argument('--output', type=Path, required=True, help='new private directory')
    args = parser.parse_args(argv)
    try:
        root = _workspace_root(args.workspace)
        if not root.is_dir():
            raise ValueError('Expected an existing workspace directory')
        args.console_dump = (root / args.console_dump).resolve()
        args.output = root / args.output
        if args.output.exists() or args.output.is_symlink():
            raise FileExistsError('Refusing existing console output before input reads')
        board = load_board(root, args.board)
        policy = dict(board['diagnostics']['ramoops_console'])
        if policy.pop('format') != FORMAT:
            raise ValueError('Unsupported console format; no layout inference')
        data, source = read_exact_capture(args.console_dump, expected_bytes=policy['zone_size'])
        log, report = decode_console(data, **policy)
        report.update(board=board['id'], source=source,
                      log_sha256=hashlib.sha256(log).hexdigest(),
                      input_modified=False, phone_access=False, boot_authorized=False)
        args.output.mkdir(parents=True, exist_ok=False)
        with (args.output / 'console.log').open('xb') as stream:
            stream.write(log)
        write_evidence(args.output / 'report.json', report)
    except (OSError, ValueError, KeyError, TypeError) as error:
        parser.error(str(error))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
