# SPDX-License-Identifier: MIT
"""Console/session CLIs use explicit capture layouts and create-only outputs."""
import contextlib
import io
import json
import os
from pathlib import Path
import struct
import tempfile
import unittest
from unittest.mock import patch

from portkit.cli import ramoops, session_logs
from portkit.core.ramoops import FORMAT


class BinaryLogCliTests(unittest.TestCase):
    def setUp(self):
        self.folder = tempfile.TemporaryDirectory(prefix='binary workspace ')
        self.addCleanup(self.folder.cleanup)
        self.root = Path(self.folder.name)
        self.zone = struct.pack('<III', 0x43474245, 3, 3) + b'abc' + bytes(17)
        self.memory = bytes(16) + self.zone + bytes(16)
        profile = self.root / 'boards/fixture/profile.json'
        profile.parent.mkdir(parents=True)
        profile.write_text(json.dumps({
            'schema': 1, 'id': 'fixture', 'kernel': {'default_profile': 'unused.json'},
            'diagnostics': {
                'ramoops_console': dict(format=FORMAT, zone_size=32, signature=0x43474245, ecc=0),
                'session_logs': dict(captures=dict(memory=64, trace=16),
                    size_variants=dict(trace=[16, 32]), console=dict(capture='memory', offset=16),
                    unordered_text=['trace']),
            }}), encoding='utf-8')
        (self.root / 'zone.bin').write_bytes(self.zone)
        (self.root / 'capture-memory.bin').write_bytes(self.memory)
        (self.root / 'capture-trace.bin').write_bytes(b'synthetic trace'.ljust(16, b'\0'))
        self.common = ['--workspace', str(self.root), '--board', 'fixture']
        self.cases = [(ramoops, ['--console-dump', 'zone.bin', '--output', 'console'], 'console'),
                      (session_logs, ['capture', 'session'], 'session')]

    def test_external_profile_and_inputs_from_foreign_cwd_preserve_all_outputs(self):
        with tempfile.TemporaryDirectory() as other:
            previous = Path.cwd()
            try:
                os.chdir(other)
                for module, args, name in self.cases:
                    with self.subTest(command=name):
                        self.assertEqual(module.main(self.common + args), 0)
                        output = self.root / name
                        before = {p.name: p.read_bytes() for p in output.iterdir()}
                        self.assertEqual(before['console.log'], b'abc')
                        report = json.loads(before['report.json' if name == 'console' else 'decode-report.json'])
                        self.assertIs(report['boot_authorized'], False)
                        self.assertIs(report['phone_access'], False)
                        with patch.object(module, 'load_board') as load, \
                             contextlib.redirect_stderr(io.StringIO()), self.assertRaises(SystemExit):
                            module.main(self.common + args)
                        load.assert_not_called()
                        self.assertEqual({p.name: p.read_bytes() for p in output.iterdir()}, before)
                        self.assertFalse((Path(other) / name).exists())
            finally:
                os.chdir(previous)
        self.assertEqual((self.root / 'zone.bin').read_bytes(), self.zone)
        self.assertEqual((self.root / 'capture-memory.bin').read_bytes(), self.memory)

    def test_missing_workspace_invalid_size_and_override_never_publish(self):
        for module, args, name in self.cases:
            for prefix in ([], ['--workspace', 'relative'], ['--workspace', str(self.root / 'missing')]):
                with self.subTest(command=name, prefix=prefix), patch.object(module, 'load_board') as load, \
                     contextlib.redirect_stderr(io.StringIO()), self.assertRaises(SystemExit):
                    module.main(prefix + ['--board', 'fixture'] + args)
                load.assert_not_called()
        (self.root / 'zone.bin').write_bytes(self.zone[:-1])
        with contextlib.redirect_stderr(io.StringIO()), self.assertRaises(SystemExit):
            ramoops.main(self.common + self.cases[0][1])
        self.assertFalse((self.root / 'console').exists())
        for extra in (['--capture-size', 'trace=24'], ['--capture-size', 'unknown=16'],
                      ['--capture-size', 'trace=16', '--capture-size', 'trace=16']):
            with contextlib.redirect_stderr(io.StringIO()), self.assertRaises(SystemExit):
                session_logs.main(self.common + ['capture', 'session'] + extra)
            self.assertFalse((self.root / 'session').exists())
        (self.root / 'capture-trace.bin').write_bytes(b'synthetic trace'.ljust(32, b'\0'))
        self.assertEqual(session_logs.main(self.common + ['capture', 'session', '--capture-size', 'trace=32']), 0)
        report = json.loads((self.root / 'session/decode-report.json').read_text())
        self.assertEqual(report['size_overrides'], {'trace': 32})
