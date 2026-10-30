# SPDX-License-Identifier: MIT
"""Decode a declared offline capture set; private output, no device access."""
import argparse
from pathlib import Path

from portkit.core.session_logs import decode_session, write_decoded_session
from portkit.profiles import load_board, _workspace_root


def main(argv=None, *, workspace=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--workspace', type=Path, default=workspace, required=workspace is None,
                        help='explicit absolute workspace for profile and capture paths')
    parser.add_argument('--board', required=True)
    parser.add_argument('prefix', type=Path, help='existing PREFIX-NAME.bin capture files')
    parser.add_argument('output', type=Path, help='new private directory')
    parser.add_argument('--capture-size', action='append', default=[], metavar='NAME=BYTES',
                        help='only a size variant explicitly allowed by the selected profile')
    args = parser.parse_args(argv)
    try:
        root = _workspace_root(args.workspace)
        if not root.is_dir():
            raise ValueError('Expected an existing workspace directory')

        for name in ('prefix', 'output'):
            path = getattr(args, name)
            if not path.is_absolute():
                setattr(args, name, root / path)
        if args.output.exists() or args.output.is_symlink():
            raise FileExistsError('Select a new private directory; existing output is preserved')
        board = load_board(root, args.board)
        diagnostics = board['diagnostics']
        overrides = {}
        for item in args.capture_size:
            name, value = item.split('=', 1)
            if name in overrides:
                raise ValueError('Repeated capture size override')
            overrides[name] = int(value, 0)
        outputs, report = decode_session(args.prefix,
            policy=diagnostics['session_logs'], console_policy=diagnostics['ramoops_console'],
            size_overrides=overrides)
        report.update(schema=1, board=board['id'], boot_authorized=False,
                      layout=diagnostics['session_logs'],
                      console_policy=diagnostics['ramoops_console'], size_overrides=overrides)
        write_decoded_session(args.output, outputs, report)
    except (OSError, ValueError, TypeError, KeyError) as error:
        parser.error(str(error))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
