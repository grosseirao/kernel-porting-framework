# SPDX-License-Identifier: MIT
"""Compare saved .config values against explicit fragments, offline.

Does not resolve Kconfig, build, configure or enable hardware. Exit 0 means the
requested literal values match, not that the device or kernel is functional.
Exit 2 means mismatch or invalid input. JSON evidence is create-only and omits
configuration values, which may contain private command lines or identities.
"""
import argparse
from pathlib import Path

from portkit.core.captures import read_text_capture
from portkit.core.evidence import write_evidence
from portkit.core.kconfig import config_values, mismatched_symbols
from portkit.profiles import _workspace_root


def main(argv=None, *, workspace=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--workspace', type=Path, default=workspace, required=workspace is None,
                        help='explicit absolute workspace; relative inputs/outputs use this root')
    parser.add_argument('--config', type=Path, required=True)
    parser.add_argument('--fragment', type=Path, action='append', required=True,
                        help='requirements in order, last assignment wins')
    parser.add_argument('--output', type=Path, required=True, help='new JSON report')
    args = parser.parse_args(argv)
    try:
        root = _workspace_root(args.workspace)
        if not root.is_dir():
            raise ValueError('Expected an explicit absolute existing workspace directory')
        args.config = (root / args.config).resolve()
        args.fragment = [(root / path).resolve() for path in args.fragment]
        args.output = root / args.output
        text, source = read_text_capture(args.config)
        actual = config_values(text)
        required, fragments = {}, []
        for path in args.fragment:
            text, identity = read_text_capture(path)
            values = config_values(text)
            if not values:
                raise ValueError('Requirement fragment has no saved Kconfig assignments')
            required.update(values)
            fragments.append(identity)
        mismatches = mismatched_symbols(actual, required)
        write_evidence(args.output, {
            'schema': 1, 'config': source, 'fragments': fragments,
            'required_symbols': list(required), 'mismatched_symbols': mismatches,
            'requirements_satisfied': not mismatches,
            'values_exported': False, 'dependencies_resolved': False,
            'phone_access': False, 'boot_authorized': False,
        })
    except (OSError, ValueError) as error:
        parser.error(str(error))
    return 2 if mismatches else 0


if __name__ == '__main__':
    raise SystemExit(main())
