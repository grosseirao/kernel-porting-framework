# SPDX-License-Identifier: MIT
"""Filter explicit offline FDT/iomem captures using a board's node selectors.

No SSH, transport or device reads. Private properties/bootargs are not exported.
These captures and the supplied release do not prove the current device state.
Relative capture/output paths use the explicit workspace root.
"""
import argparse
from pathlib import Path
import re

from portkit.core.boot_snapshot import boot_snapshot
from portkit.core.captures import read_exact_capture, read_text_capture
from portkit.core.evidence import write_evidence
from portkit.profiles import load_board, _workspace_root


def main(argv=None, *, workspace=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--workspace', type=Path, default=workspace, required=workspace is None,
                        help='explicit absolute workspace for profile and capture paths')
    parser.add_argument('--board', required=True)
    parser.add_argument('--fdt', type=Path, required=True, help='existing binary FDT capture')
    parser.add_argument('--iomem', type=Path, required=True, help='existing iomem text capture')
    parser.add_argument('--kernel-release', required=True, help='release claimed by capture source, not live verification')
    parser.add_argument('--output', type=Path, required=True, help='new JSON evidence')
    args = parser.parse_args(argv)
    try:
        root = _workspace_root(args.workspace)
        if not root.is_dir():
            raise ValueError('Expected an existing workspace directory')

        for name in ('fdt', 'iomem', 'output'):
            path = getattr(args, name)
            if not path.is_absolute():
                setattr(args, name, root / path)
        if args.output.exists() or args.output.is_symlink():
            raise FileExistsError('Select new evidence; existing output is preserved')
        if not re.fullmatch(r'[A-Za-z0-9][A-Za-z0-9._+-]{0,255}', args.kernel_release):
            raise ValueError('Expected one kernel release token, not arbitrary captured text')
        board = load_board(root, args.board)
        policy = board['diagnostics']['boot_snapshot']
        data, fdt_source = read_exact_capture(args.fdt, expected_bytes=args.fdt.stat().st_size)
        iomem, iomem_source = read_text_capture(args.iomem)
        snapshot = boot_snapshot(data, iomem, args.kernel_release, **policy)
        snapshot.update(board=board['id'], sources=dict(fdt=fdt_source, iomem=iomem_source),
                        phone_access=False, boot_authorized=False)
        write_evidence(args.output, snapshot)
    except (OSError, ValueError, TypeError, KeyError) as error:
        parser.error(str(error))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
