# SPDX-License-Identifier: MIT
"""Parse the decimal N,N-M subset of Linux CPU lists, without device access."""
import re


def parse_cpu_list(value, *, max_cpus=64):
    """Return sorted distinct IDs; do not infer topology or online CPU state.

    Bitmap, stride and grouping syntax are deliberately not supported. The
    caller supplies its supported ID bound; this is not a hardware limit.
    """
    if type(max_cpus) is not int or not 1 <= max_cpus <= 4096:
        raise ValueError('Invalid supported CPU count')
    result = set()
    for part in value.strip().split(','):
        if not re.fullmatch(r'\d+(?:-\d+)?', part):
            raise ValueError('Invalid CPU list')
        ends = list(map(int, part.split('-')))
        low, high = (ends[0], ends[-1])
        if not 0 <= low <= high < max_cpus:
            raise ValueError('CPU list outside supported range')
        result.update(range(low, high + 1))
    return sorted(result)
