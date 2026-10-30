#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Analyze an existing stability text capture using an explicit board profile.

Offline only: no phone transport or test execution. Exit 0 means the capture
reports a complete bounded pass, NOT physical qualification; exit 2 means an
incomplete/failed report or invalid input. Output evidence is create-only.
"""
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from portkit.core.captures import read_text_capture
from portkit.core.evidence import write_evidence
from portkit.core.stability import stability_findings
from portkit.profiles import load_board


from portkit.cli.stability import main as _toolkit_main


def main(argv=None):
    return _toolkit_main(argv, workspace=ROOT)


if __name__ == '__main__':
    raise SystemExit(main())
