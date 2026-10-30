# SPDX-License-Identifier: MIT
"""Interpret an existing SMP text capture with explicit profile markers.

Exit 0 means analysis completed, NOT successful boot or physical CPU validation.
No transport, CPU power control or diagnostic execution. Output is create-only.
"""
import argparse
from pathlib import Path

from portkit.core.captures import read_text_capture
from portkit.core.evidence import write_evidence
from portkit.core.smp import smp_findings
from portkit.profiles import load_board, _workspace_root


def main(argv=None, *, workspace=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--workspace', type=Path, default=workspace, required=workspace is None,
                        help='explicit absolute workspace for profile and capture paths')
    parser.add_argument('--board', required=True)
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
        policy = board['diagnostics']['smp']
        text, source = read_text_capture(args.log)
        findings = smp_findings(text, **policy)
        write_evidence(args.output, {
            'schema': 1, 'board': board['id'], 'source': source, 'policy': policy,
            'smp': findings, 'phone_access': False, 'boot_authorized': False,
            'physical_cpu_online_verified': False, 'boot_correlation_confirmed': False,
        })
    except (OSError, ValueError, KeyError, TypeError) as error:
        parser.error(str(error))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
