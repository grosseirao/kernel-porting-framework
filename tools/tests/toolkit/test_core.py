# SPDX-License-Identifier: MIT
"""Existing host contracts, separated from board/recovery integration tests."""
import hashlib
from pathlib import Path
import subprocess
import tempfile
import unittest
from unittest.mock import patch

from portkit.core.hashes import sha256, verify_sha256
from portkit.core.manifests import file_manifest
from portkit.core.evidence import write_evidence
from portkit.core.processes import run_checked, run_bounded
from portkit.core.results import State, StepResult, TestClass


class PortkitTests(unittest.TestCase):
    def test_streamed_hash_equivalence_and_rejection(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / 'input'
            data = b'original\0' * 300000
            path.write_bytes(data)
            expected = hashlib.sha256(data).hexdigest()
            self.assertEqual(sha256(path), expected)
            self.assertEqual(verify_sha256(path, expected), expected)
            for value in ('0' * 64, 'x', expected.upper(), None):
                with self.assertRaises(ValueError):
                    verify_sha256(path, value)

    def test_manifest_order_and_escape_rejected(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            (root / 'a').write_bytes(b'a')
            (root / 'b').write_bytes(b'b')
            self.assertEqual(file_manifest(root, ['b', 'a']), file_manifest(root, ['a', 'b']))
            for names in (['../escape'], ['/etc/passwd'], ['missing'], ['a', './a']):
                with self.assertRaises(ValueError):
                    file_manifest(root, names)

    def test_evidence_never_overwrites_and_no_temp_leaks(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / 'record.json'
            write_evidence(path, {'ok': True})
            original = path.read_bytes()
            with self.assertRaises(FileExistsError):
                write_evidence(path, {'ok': False})
            self.assertEqual(path.read_bytes(), original)
            self.assertEqual(list(Path(folder).iterdir()), [path])

    def test_subprocess_preserves_argv_kwargs_and_has_no_retry(self):
        with tempfile.TemporaryDirectory() as folder:
            source, work = Path(folder) / 'source', Path(folder) / 'work'
            with patch('portkit.core.processes.subprocess.run') as run:
                run_checked(['make', source], cwd=work, stdout=subprocess.DEVNULL)
                run.assert_called_once_with(['make', str(source)], check=True,
                                            cwd=work, stdout=subprocess.DEVNULL)
        for command, kwargs in [('sh -c x', {}), ([], {}), (['sh'], {'shell': True}),
                                (['tool'], {'check': False})]:
            with self.assertRaises(ValueError):
                run_checked(command, **kwargs)
        with patch('portkit.core.processes.subprocess.run', side_effect=OSError('stop')) as run:
            with self.assertRaises(OSError):
                run_bounded(['fake'], timeout=1)
            self.assertEqual(run.call_count, 1)

    def test_result_vocabulary_does_not_imply_recovery(self):
        result = StepResult('test', State.PASSED, TestClass.OFFLINE)
        self.assertEqual(result.classification.value, 'offline')
        self.assertIsNone(result.evidence_path)
