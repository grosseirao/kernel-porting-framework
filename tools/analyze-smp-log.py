#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Interpret an existing SMP text capture with explicit profile markers.

Exit 0 means analysis completed, NOT successful boot or physical CPU validation.
No transport, CPU power control or diagnostic execution. Output is create-only.
"""
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from portkit.core.captures import read_text_capture
from portkit.core.evidence import write_evidence
from portkit.core.smp import smp_findings
from portkit.profiles import load_board


from portkit.cli.smp import main as _toolkit_main


def main(argv=None):
    return _toolkit_main(argv, workspace=ROOT)


if __name__ == '__main__':
    raise SystemExit(main())
