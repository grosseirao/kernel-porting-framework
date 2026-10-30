# SPDX-License-Identifier: MIT
"""Text-analysis commands consume external policies, never execute diagnostics."""
import contextlib
import io
import json
import os
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

from portkit.cli import stability, smp, register_snapshot


class TextLogCliTests(unittest.TestCase):
    def setUp(self):
        self.folder = tempfile.TemporaryDirectory(prefix='text workspace ')
        self.addCleanup(self.folder.cleanup)
        self.root = Path(self.folder.name)
        profile = self.root / 'boards' / 'fixture' / 'profile.json'
        profile.parent.mkdir(parents=True)
        profile.write_text(json.dumps({
            'schema': 1, 'id': 'fixture', 'kernel': {'default_profile': 'unused.json'},
            'diagnostics': {
                'stability': dict(prefix='FIX-STABILITY', cpus=[2], total_seconds=9,
                                  watchdog_min=3, watchdog_max=4),
                'smp': dict(prefix='FIX-CPU', online_prefix='FIX-BOOT', max_cpus=8,
                            arm_cpu_up_timeout_inference=False),
                'register_snapshots': {'fixture': dict(prefix='FIX-REG: ',
                    required_markers=['FIX: marker'], fields=[[1, 16, 255]], sample_count=1)},
            }}), encoding='utf-8')
        self.cases = [
            (stability, [], 'stability', 'FIX-STABILITY: ', [
                'watchdog_timeout value=3', 'start_seconds value=9', 'phase value=0',
                'phase value=1', 'worker_pass_cpu value=2', 'phase value=2',
                'pass_seconds value=9', 'stop_feeding_wait_reset value=3']),
            (smp, [], 'smp', '', ['FIX-BOOT: cpus online 0,2']),
            (register_snapshot, ['--contract', 'fixture'], 'snapshot', '', [
                'FIX: marker', 'FIX-REG: begin version=1 read_only=1',
                'FIX-REG: sample=0 bank=1 offset=0x010 value=0x00000010',
                'FIX-REG: end samples=1 fields=1 stable=1 read_only=1']),
        ]

    def args(self, extra, output):
        return ['--workspace', str(self.root), '--board', 'fixture', '--log', 'capture.log',
                '--output', output, *extra]

    def test_external_workspace_from_foreign_cwd_and_filtered_create_only_output(self):
        with tempfile.TemporaryDirectory() as other:
            previous = Path.cwd()
            try:
                os.chdir(other)
                for module, extra, key, prefix, lines in self.cases:
                    with self.subTest(command=key):
                        data = ('private=SECRET\n' + '\n'.join(prefix + line for line in lines)).encode()
                        source = self.root / 'capture.log'
                        source.write_bytes(data)
                        output = self.root / (key + '.json')
                        args = self.args(extra, output.name)
                        self.assertEqual(module.main(args), 0)
                        before = output.read_bytes()
                        report = json.loads(before)
                        self.assertIn(key, report)
                        self.assertIs(report['boot_authorized'], False)
                        self.assertNotIn('SECRET', before.decode())
                        self.assertEqual(source.read_bytes(), data)
                        self.assertFalse((Path(other) / output.name).exists())
                        with contextlib.redirect_stderr(io.StringIO()), self.assertRaises(SystemExit):
                            module.main(args)
                        self.assertEqual(output.read_bytes(), before)
            finally:
                os.chdir(previous)

    def test_missing_or_relative_workspace_fails_before_reading_profile(self):
        for module, extra, key, _, _ in self.cases:
            args = self.args(extra, key + '.json')[2:]
            for prefix in ([], ['--workspace', 'relative'], ['--workspace', str(self.root / 'missing')]):
                with self.subTest(command=key, prefix=prefix), \
                     patch.object(module, 'load_board') as load, \
                     contextlib.redirect_stderr(io.StringIO()), self.assertRaises(SystemExit):
                    module.main(prefix + args)
                load.assert_not_called()
                self.assertFalse((self.root / (key + '.json')).exists())

    def test_invalid_capture_publishes_nothing_and_incomplete_stability_returns_two(self):
        for module, extra, key, _, _ in self.cases:
            for raw in (b'bad\0log', b'\xff'):
                (self.root / 'capture.log').write_bytes(raw)
                with self.subTest(command=key, raw=raw), contextlib.redirect_stderr(io.StringIO()), \
                     self.assertRaises(SystemExit):
                    module.main(self.args(extra, key + '.json'))
                self.assertFalse((self.root / (key + '.json')).exists())
        (self.root / 'capture.log').write_bytes(b'')
        self.assertEqual(stability.main(self.args([], 'incomplete.json')), 2)
        self.assertFalse(json.loads((self.root / 'incomplete.json').read_text())['stability']
                         ['complete_bounded_test_reported_pass'])
