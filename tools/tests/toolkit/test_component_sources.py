# SPDX-License-Identifier: MIT
"""Shared source lookup without board inputs or a neighboring checkout."""
import os
from pathlib import Path
import tempfile
import unittest

from portkit.composition import component_source


class ComponentSourceTests(unittest.TestCase):
    def test_explicit_external_root_selects_exact_bytes_independently_of_cwd(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            source = root / 'kernel/components/chip/header.h'
            source.parent.mkdir(parents=True)
            source.write_bytes(b'/* synthetic component */\n')
            previous = Path.cwd()
            try:
                os.chdir(root.parent)
                result = component_source(root, 'kernel/components/chip/header.h')
                self.assertEqual(result, source)
                self.assertEqual(result.read_bytes(), b'/* synthetic component */\n')
            finally:
                os.chdir(previous)

    def test_missing_or_invalid_input_never_falls_back(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            for selected in (None, '', '.', 'relative', root):
                with self.subTest(root=str(selected)), self.assertRaises(ValueError):
                    component_source(selected, 'kernel/components/missing.h')
            for name in ('../escape', '/kernel/components/input.h', 'C:/input.h',
                         'kernel/components/../input.h', 'kernel/devices/fixture/input.h',
                         'kernel/components\\input.h'):
                with self.subTest(name=name), self.assertRaises(ValueError):
                    component_source(root, name)

    @unittest.skipUnless(os.name == 'posix', 'symlink fixture requires POSIX')
    def test_shared_parent_symlink_is_refused_even_inside_the_same_root(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            real = root / 'kernel/components/real'
            real.mkdir(parents=True)
            (real / 'input.h').write_text('/* synthetic */')
            (real.parent / 'alias').symlink_to(real, target_is_directory=True)
            with self.assertRaises(ValueError):
                component_source(root, 'kernel/components/alias/input.h')
