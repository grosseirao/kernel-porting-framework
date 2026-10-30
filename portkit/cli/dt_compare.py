# SPDX-License-Identifier: MIT
"""Compare two explicit DTBs offline; DTS/diff output is private and create-only.

Canonical equality is not binding validation, hardware equivalence or boot
authorization. Raw property values may contain identifiers/calibration.
"""
import argparse
from pathlib import Path
import subprocess

from portkit.core.captures import read_exact_capture
from portkit.core.devicetree import compare_dtb
from portkit.core.evidence import write_evidence
from portkit.profiles import _workspace_root


def main(argv=None, *, workspace=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--workspace', type=Path, default=workspace, required=workspace is None,
                        help='explicit absolute workspace for profile and capture paths')
    parser.add_argument('--reference', type=Path, required=True)
    parser.add_argument('--candidate', type=Path, required=True)
    parser.add_argument('--output', type=Path, required=True, help='new private directory')
    args = parser.parse_args(argv)
    try:
        root = _workspace_root(args.workspace)
        if not root.is_dir():
            raise ValueError('Expected an existing workspace directory')
        args.reference = (root / args.reference).resolve()
        args.candidate = (root / args.candidate).resolve()
        args.output = root / args.output
        if args.output.exists() or args.output.is_symlink():
            raise FileExistsError('Refusing existing comparison output')
        reference, reference_id = read_exact_capture(args.reference, expected_bytes=args.reference.stat().st_size)
        candidate, candidate_id = read_exact_capture(args.candidate, expected_bytes=args.candidate.stat().st_size)
        report, actual, built, delta = compare_dtb(reference, candidate)
        report.update(schema=1, reference=reference_id, candidate=candidate_id,
                      bindings_validated=False, phone_access=False, boot_authorized=False)
        args.output.mkdir(parents=True, exist_ok=False)
        for name, text in (('reference.dts', actual), ('candidate.dts', built), ('comparison.diff', delta)):
            with (args.output / name).open('x', encoding='utf-8') as stream:
                stream.write(text)
        write_evidence(args.output / 'comparison.json', report)
    except (OSError, ValueError, subprocess.SubprocessError) as error:
        parser.error(str(error))
    return 0 if report['canonical_equal'] else 2


if __name__ == '__main__':
    raise SystemExit(main())
