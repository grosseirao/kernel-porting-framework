#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Inspect metadata of an explicit Android DT table v0, without selecting a PCB.

Offline only. Reports hashes/headers, not raw FDT properties or active identity.
No image modification, overlay application, transport or boot authorization.
Relative input/output paths are anchored to the project root.
"""
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from portkit.core.android_dt import parse_dt_table
from portkit.core.captures import read_exact_capture
from portkit.core.evidence import write_evidence
from portkit.cli.dt_table import main as _toolkit_main


def main(argv=None):
    return _toolkit_main(argv, workspace=ROOT)


if __name__ == '__main__':
    raise SystemExit(main())
