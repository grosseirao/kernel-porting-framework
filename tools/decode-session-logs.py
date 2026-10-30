#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Decode a declared offline capture set; private output, no device access."""
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from portkit.core.session_logs import decode_session, write_decoded_session
from portkit.profiles import load_board


from portkit.cli.session_logs import main as _toolkit_main


def main(argv=None):
    return _toolkit_main(argv, workspace=ROOT)


if __name__ == '__main__':
    raise SystemExit(main())
