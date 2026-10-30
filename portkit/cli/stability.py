# SPDX-License-Identifier: MIT
"""Analyze an existing stability text capture using an explicit board profile.

Offline only: no phone transport or test execution. Exit 0 means the capture
reports a complete bounded pass, NOT physical qualification; exit 2 means an
incomplete/failed report or invalid input. Output evidence is create-only.
"""
import argparse
from pathlib import Path

from portkit.core.captures import read_text_capture
from portkit.core.evidence import write_evidence
from portkit.core.stability import stability_findings
from portkit.profiles import load_board, _workspace_root


def main(argv=None, *, workspace=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--workspace', type=Path, default=workspace, required=workspace is None,
                        help='explicit absolute workspace for profile and capture paths')
    parser.add_argument('--board', required=True, help='explicit board profile identifier')
    parser.add_argument('--log', type=Path, required=True, help='existing UTF-8 capture, at most 4 MiB')
    parser.add_argument('--output', type=Path, required=True, help='new JSON evidence file')
    args = parser.parse_args(argv)
    try:
        root = _workspace_root(args.workspace)
        if not root.is_dir():
            raise ValueError('Expected an existing workspace directory')
        args.log = (root / args.log).resolve()
        args.output = root / args.output
        board = load_board(root, args.board)
        policy = board['diagnostics']['stability']
        text, source = read_text_capture(args.log)
        findings = stability_findings(text, **policy)
        write_evidence(args.output, {
            'schema': 1, 'board': board['id'], 'source': source,
            'policy': policy, 'stability': findings, 'boot_authorized': False,
            'scope': 'offline capture interpretation, no device access or test execution',
        })
    except (OSError, ValueError, KeyError, TypeError) as error:
        parser.error(str(error))
    return 0 if findings['complete_bounded_test_reported_pass'] else 2


if __name__ == '__main__':
    raise SystemExit(main())
