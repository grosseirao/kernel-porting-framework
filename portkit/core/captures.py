# SPDX-License-Identifier: MIT
"""Bounded reads and byte identities for explicit offline captures."""
import hashlib
from pathlib import Path


MAX_TEXT_CAPTURE = 4 * 1024 * 1024


def read_exact_capture(path, *, expected_bytes):
    """Read an explicit regular binary snapshot, never guess a capture size.

    The 16 MiB bound is a host allocation guard, not a hardware capability.
    """
    if type(expected_bytes) is not int or not 0 < expected_bytes <= 16 * 1024 * 1024:
        raise ValueError('Expected a capture size between 1 byte and 16 MiB')
    path = Path(path)
    if not path.is_file() or path.stat().st_size != expected_bytes:
        raise ValueError('Requires an existing regular capture of the exact declared size')
    with path.open('rb') as stream:
        raw = stream.read(expected_bytes + 1)
    if len(raw) != expected_bytes:
        raise ValueError('Capture size changed during reading')
    return raw, {'file': path.name, 'size': len(raw),
                 'sha256': hashlib.sha256(raw).hexdigest()}


def read_text_capture(path, *, max_bytes=MAX_TEXT_CAPTURE):
    """Return text and byte identity, without exporting an absolute source path.

    Binary dumps need a separate decoder. The limit is applied both before and
    during reading so a growing capture cannot cause an unbounded allocation.
    """
    if type(max_bytes) is not int or max_bytes <= 0:
        raise ValueError('Expected a positive capture byte limit')
    path = Path(path)
    if not path.is_file() or path.stat().st_size > max_bytes:
        raise ValueError('Requires an existing text capture within the byte limit')
    with path.open('rb') as stream:
        raw = stream.read(max_bytes + 1)
    if len(raw) > max_bytes:
        raise ValueError('Text capture exceeded the byte limit during reading')
    if b'\0' in raw:
        raise ValueError('Text capture required; decode/identify a raw memory dump separately')
    return raw.decode('utf-8'), {'file': path.name, 'size': len(raw),
                               'sha256': hashlib.sha256(raw).hexdigest()}
