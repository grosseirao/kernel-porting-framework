# SPDX-License-Identifier: MIT
"""Deterministic manifests over explicit input files; no workspace crawling."""
from pathlib import Path
from .hashes import sha256


def file_manifest(root, names):
    root = Path(root).resolve()
    result = {}
    for name in sorted(names):
        relative = Path(name)
        path = root / relative
        if relative.is_absolute() or '..' in relative.parts or path.is_symlink():
            raise ValueError('Unsafe manifest path')
        resolved = path.resolve()
        if not resolved.is_relative_to(root) or not resolved.is_file():
            raise ValueError('Missing or escaping manifest input')
        key = relative.as_posix()
        if key in result:
            raise ValueError('Duplicate manifest input')
        result[key] = {'sha256': sha256(resolved), 'bytes': resolved.stat().st_size}
    return {'schema': 1, 'files': result}
