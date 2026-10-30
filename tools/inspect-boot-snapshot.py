#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Filter explicit offline FDT/iomem captures using a board's node selectors.

No SSH, transport or device reads. Private properties/bootargs are not exported.
These captures and the supplied release do not prove the current device state.
Relative capture/output paths are anchored to the project root.
"""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from portkit.core.boot_snapshot import boot_snapshot
from portkit.core.captures import read_exact_capture, read_text_capture
from portkit.core.evidence import write_evidence
from portkit.profiles import load_board


from portkit.cli.boot_snapshot import main as _toolkit_main


def main(argv=None):
    return _toolkit_main(argv, workspace=ROOT)


if __name__ == '__main__':
    raise SystemExit(main())
