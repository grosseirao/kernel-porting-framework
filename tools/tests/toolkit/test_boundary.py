# SPDX-License-Identifier: MIT
"""Library boundary checks, runnable with only the package and these tests."""
import ast
import importlib
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

import portkit
from portkit.core.evidence import write_evidence
from portkit.core.manifests import file_manifest
from portkit.profiles import development_root, load_board
from portkit.profiles import _load_lab_data, cycle_defaults, load_lab
from portkit.composition import load_composition


class ToolkitBoundaryTests(unittest.TestCase):
    def test_runtime_never_discovers_configuration_beside_the_package(self):
        board = {'id': 'fixture', 'lab_configuration': '.env'}
        with patch('portkit.profiles._load_lab_data') as read:
            with self.assertRaisesRegex(ValueError, 'explicit absolute workspace'):
                development_root(board)
            read.assert_not_called()
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            runtime = root / 'runtime'
            # Explicit runtime needs neither a workspace nor a config file.
            self.assertEqual(development_root(board, runtime), runtime)
            (root / '.env').write_text('KPF_FIXTURE_RUNTIME_ROOT=' + json.dumps(str(runtime)) + '\n')
            self.assertEqual(development_root(board, project=root), runtime)

    def test_workspace_apis_reject_cwd_relative_roots_before_input_reads(self):
        board = {'id': 'fixture', 'lab_configuration': '.env'}
        calls = (lambda root: load_board(root, 'fixture'),
                 lambda root: development_root(board, project=root),
                 lambda root: _load_lab_data(root, board),
                 lambda root: load_lab(root, board),
                 lambda root: cycle_defaults(root, board),
                 lambda root: load_composition(root, 'fixture'))
        for value in (None, '', '.', 'relative/workspace', Path('relative'), 'bad\nroot'):
            for call in calls:
                with self.subTest(root=str(value), operation=call), \
                     patch.object(Path, 'open', side_effect=AssertionError('implicit input read')), \
                     self.assertRaisesRegex(ValueError, 'explicit absolute workspace'):
                    call(value)

    def test_library_has_no_static_device_or_cli_dependency(self):
        package = Path(portkit.__file__).resolve().parent
        for path in package.rglob('*.py'):
            with self.subTest(module=path.relative_to(package)):
                tree = ast.parse(path.read_text(encoding='utf-8'))
                for node in ast.walk(tree):
                    if isinstance(node, ast.Import):
                        names = [alias.name for alias in node.names]
                    elif isinstance(node, ast.ImportFrom) and not node.level:
                        names = [node.module or '']
                    else:
                        names = []
                    for name in names:
                        self.assertNotIn(name.split('.')[0], {'tools', 'boards', 'installer', 'kernel'})
                    if isinstance(node, ast.Constant) and isinstance(node.value, str):
                        self.assertNotIn('k40s', node.value.lower())

    def test_all_library_modules_import_without_workspace_reads(self):
        package = Path(portkit.__file__).resolve().parent
        names = []
        for path in package.rglob('*.py'):
            parts = list(path.relative_to(package).with_suffix('').parts)
            if parts[-1] == '__init__':
                parts.pop()
            names.append('.'.join(['portkit', *parts]))
        with patch.object(Path, 'open', side_effect=AssertionError('implicit workspace read')):
            for name in sorted(names):
                importlib.import_module(name)

    def test_external_synthetic_workspace_uses_explicit_inputs_only(self):
        with tempfile.TemporaryDirectory(prefix='device workspace ') as folder:
            root = Path(folder)
            profile = root / 'boards' / 'fixture' / 'profile.json'
            profile.parent.mkdir(parents=True)
            profile.write_text(json.dumps({
                'schema': 1, 'id': 'fixture', 'kernel': {'default_profile': 'kernel/fixture.json'},
                'lab_configuration': '.env',
            }), encoding='utf-8')
            board = load_board(root, 'fixture')
            # An explicit runtime must not require any host configuration file.
            self.assertEqual(development_root(board, root / 'runtime', project=root), root / 'runtime')
            (root / 'input.txt').write_bytes(b'synthetic payload\n')
            manifest = file_manifest(root, ['input.txt'])
            output = root / 'result.json'
            write_evidence(output, manifest)
            self.assertEqual(json.loads(output.read_text()), manifest)
            original = output.read_bytes()
            with self.assertRaises(FileExistsError):
                write_evidence(output, {'changed': True})
            self.assertEqual(output.read_bytes(), original)
            with self.assertRaises(ValueError):
                file_manifest(root, ['../outside'])
            self.assertFalse((root / '.env').exists())
