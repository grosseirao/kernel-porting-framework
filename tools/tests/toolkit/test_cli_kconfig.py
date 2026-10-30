# SPDX-License-Identifier: MIT
"""Packaged Kconfig command with synthetic, explicit external workspaces."""
import contextlib
import io
import json
import os
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

from portkit.cli.kconfig import main


class KconfigCliTests(unittest.TestCase):
    def test_ordered_fragments_two_architectures_and_no_private_values(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            config, first, last = root / '.config', root / 'base.config', root / 'extra.config'
            first.write_text('CONFIG_MODULES=y\nCONFIG_PREEMPT=n\n')
            for architecture in ('ARM64', 'RISCV'):
                text = f'CONFIG_{architecture}=y\nCONFIG_PREEMPT=y\nCONFIG_MODULES=y\nCONFIG_CMDLINE="SECRET"\n'
                config.write_text(text)
                last.write_text(f'CONFIG_{architecture}=y\nCONFIG_PREEMPT=y\nCONFIG_CMDLINE="SECRET"\n')
                output = root / f'{architecture}.json'
                args = ['--workspace', str(root), '--config', str(config), '--fragment', str(first),
                        '--fragment', str(last), '--output', str(output)]
                self.assertEqual(main(args), 0)
                report = json.loads(output.read_text())
                self.assertTrue(report['requirements_satisfied'])
                self.assertFalse(report['values_exported'])
                self.assertFalse(report['dependencies_resolved'])
                self.assertFalse(report['phone_access'])
                self.assertFalse(report['boot_authorized'])
                self.assertNotIn('SECRET', output.read_text())
                self.assertEqual(report['required_symbols'],
                                 ['CONFIG_MODULES', 'CONFIG_PREEMPT', f'CONFIG_{architecture}', 'CONFIG_CMDLINE'])
                self.assertEqual(config.read_text(), text)
                saved = output.read_bytes()
                with contextlib.redirect_stderr(io.StringIO()), self.assertRaises(SystemExit):
                    main(args)
                self.assertEqual(output.read_bytes(), saved)
            args = ['--workspace', str(root), '--config', str(config), '--fragment', str(last),
                    '--fragment', str(first), '--output', str(root / 'reverse.json')]
            self.assertEqual(main(args), 2)
            self.assertEqual(json.loads((root / 'reverse.json').read_text())['mismatched_symbols'],
                             ['CONFIG_PREEMPT'])

    def test_mismatch_has_evidence_invalid_input_does_not(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            config, fragment, output = root / '.config', root / 'required', root / 'report.json'
            config.write_text('CONFIG_CMDLINE="PRIVATE-ACTUAL"\nCONFIG_MODULES=m\n')
            fragment.write_text('CONFIG_CMDLINE="PRIVATE-REQUIRED"\nCONFIG_MODULES=y\n')
            args = ['--workspace', str(root), '--config', str(config), '--fragment', str(fragment),
                    '--output', str(output)]
            self.assertEqual(main(args), 2)
            report = json.loads(output.read_text())
            self.assertEqual(report['mismatched_symbols'], ['CONFIG_CMDLINE', 'CONFIG_MODULES'])
            self.assertNotIn('PRIVATE', output.read_text())
            for data in (b'\0', b'\xff', b'# header only\n'):
                fragment.write_bytes(data)
                invalid = root / 'invalid.json'
                with contextlib.redirect_stderr(io.StringIO()), self.assertRaises(SystemExit):
                    main(args[:-1] + [str(invalid)])
                self.assertFalse(invalid.exists())

    def test_workspace_is_required_validated_before_reads_and_independent_from_cwd(self):
        with tempfile.TemporaryDirectory(prefix='external workspace ') as folder, tempfile.TemporaryDirectory() as other:
            root = Path(folder)
            (root / 'actual.config').write_text('CONFIG_MODULES=y\n')
            (root / 'required.config').write_text('CONFIG_MODULES=y\n')
            args = ['--config', 'actual.config', '--fragment', 'required.config', '--output', 'result.json']
            previous = Path.cwd()
            try:
                os.chdir(other)
                for prefix in ([], ['--workspace', 'relative'], ['--workspace', str(root / 'missing')],
                               ['--workspace', str(root / 'actual.config')], ['--workspace', str(root) + '\n']):
                    with patch('portkit.cli.kconfig.read_text_capture') as read, \
                         contextlib.redirect_stderr(io.StringIO()), self.assertRaises(SystemExit) as stopped:
                        main(prefix + args)
                    self.assertEqual(stopped.exception.code, 2)
                    read.assert_not_called()
                    self.assertFalse((root / 'result.json').exists())
                self.assertEqual(main(['--workspace', str(root)] + args), 0)
                self.assertFalse((Path(other) / 'result.json').exists())
            finally:
                os.chdir(previous)
            self.assertTrue(json.loads((root / 'result.json').read_text())['requirements_satisfied'])
