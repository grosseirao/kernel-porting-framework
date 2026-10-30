# SPDX-License-Identifier: MIT
"""Declarative UML test sets; never import executable configuration."""
import hashlib
import json
from pathlib import Path, PurePosixPath
import re
from types import SimpleNamespace


HOST_FORBIDDEN = ('NET', 'UML_NET', 'HOSTFS', 'MCONSOLE', 'MODULES', 'KUNIT_ALL_TESTS')


def load_test_set(path, root):
    root = Path(root).resolve()
    path = (root / Path(path)).resolve()
    if not path.is_relative_to(root):
        raise ValueError('Test set must be inside the project')
    data = json.loads(path.read_text(encoding='utf-8'))
    keys = {'schema', 'id', 'VERSION', 'ARCHIVE', 'ARCHIVE_SHA', 'PATCH', 'INPUTS',
            'SOC_INPUTS', 'SOC_PATCHES', 'CONFIG', 'UPSTREAM_INPUTS', 'EXPECTED_SUITES',
            'FORBIDDEN_CONFIG', 'REQUIRED_CONFIG', 'TRACKED_PARENT_FILES', 'TRACKED_EXTRA_FILES'}
    if not isinstance(data, dict) or set(data) != keys or type(data['schema']) is not int or data['schema'] != 1:
        raise ValueError('Unknown KUnit test-set schema or fields')
    if not isinstance(data['id'], str) or not re.fullmatch('[a-z0-9-]{1,64}', data['id']):
        raise ValueError('Invalid test-set id')
    if not isinstance(data['VERSION'], str) or not re.fullmatch(r'[0-9]+\.[0-9]+(?:\.[0-9]+)?', data['VERSION']):
        raise ValueError('Explicit kernel release required')

    def relative(value, local=False):
        if (not isinstance(value, str) or not value or '\\' in value or ':' in value or
                '\0' in value or PurePosixPath(value).is_absolute() or
                any(part in ('', '.', '..') for part in value.split('/'))):
            raise ValueError('Expected confined relative path')
        if local and not (root / value).resolve().is_relative_to(root):
            raise ValueError('Input symlink escapes project')

    def digest(value):
        if not isinstance(value, str) or not re.fullmatch('[0-9a-f]{64}', value):
            raise ValueError('Explicit SHA256 required')

    def string_list(value):
        if not isinstance(value, list) or any(not isinstance(item, str) or not item for item in value):
            raise ValueError('Explicit list of nonempty strings required')
        if len(set(value)) != len(value):
            raise ValueError('Duplicate list entry')

    for field in ('ARCHIVE', 'PATCH', 'CONFIG'):
        relative(data[field], local=True)
    digest(data['ARCHIVE_SHA'])
    for field in ('UPSTREAM_INPUTS', 'SOC_INPUTS', 'INPUTS'):
        mapping = data[field]
        if not isinstance(mapping, dict):
            raise ValueError('Expected input mapping')
        for name, value in mapping.items():
            relative(name, local=field == 'INPUTS')
            if field == 'INPUTS':
                relative(value)
            else:
                digest(value)
    if len(set(data['INPUTS'].values())) != len(data['INPUTS']):
        raise ValueError('Duplicate installed target')
    for field in ('SOC_PATCHES', 'TRACKED_PARENT_FILES', 'TRACKED_EXTRA_FILES'):
        string_list(data[field])
        for value in data[field]:
            relative(value, local=field == 'SOC_PATCHES')
    for field in ('FORBIDDEN_CONFIG', 'REQUIRED_CONFIG'):
        string_list(data[field])
        if any(not re.fullmatch('[A-Z0-9_]+', symbol) for symbol in data[field]):
            raise ValueError('Invalid Kconfig symbol')
    forbidden = set(HOST_FORBIDDEN) | set(data['FORBIDDEN_CONFIG'])
    if forbidden.intersection(data['REQUIRED_CONFIG']):
        raise ValueError('Required and forbidden configurations overlap')
    suites = data['EXPECTED_SUITES']
    if not isinstance(suites, dict) or not suites:
        raise ValueError('Nonempty expected suites required')
    names = set()
    for name, cases in suites.items():
        if not name:
            raise ValueError('Empty suite name')
        string_list(cases)
        if not cases or names.intersection(cases):
            raise ValueError('Empty suite or ambiguous case name')
        names.update(cases)
    fingerprint = hashlib.sha256(json.dumps(data, sort_keys=True, separators=(',', ':')).encode()).hexdigest()
    data['EXPECTED_SUITES'] = {name: set(cases) for name, cases in suites.items()}
    return SimpleNamespace(**data, fingerprint=fingerprint, path=path,
                           EXPECTED_CASES=names)
