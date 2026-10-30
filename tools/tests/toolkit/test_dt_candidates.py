# SPDX-License-Identifier: MIT
"""Candidate selection extracted from a port, without board paths or IDs."""
import importlib.util
import shutil
import unittest

from portkit.core.devicetree import compare_dtb_candidates


@unittest.skipUnless(importlib.util.find_spec('libfdt') and shutil.which('dtc'), 'libfdt and DTC required')
class DtCandidateTests(unittest.TestCase):
    def setUp(self):
        import libfdt
        def blob(value):
            tree = libfdt.FdtSw()
            tree.finish_reservemap()
            tree.begin_node('')
            tree.property_string('fixture', value)
            tree.end_node()
            result = tree.as_fdt()
            result.pack()
            return bytes(result.as_bytearray())
        self.reference = blob('reference')
        self.other = blob('different')
        self.reads = []
        self.blobs = {'renamed.dtb': self.reference, 'other.dtb': self.other}

    def read(self, name):
        self.reads.append(name)
        return self.blobs[name]

    def test_unique_match_avoids_missing_fallback_and_preserves_read_order(self):
        selected, result, actual, built, delta = compare_dtb_candidates(
            self.reference, ['other.dtb', 'renamed.dtb'], read_candidate=self.read,
            fallback='missing.dtb', candidate_label='compiled')
        self.assertEqual(selected, 'renamed.dtb')
        self.assertTrue(result['canonical_equal'])
        self.assertEqual((actual, delta), (built, ''))
        self.assertEqual(self.reads, ['other.dtb', 'renamed.dtb', 'renamed.dtb'])

    def test_no_match_uses_explicit_fallback_without_claiming_equivalence(self):
        selected, result, _, _, delta = compare_dtb_candidates(
            self.reference, ['other.dtb'], read_candidate=self.read,
            fallback='other.dtb', candidate_label='compiled')
        self.assertEqual(selected, 'other.dtb')
        self.assertFalse(result['canonical_equal'])
        self.assertTrue(delta.startswith('--- reference\n+++ compiled\n'))
        self.assertEqual(self.reads, ['other.dtb', 'other.dtb'])

    def test_ambiguity_refused_without_selecting_or_reading_fallback(self):
        self.blobs['duplicate.dtb'] = self.reference
        with self.assertRaisesRegex(ValueError, 'More than one canonical DT candidate matches'):
            compare_dtb_candidates(self.reference, ['renamed.dtb', 'duplicate.dtb'],
                                   read_candidate=self.read, fallback='missing.dtb')
        self.assertEqual(self.reads, ['renamed.dtb', 'duplicate.dtb'])

    def test_all_candidates_are_validated_even_after_a_match(self):
        self.blobs['bad.dtb'] = b'invalid FDT'
        with self.assertRaises(ValueError):
            compare_dtb_candidates(self.reference, ['renamed.dtb', 'bad.dtb'],
                                   read_candidate=self.read, fallback='missing.dtb')
        self.assertEqual(self.reads, ['renamed.dtb', 'bad.dtb'])
