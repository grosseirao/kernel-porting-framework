# SPDX-License-Identifier: MIT
"""libfdt for parsing; only project-specific invariants live here.

Schema validation remains dt-schema's job; compilation/overlays remain DTC's.
No custom FDT binary parser or fallback is provided.
"""


def load_fdt(data):
    import libfdt
    return libfdt.Fdt(bytes(data))


def parse_fdt(data):
    """libfdt snapshot in the legacy (nodes, reservations) representation.

    This is an output adapter, not a binary parser. Never falls back to the
    historical parser if libfdt is unavailable or rejects an invalid blob.
    """
    import libfdt
    raw = bytearray(data)
    try:
        if libfdt.fdt_check_full(raw, len(raw)) != 0:
            raise ValueError('libfdt rejected malformed or truncated FDT')
        tree = libfdt.Fdt(raw)
        if tree.version() < 17:
            raise ValueError('FDT version before the reviewed v17 format')
        reserves = []
        for index in range(tree.num_mem_rsv()):
            address, size = tree.get_mem_rsv(index)
            reserves.append({'address': address, 'size': size})
        nodes = {}
        pending = [(0, '/')]
        while pending:
            offset, path = pending.pop()
            if path in nodes:
                raise ValueError('Duplicate FDT node path')
            props = {}
            prop_offset = tree.first_property_offset(offset, quiet=(libfdt.NOTFOUND,))
            while prop_offset >= 0:
                prop = tree.get_property_by_offset(prop_offset)
                prop.name.encode('ascii')
                if prop.name in props:
                    raise ValueError('Duplicate FDT property')
                props[prop.name] = bytes(prop)
                prop_offset = tree.next_property_offset(prop_offset, quiet=(libfdt.NOTFOUND,))
            nodes[path] = props
            children = []
            child = tree.first_subnode(offset, quiet=(libfdt.NOTFOUND,))
            while child >= 0:
                name = tree.get_name(child)
                name.encode('ascii')
                children.append((child, path.rstrip('/') + '/' + name))
                child = tree.next_subnode(child, quiet=(libfdt.NOTFOUND,))
            pending.extend(reversed(children))
        return nodes, reserves
    except (libfdt.FdtException, UnicodeError) as error:
        raise ValueError('Invalid FDT according to libfdt') from error


def require_property(tree, node, name, expected):
    if not isinstance(expected, bytes):
        raise ValueError('Expected exact property bytes, not inferred conversion')
    actual = bytes(tree.getprop(tree.path_offset(node), name))
    if actual != expected:
        raise ValueError(f'Board invariant violated: {node}/{name}')
    return True


def canonical_dts(data):
    """DTC's sorted DTS view of one valid v17+ blob, not hardware validation."""
    from .processes import run_bounded
    parse_fdt(data)
    result = run_bounded(['dtc', '-q', '-s', '-I', 'dtb', '-O', 'dts'],
                         input=data, capture_output=True, timeout=30)
    return result.stdout.decode('utf-8')


def compare_dtb(reference, candidate, *, candidate_label='candidate'):
    """Return comparison metadata and private DTS/diff; never publish implicitly.

    Raw property values/phandles are not rewritten to manufacture equivalence.
    """
    import difflib
    actual, built = canonical_dts(reference), canonical_dts(candidate)
    delta = ''.join(difflib.unified_diff(actual.splitlines(True), built.splitlines(True),
                                       fromfile='reference', tofile=candidate_label))
    return ({'byte_equal': reference == candidate, 'canonical_equal': actual == built,
             'diff_lines': len(delta.splitlines())}, actual, built, delta)


def compare_dtb_candidates(reference, candidates, *, read_candidate, fallback,
                           candidate_label='candidate'):
    """Select one canonical match, otherwise compare the explicit fallback.

    Candidate identifiers and their iteration order are supplied by the caller;
    read_candidate(identifier) supplies bytes. No filesystem discovery, board
    selection, value normalization or claim of hardware compatibility is made.
    All candidates are checked, including after a match. The selected candidate
    is read again as in the original workflow; inputs must be immutable captures.
    """
    actual = canonical_dts(reference)
    matches = [name for name in candidates
               if canonical_dts(read_candidate(name)) == actual]
    if len(matches) > 1:
        raise ValueError('More than one canonical DT candidate matches')
    selected = matches[0] if matches else fallback
    result, actual, built, delta = compare_dtb(
        reference, read_candidate(selected), candidate_label=candidate_label)
    return selected, result, actual, built, delta
