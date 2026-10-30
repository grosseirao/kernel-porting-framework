# SPDX-License-Identifier: MIT
"""Check an explicit static DT node contract; no probe, MMIO or device access."""
import argparse
from pathlib import Path

from portkit.core.captures import read_exact_capture
from portkit.core.devicetree import parse_fdt
from portkit.core.dt_contracts import verify_node_contract
from portkit.core.evidence import write_evidence
from portkit.profiles import load_board, _workspace_root


def main(argv=None, *, workspace=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--workspace', type=Path, default=workspace, required=workspace is None,
                        help='explicit absolute workspace for profile and capture paths')
    parser.add_argument('--board', required=True)
    parser.add_argument('--contract', required=True, help='explicit contract name in the board profile')
    parser.add_argument('--fdt', type=Path, required=True)
    parser.add_argument('--output', type=Path, required=True, help='new JSON evidence')
    args = parser.parse_args(argv)
    try:
        root = _workspace_root(args.workspace)
        if not root.is_dir():
            raise ValueError('Expected an existing workspace directory')

        for name in ('fdt', 'output'):
            path = getattr(args, name)
            if not path.is_absolute():
                setattr(args, name, root / path)
        if args.output.exists() or args.output.is_symlink():
            raise FileExistsError('Select new evidence; existing output is preserved')
        board = load_board(root, args.board)
        contract = board['diagnostics']['dt_contracts'][args.contract]
        data, source = read_exact_capture(args.fdt, expected_bytes=args.fdt.stat().st_size)
        nodes, _ = parse_fdt(data)
        result = verify_node_contract(nodes, contract)
        write_evidence(args.output, {
            'schema': 1, 'board': board['id'], 'contract': args.contract, 'source': source,
            'node': result, 'static_contract_satisfied': True,
            'register_semantics_verified': False, 'driver_compatibility_verified': False,
            'phone_access': False, 'boot_authorized': False,
        })
    except (OSError, ValueError, TypeError, KeyError) as error:
        parser.error(str(error))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
