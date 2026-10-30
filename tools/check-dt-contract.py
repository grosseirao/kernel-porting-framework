#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Check an explicit static DT node contract; no probe, MMIO or device access."""
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from portkit.core.captures import read_exact_capture
from portkit.core.devicetree import parse_fdt
from portkit.core.dt_contracts import verify_node_contract
from portkit.core.evidence import write_evidence
from portkit.profiles import load_board


from portkit.cli.dt_contract import main as _toolkit_main


def main(argv=None):
    return _toolkit_main(argv, workspace=ROOT)


if __name__ == '__main__':
    raise SystemExit(main())
