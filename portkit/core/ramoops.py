# SPDX-License-Identifier: MIT
"""Decode one explicitly identified LE32/ECC0 persistent RAM console zone.

No layout inference, ECC correction, physical reads or boot correlation. The
signature is the actual expected header value, including any type XOR.
"""
import struct

FORMAT = 'persistent-ram-console-le32-ecc0'


def decode_console(data, *, zone_size, signature, ecc=0):
    if (type(zone_size) is not int or not 12 < zone_size <= 16 * 1024 * 1024 or
            type(signature) is not int or not 0 <= signature < 2**32 or
            type(ecc) is not int or ecc != 0):
        raise ValueError('Requires an explicit console size/signature and ECC=0')
    if len(data) != zone_size:
        raise ValueError('Requires the exact declared console zone')
    observed, start, size = struct.unpack_from('<III', data)
    capacity = len(data) - 12
    if observed != signature or size > capacity or start > size:
        raise ValueError('Invalid persistent RAM signature, start or size')
    log = data[12 + start:12 + size] + data[12:12 + start]
    return log, {'format': FORMAT, 'signature': observed,
                 'start': start, 'size': size, 'capacity': capacity,
                 'retention_across_reboot_verified': False}
