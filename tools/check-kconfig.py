#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Compare saved .config values against explicit fragments, offline.

Does not resolve Kconfig, build, configure or enable hardware. Exit 0 means the
requested literal values match, not that the device or kernel is functional.
Exit 2 means mismatch or invalid input. JSON evidence is create-only and omits
configuration values, which may contain private command lines or identities.
"""
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from portkit.core.captures import read_text_capture
from portkit.core.evidence import write_evidence
from portkit.core.kconfig import config_values, mismatched_symbols
from portkit.cli.kconfig import main as _toolkit_main


def main(argv=None):
    return _toolkit_main(argv, workspace=ROOT)


if __name__ == '__main__':
    raise SystemExit(main())
