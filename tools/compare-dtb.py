#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Compare two explicit DTBs offline; DTS/diff output is private and create-only.

Canonical equality is not binding validation, hardware equivalence or boot
authorization. Raw property values may contain identifiers/calibration.
"""
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from portkit.core.captures import read_exact_capture
from portkit.core.devicetree import compare_dtb
from portkit.core.evidence import write_evidence


from portkit.cli.dt_compare import main as _toolkit_main


def main(argv=None):
    return _toolkit_main(argv, workspace=ROOT)


if __name__ == '__main__':
    raise SystemExit(main())
