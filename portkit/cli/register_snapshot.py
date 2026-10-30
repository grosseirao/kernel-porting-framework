# SPDX-License-Identifier: MIT
"""Validate existing register log samples against an explicit board contract.

Exit 0 means a complete log protocol, not physical read-only behavior, valid
register semantics, stable hardware or authorization to execute diagnostics.
"""
import argparse
from pathlib import Path

from portkit.core.captures import read_text_capture
from portkit.core.evidence import write_evidence
from portkit.core.register_snapshot import register_snapshot
from portkit.profiles import load_board, _workspace_root


def main(argv=None, *, workspace=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--workspace', type=Path, default=workspace, required=workspace is None,
                        help='explicit absolute workspace for profile and capture paths')
    parser.add_argument('--board', required=True)
    parser.add_argument('--contract', required=True)
    parser.add_argument('--log', type=Path, required=True)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args(argv)
    try:
        root = _workspace_root(args.workspace)
        if not root.is_dir():
            raise ValueError('Expected an existing workspace directory')
        args.log = (root / args.log).resolve()
        args.output = root / args.output
        board = load_board(root, args.board)
        policy = board['diagnostics']['register_snapshots'][args.contract]
        text, source = read_text_capture(args.log)
        snapshot = register_snapshot(text, **policy)
        write_evidence(args.output, {
            'schema': 1, 'board': board['id'], 'contract': args.contract, 'source': source,
            'snapshot': snapshot, 'log_protocol_complete': True,
            'register_semantics_verified': False, 'physical_read_only_verified': False,
            'phone_access': False, 'boot_authorized': False,
        })
    except (OSError, ValueError, KeyError, TypeError) as error:
        parser.error(str(error))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
