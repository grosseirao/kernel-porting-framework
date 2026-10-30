# SPDX-License-Identifier: MIT
"""MediaTek-only contract; current implementation remains the validated legacy CLI.

No mtkclient import or USB initialization is performed here. Board defaults are
validated locally; identification and reset still use the legacy CLI.
"""
from typing import Protocol


class MediaTekDA(Protocol):
    def identify_hwcode(self, *, timeout: float) -> int: ...
    def shutdown_reset_da(self, *, board: dict, authorization: str,
                          timeout: float) -> dict: ...


def validate_hwcode(hwcode, expected):
    if type(hwcode) is not int or type(expected) is not int or hwcode != expected:
        raise ValueError('Unexpected MediaTek hwcode; no session authorized')
    return hwcode


def board_session_defaults(board):
    """Expected identity and default log capture; not permission to open a DA."""
    hwcode = board['hwcode']
    region = board['dram']['atomic_logbuf']
    address, length = region['address'], region['bytes']
    if type(hwcode) is not int or not 0 < hwcode <= 0xffff:
        raise ValueError('Invalid expected MediaTek hwcode')
    if (type(address) is not int or type(length) is not int
            or not 0x40000000 <= address < 0xc0000000
            or not 0 < length <= 0x100000 or address % 4 or length % 4
            or address + length > 0xc0000000):
        raise ValueError('Invalid default MediaTek DRAM capture')
    return hwcode, address, length
