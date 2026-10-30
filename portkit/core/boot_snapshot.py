# SPDX-License-Identifier: MIT
"""Allow-listed boot metadata from explicit FDT/iomem captures, without transport."""
from .devicetree import parse_fdt

PROPERTIES = frozenset({
    'compatible', 'reg', 'interrupts', 'interrupt-parent', '#address-cells',
    '#size-cells', '#interrupt-cells', '#redistributor-regions', 'method',
    'clock-frequency', 'status', 'no-map', 'size', 'alignment', 'alloc-ranges',
    'clock-names', 'clocks', 'device_type', 'enable-method',
})


def _selectors(values, *, prefixes=False):
    if (not isinstance(values, (list, tuple)) or
            any(not isinstance(value, str) or not value.startswith('/') or '\0' in value or
                '..' in value.split('/') or (prefixes and value == '/') for value in values)):
        raise ValueError('Expected explicit absolute node selectors, not a whole-tree prefix')
    return tuple(values)


def boot_snapshot(data, iomem, release, *, node_paths, node_prefixes):
    paths = _selectors(node_paths)
    prefixes = _selectors(node_prefixes, prefixes=True)
    nodes, reserves = parse_fdt(data)
    selected = {}
    for path, props in nodes.items():
        if path == '/chosen' or path.startswith('/chosen/'):
            continue
        if path in paths or path.startswith(prefixes):
            selected[path] = {key: value.hex() for key, value in props.items() if key in PROPERTIES}
    ram = []
    for line in iomem.splitlines():
        if line.endswith(' : System RAM') and not line.startswith(' '):
            start, last = line.split(' : ')[0].split('-')
            start, last = int(start, 16), int(last, 16)
            if start < 0 or last < start:
                raise ValueError('Invalid captured System RAM interval')
            ram.append({'address': start, 'size': last - start + 1})
    return {'schema': 1, 'kernel_release': release.strip(), 'source': 'offline FDT and iomem captures',
            'raw_fdt_saved': False, 'bootargs_saved': False,
            'properties_encoding': 'big-endian bytes as hex; paths/properties allow-listed',
            'nodes': selected, 'fdt_reservations': reserves, 'system_ram': ram,
            'warning': 'Captures may be stale or unrelated; current device state and later boot are not proven'}
