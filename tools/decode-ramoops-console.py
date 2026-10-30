#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Decode one existing console-only dump using an explicit board profile.

Offline only. Output includes private raw console contents; choose a new private
directory. Does not scan full pstore, infer a layout or access device memory.
"""
import hashlib
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from portkit.core.captures import read_exact_capture
from portkit.core.evidence import write_evidence
from portkit.core.ramoops import FORMAT, decode_console
from portkit.profiles import load_board


from portkit.cli.ramoops import main as _toolkit_main


def main(argv=None):
    return _toolkit_main(argv, workspace=ROOT)


if __name__ == '__main__':
    raise SystemExit(main())
