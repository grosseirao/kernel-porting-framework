# SPDX-License-Identifier: MIT
"""Exact static DT invariants; no address translation or hardware qualification."""
import struct


def cells(data):
    if len(data) % 4:
        raise ValueError('Unaligned DT cells')
    return list(struct.unpack('>' + 'I' * (len(data) // 4), data))


def require_bus_cells(nodes, parent, *, address_cells, size_cells,
                      message='Unexpected parent address/size cells'):
    if any(type(value) is not int or not 0 <= value <= 4
           for value in (address_cells, size_cells)):
        raise ValueError('Explicit supported address/size cell counts required')
    node = nodes.get(parent, {})
    if (node.get('#address-cells') != struct.pack('>I', address_cells) or
            node.get('#size-cells') != struct.pack('>I', size_cells)):
        raise ValueError(message)


def unique_compatible(nodes, compatible, *, message='Expected one compatible node'):
    if not isinstance(compatible, bytes) or not compatible or b'\0' in compatible:
        raise ValueError('Expected one exact compatible token')
    matches = [(path, node) for path, node in nodes.items()
               if compatible in node.get('compatible', b'').split(b'\0')]
    if len(matches) != 1:
        raise ValueError(message)
    return matches[0]


def require_available(node, *, message='DT node disabled'):
    if node.get('status', b'okay\0') not in (b'okay\0', b'ok\0'):
        raise ValueError(message)


def verify_node_contract(nodes, contract):
    """Verify explicit bytes and report only selected metadata, never raw props.

    Parent is checked literally; no ranges/IRQ/clock translation is inferred.
    """
    if not isinstance(contract, dict) or set(contract) != {
            'compatible', 'parent', 'address_cells', 'size_cells',
            'properties', 'require_available'}:
        raise ValueError('Invalid DT contract fields')
    compatible, parent = contract['compatible'], contract['parent']
    if (not isinstance(compatible, str) or not isinstance(parent, str) or
            not parent.startswith('/') or '\0' in parent or '..' in parent.split('/') or
            type(contract['require_available']) is not bool):
        raise ValueError('Invalid DT contract selector or availability policy')
    require_bus_cells(nodes, parent, address_cells=contract['address_cells'],
                      size_cells=contract['size_cells'])
    path, node = unique_compatible(nodes, compatible.encode('ascii'))
    if (path.rsplit('/', 1)[0] or '/') != parent:
        raise ValueError('Compatible node is not under the declared parent')
    properties = contract['properties']
    if not isinstance(properties, dict):
        raise ValueError('Expected a map of exact DT property bytes')
    for name, encoded in properties.items():
        if (not isinstance(name, str) or not name or '/' in name or '\0' in name or
                not isinstance(encoded, str)):
            raise ValueError('Invalid property contract encoding')
        expected = bytes.fromhex(encoded)
        if node.get(name) != expected:
            raise ValueError('DT property contract mismatch: ' + name)
    if contract['require_available']:
        require_available(node)
    return {'path': path, 'compatible': [compatible],
            'verified_properties': list(properties), 'availability_required': contract['require_available']}
