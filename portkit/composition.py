# SPDX-License-Identifier: MIT
"""Offline component inventory, NOT DT, Kconfig, deployment or driver loading."""
import hashlib
import json
from pathlib import PurePosixPath

from portkit.profiles import load_board, _unique_object, _invalid_constant, _workspace_root


def _relative(name):
    if (not isinstance(name, str) or not name or not PurePosixPath(name).parts or '\\' in name or ':' in name
            or PurePosixPath(name).is_absolute() or '..' in PurePosixPath(name).parts):
        raise ValueError('Invalid component source path')
    return PurePosixPath(name)


def component_source(project, name):
    """Resolve one explicit shared kernel input, never a board or parent lookup."""
    root = _workspace_root(project)
    relative = _relative(name)
    namespace = root / 'kernel/components'
    path = root / relative
    if (not relative.is_relative_to('kernel/components') or
            not path.resolve().is_relative_to(namespace) or not path.is_file() or
            any(p.is_symlink() for p in [path, *path.parents]
                if p != root and p.is_relative_to(root))):
        raise ValueError('Missing or escaping shared component source')
    return path


def load_composition(project, board_name, *, components_root=None):
    root = _workspace_root(project)
    # Never discover a parent checkout or fall back from an explicit selection.
    shared = root if components_root is None else _workspace_root(components_root)
    # Dependency is already pinned in the official WSL development environment.
    try:
        from jsonschema import Draft202012Validator, ValidationError, SchemaError
    except ImportError as error:
        raise ValueError('Use the official WSL/Linux venv with jsonschema 4.26.0') from error
    inputs = {}

    def hash_source(name, namespace, *, source_root=None):
        base = root if source_root is None else source_root
        relative = _relative(name)
        path = (component_source(base, name) if source_root is not None else base / relative)
        if (not relative.is_relative_to(namespace) or not path.resolve().is_relative_to(base/namespace)
                or not path.is_file()
                or any(p.is_symlink() for p in [path, *path.parents] if p != base and p.is_relative_to(base))):
            raise ValueError('Missing or escaping component/board source')
        inputs[name] = hashlib.sha256(path.read_bytes()).hexdigest()

    def read(name, namespace):
        relative = _relative(name)
        if not relative.is_relative_to(PurePosixPath(namespace)):
            raise ValueError('Component input outside its namespace')
        base = shared if namespace == 'components' else root
        path = base / relative
        if (not path.resolve().is_relative_to(base / namespace)
                or any(p.is_symlink() for p in [path, *path.parents] if p != base and p.is_relative_to(base))):
            raise ValueError('Escaping or symlinked component input')
        data = path.read_bytes()
        inputs[name] = hashlib.sha256(data).hexdigest()
        return json.loads(data.decode('utf-8'), object_pairs_hook=_unique_object,
                          parse_constant=_invalid_constant)

    validators = {}
    for kind in ('catalog', 'component', 'composition'):
        schema = read(f'components/schemas/{kind}.json', 'components')
        # The reviewed schemas are standalone. Never resolve remote references.
        def references(value):
            if isinstance(value, dict):
                return '$ref' in value or '$dynamicRef' in value or any(references(v) for v in value.values())
            return isinstance(value, list) and any(references(v) for v in value)
        if references(schema):
            raise ValueError('Composition schemas must be self-contained')
        try:
            Draft202012Validator.check_schema(schema)
        except SchemaError as error:
            raise ValueError('Invalid local component schema') from error
        validators[kind] = Draft202012Validator(schema)

    def validate(kind, data):
        try:
            validators[kind].validate(data)
        except ValidationError as error:
            raise ValueError('Invalid ' + kind + ': ' + error.message) from error

    board = load_board(root, board_name)
    # Include board provenance, never load local laboratory configuration.
    read(f'boards/{board_name}/profile.json', f'boards/{board_name}')
    expected = f'boards/{board_name}/components.json'
    if board.get('composition') != expected:
        raise ValueError('Unexpected board composition path')
    composition = read(expected, f'boards/{board_name}')
    validate('composition', composition)
    if composition['board'] != board_name:
        raise ValueError('Composition belongs to another board')
    read(composition['evidence_index'], 'docs/baselines')  # Public hashes only, never private logs.
    catalog = read(composition['catalog'], 'components')
    validate('catalog', catalog)
    definitions = {}
    for path in catalog['components']:
        definition = read(path, 'components')
        validate('component', definition)
        identity = definition['id']
        if identity in definitions:
            raise ValueError('Duplicate component identity: ' + identity)
        for candidate in definition['upstream']:
            if candidate['origin'] not in catalog['origins']:
                raise ValueError('Unknown component provenance')
            for source in candidate['paths']:
                _relative(source)  # A path in the upstream tree, not a local read.
        for source in definition['legacy_sources'] + definition.get('reusable_sources', []):
            relative = _relative(source)
            if source in definition.get('reusable_sources', []) and not relative.is_relative_to('kernel/components'):
                raise ValueError('Reusable chip code must be independent of board directories')
            if relative.parts[0] not in ('kernel', 'patches'):
                raise ValueError('Legacy source is not reviewed kernel source')
            hash_source(source, relative.parts[0], source_root=(
                shared if source in definition.get('reusable_sources', []) else None))
        definitions[identity] = definition

    instances = {}
    for instance in composition['instances']:
        name = instance['id']
        if name in instances or instance['component'] not in definitions:
            raise ValueError('Duplicate instance or unknown component: ' + name)
        values = {}
        for source in instance.get('board_sources', []):
            hash_source(source, 'kernel/devices/'+board['device'])
        for field in instance['board_fields']:
            if field.split('.')[0] not in ('hardware', 'charger_auto_bind'):
                raise ValueError('Board wiring must not reference private/recovery settings')
            value = board
            for key in field.split('.'):
                if not isinstance(value, dict) or key not in value:
                    raise ValueError('Missing board wiring field: ' + field)
                value = value[key]
            values[field] = value
        instances[name] = dict(instance, definition=definitions[instance['component']], board_values=values)

    visited, active, order = set(), set(), []

    def visit(name):
        if name not in instances:
            raise ValueError('Missing component dependency: ' + name)
        if name in active:
            raise ValueError('Cyclic component dependency')
        if name in visited:
            return
        active.add(name)
        for dependency in instances[name]['depends_on']:
            visit(dependency)
        active.remove(name)
        visited.add(name)
        order.append(name)

    for name in instances:
        visit(name)
    return {'schema': 1, 'board': board_name, 'deployment': 'inventory-only',
            'dependency_order': order, 'instances': instances,
            'unresolved': composition['unresolved'], 'origins': catalog['origins'],
            'evidence_index': composition['evidence_index'],
            'input_sha256': inputs,
            'fingerprint': hashlib.sha256(json.dumps(inputs, sort_keys=True).encode()).hexdigest(),
            'note': 'Dependency order is descriptive, NOT a probe/build/flash authorization'}
