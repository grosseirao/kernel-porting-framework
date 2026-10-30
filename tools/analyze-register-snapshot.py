#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Validate existing register log samples against an explicit board contract.

Exit 0 means a complete log protocol, not physical read-only behavior, valid
register semantics, stable hardware or authorization to execute diagnostics.
"""
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from portkit.core.captures import read_text_capture
from portkit.core.evidence import write_evidence
from portkit.core.register_snapshot import register_snapshot
from portkit.profiles import load_board


from portkit.cli.register_snapshot import main as _toolkit_main


def main(argv=None):
    return _toolkit_main(argv, workspace=ROOT)


if __name__ == '__main__':
    raise SystemExit(main())
