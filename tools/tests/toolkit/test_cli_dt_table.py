# SPDX-License-Identifier: MIT
"""Packaged DT metadata CLI with explicit roots and synthetic containers."""
import contextlib
import io
import json
import os
from pathlib import Path
import struct
import tempfile
import unittest
from unittest.mock import patch

from portkit.cli.dt_table import main


class DtTableCliTests(unittest.TestCase):
    def test_empty_container_from_foreign_cwd_and_create_only_before_reads(self):
        data = struct.pack('>8I', 0xd7b7ab1e, 32, 32, 32, 0, 32, 4096, 0)
        with tempfile.TemporaryDirectory(prefix='dt workspace ') as folder, tempfile.TemporaryDirectory() as other:
            root = Path(folder)
            source = root / 'table.img'
            source.write_bytes(data)
            args = ['--workspace', str(root), '--input', 'table.img', '--output', 'metadata.json']
            previous = Path.cwd()
            try:
                os.chdir(other)
                self.assertEqual(main(args), 0)
                self.assertFalse((Path(other) / 'metadata.json').exists())
            finally:
                os.chdir(previous)
            output = root / 'metadata.json'
            saved = output.read_bytes()
            report = json.loads(saved)
            self.assertEqual(report['entries'], [])
            self.assertEqual(report['source']['file'], 'table.img')
            for field in ('active_entry_selected', 'raw_properties_exported', 'phone_access', 'boot_authorized'):
                self.assertIs(report[field], False)
            self.assertEqual(source.read_bytes(), data)
            with patch('portkit.cli.dt_table.read_exact_capture') as read, \
                 contextlib.redirect_stderr(io.StringIO()), self.assertRaises(SystemExit) as stopped:
                main(['--workspace', str(root), '--input', 'missing.img', '--output', 'metadata.json'])
            self.assertEqual(stopped.exception.code, 2)
            read.assert_not_called()
            self.assertEqual(output.read_bytes(), saved)

    def test_invalid_workspace_and_container_never_publish_report(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            args = ['--input', str(root / 'table.img'), '--output', str(root / 'metadata.json')]
            for prefix in ([], ['--workspace', 'relative'], ['--workspace', str(root / 'missing')],
                           ['--workspace', str(root) + '\n']):
                with patch('portkit.cli.dt_table.read_exact_capture') as read, \
                     contextlib.redirect_stderr(io.StringIO()), self.assertRaises(SystemExit):
                    main(prefix + args)
                read.assert_not_called()
            for data in (b'', b'bad', struct.pack('>8I', 0xd7b7ab1e, 32, 32, 16, 0, 32, 4096, 0)):
                (root / 'table.img').write_bytes(data)
                with contextlib.redirect_stderr(io.StringIO()), self.assertRaises(SystemExit):
                    main(['--workspace', str(root)] + args)
                self.assertFalse((root / 'metadata.json').exists())
