# SPDX-License-Identifier: MIT
"""Streaming SHA-256 shared by host tools; no implicit device reads."""
import hashlib
from pathlib import Path
import re


def sha256(path):
    digest = hashlib.sha256()
    with Path(path).open('rb') as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b''):
            digest.update(block)
    return digest.hexdigest()


def verify_sha256(path, expected):
    if not isinstance(expected, str) or not re.fullmatch('[0-9a-f]{64}', expected):
        raise ValueError('Expected lowercase SHA-256, not an implicit trust value')
    actual = sha256(path)
    if actual != expected:
        raise ValueError('SHA-256 mismatch')
    return actual
