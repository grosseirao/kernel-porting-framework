# SPDX-License-Identifier: MIT
"""DT commands outside the device checkout; libfdt builds synthetic fixtures."""
import contextlib
import importlib.util
import io
import json
import os
from pathlib import Path
import shutil
import struct
import tempfile
import unittest
from unittest.mock import patch

from portkit.cli import boot_snapshot, dt_contract, dt_compare


def tree_bytes(address=16):
    import libfdt
    tree = libfdt.FdtSw()
    tree.finish_reservemap()
    tree.begin_node('')
    tree.property_u32('#address-cells', 1)
    tree.property_u32('#size-cells', 1)
    tree.property_string('serial-number', 'PRIVATE_FIXTURE')
    tree.begin_node('unit@10')
    tree.property_string('compatible', 'fixture,node')
    tree.property('reg', struct.pack('>II', address, 32))
    tree.end_node()
    tree.begin_node('chosen')
    tree.property_string('bootargs', 'PRIVATE_FIXTURE')
    tree.end_node()
    tree.end_node()
    result = tree.as_fdt()
    result.pack()
    return bytes(result.as_bytearray())


class DtCliRootTests(unittest.TestCase):
    def test_no_implicit_workspace_or_input_reads(self):
        cases = [(boot_snapshot, ['--board', 'fixture', '--fdt', 'input.dtb', '--iomem', 'iomem.txt',
                                  '--kernel-release', '6.18-fixture', '--output', 'boot.json']),
                 (dt_contract, ['--board', 'fixture', '--contract', 'node', '--fdt', 'input.dtb',
                                '--output', 'contract.json']),
                 (dt_compare, ['--reference', 'input.dtb', '--candidate', 'input.dtb', '--output', 'compare'])]
        with tempfile.TemporaryDirectory() as folder:
            for module, args in cases:
                for prefix in ([], ['--workspace', 'relative'], ['--workspace', str(Path(folder) / 'missing')]):
                    with self.subTest(module=module.__name__, root=prefix), \
                         patch.object(module, 'read_exact_capture') as read, \
                         contextlib.redirect_stderr(io.StringIO()), self.assertRaises(SystemExit):
                        module.main(prefix + args)
                    read.assert_not_called()
            self.assertEqual(list(Path(folder).iterdir()), [])


@unittest.skipUnless(importlib.util.find_spec('libfdt') and shutil.which('dtc'), 'libfdt and DTC required')
class DtCliIntegrationTests(unittest.TestCase):
    def setUp(self):
        self.folder = tempfile.TemporaryDirectory(prefix='dt capture workspace ')
        self.addCleanup(self.folder.cleanup)
        self.root = Path(self.folder.name)
        profile = self.root / 'boards/fixture/profile.json'
        profile.parent.mkdir(parents=True)
        profile.write_text(json.dumps({
            'schema': 1, 'id': 'fixture', 'kernel': {'default_profile': 'unused.json'},
            'diagnostics': {
                'boot_snapshot': dict(node_paths=['/', '/unit@10'], node_prefixes=[]),
                'dt_contracts': {'node': dict(compatible='fixture,node', parent='/',
                    address_cells=1, size_cells=1, properties={'reg': '0000001000000020'},
                    require_available=True)},
            }}), encoding='utf-8')
        self.data = tree_bytes()
        (self.root / 'input.dtb').write_bytes(self.data)
        (self.root / 'iomem.txt').write_text('00001000-00001fff : System RAM\n')
        self.common = ['--workspace', str(self.root)]
        self.cases = [
            (boot_snapshot, ['--board', 'fixture', '--fdt', 'input.dtb', '--iomem', 'iomem.txt',
                             '--kernel-release', '6.18-fixture', '--output', 'boot.json'], 'boot.json'),
            (dt_contract, ['--board', 'fixture', '--contract', 'node', '--fdt', 'input.dtb',
                           '--output', 'contract.json'], 'contract.json'),
            (dt_compare, ['--reference', 'input.dtb', '--candidate', 'input.dtb', '--output', 'compare'], 'compare'),
        ]

    def outputs(self, name):
        output = self.root / name
        return {p.name: p.read_bytes() for p in output.iterdir()} if output.is_dir() else {name: output.read_bytes()}

    def test_external_workspace_outputs_and_create_only_from_foreign_cwd(self):
        with tempfile.TemporaryDirectory() as other:
            previous = Path.cwd()
            try:
                os.chdir(other)
                for module, args, name in self.cases:
                    with self.subTest(command=name):
                        self.assertEqual(module.main(self.common + args), 0)
                        saved = self.outputs(name)
                        report = json.loads(saved['comparison.json' if name == 'compare' else name])
                        self.assertIs(report['boot_authorized'], False)
                        self.assertNotIn('PRIVATE_FIXTURE', json.dumps(report))
                        with patch.object(module, 'read_exact_capture') as read, \
                             contextlib.redirect_stderr(io.StringIO()), self.assertRaises(SystemExit):
                            module.main(self.common + args)
                        read.assert_not_called()
                        self.assertEqual(self.outputs(name), saved)
                        self.assertFalse((Path(other) / name).exists())
            finally:
                os.chdir(previous)
        self.assertEqual((self.root / 'input.dtb').read_bytes(), self.data)

    def test_mismatch_is_not_equivalence_or_static_contract_success(self):
        (self.root / 'changed.dtb').write_bytes(tree_bytes(address=17))
        self.assertEqual(dt_compare.main(self.common + ['--reference', 'input.dtb', '--candidate',
                                                       'changed.dtb', '--output', 'changed']), 2)
        report = json.loads((self.root / 'changed/comparison.json').read_text())
        self.assertFalse(report['canonical_equal'])
        self.assertFalse(report['bindings_validated'])
        self.assertTrue((self.root / 'changed/comparison.diff').read_bytes())
        args = self.cases[1][1].copy()
        args[args.index('--fdt') + 1] = 'changed.dtb'
        with contextlib.redirect_stderr(io.StringIO()), self.assertRaises(SystemExit):
            dt_contract.main(self.common + args)
        self.assertFalse((self.root / 'contract.json').exists())

    def test_bad_fdt_publishes_no_partial_files(self):
        (self.root / 'input.dtb').write_bytes(b'bad FDT')
        for module, args, name in self.cases:
            with self.subTest(command=name), contextlib.redirect_stderr(io.StringIO()), self.assertRaises(SystemExit):
                module.main(self.common + args)
            self.assertFalse((self.root / name).exists())
