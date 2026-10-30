# SPDX-License-Identifier: MIT
"""Read Android DT table v0 containers without board selection or extraction.

Only the reviewed 32-byte entry format is accepted. The container's IDs/custom
fields are opaque metadata, not proof of active PCB or hardware compatibility.
"""
import hashlib
import struct

from .devicetree import parse_fdt


def parse_dt_table(data):
    """Return (entry metadata, FDT bytes) rows, preserving order and exact bytes."""
    if len(data) < 32:
        raise ValueError('Short DT table')
    magic, total, header, stride, count, offset, _, version = struct.unpack_from('>8I', data)
    if (magic != 0xd7b7ab1e or total > len(data) or header < 32 or stride != 32 or
            offset < header or offset + count * stride > total or version != 0):
        raise ValueError('Unsupported/invalid Android DT table')
    result = []
    for index in range(count):
        size, start, ident, rev, *custom = struct.unpack_from('>8I', data, offset + index * stride)
        if start < offset + count * stride or start + size > total:
            raise ValueError('DT entry outside payload or overlapping headers')
        blob = data[start:start + size]
        parse_fdt(blob)
        result.append(({'index': index, 'id': ident, 'revision': rev, 'custom': custom,
                        'offset': start, 'size': size, 'sha256': hashlib.sha256(blob).hexdigest()}, blob))
    return result
