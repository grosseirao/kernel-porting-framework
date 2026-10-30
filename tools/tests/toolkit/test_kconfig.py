# SPDX-License-Identifier: MIT
"""Saved-config contracts, independent from board/workspace CLI adapters."""
import unittest

from portkit.core.kconfig import config_values, mismatched_symbols, verify_required_config


class KconfigTests(unittest.TestCase):
    def test_raw_values_duplicates_disabled_and_string_escapes(self):
        text = ('# generated header\nCONFIG_CPU=y\nCONFIG_CPU=m\n'
                '# CONFIG_UNUSED is not set\nCONFIG_PATH="a\\b=hello"\n'
                'CONFIG_EMPTY=""\nCONFIG_NUMBER=0x1000\nCONFIG_OFF=n\n')
        self.assertEqual(config_values(text), {
            'CONFIG_CPU': 'm', 'CONFIG_UNUSED': 'n', 'CONFIG_PATH': '"a\\b=hello"',
            'CONFIG_EMPTY': '""', 'CONFIG_NUMBER': '0x1000', 'CONFIG_OFF': 'n'})
        self.assertEqual(config_values('CONFIG_A=y\n# CONFIG_A is not set\n'), {'CONFIG_A': 'n'})

    def test_missing_n_only_is_equivalent_and_first_failure_is_preserved(self):
        self.assertEqual(mismatched_symbols({}, {'CONFIG_DISABLED': 'n'}), [])
        for value in ('y', 'm', '"n"', '""', '0', '0x1000'):
            with self.subTest(value=value):
                required = {'CONFIG_REQUIRED': value}
                self.assertEqual(mismatched_symbols({}, required), ['CONFIG_REQUIRED'])
                with self.assertRaisesRegex(ValueError, 'Kconfig dropped/changed required option'):
                    verify_required_config({}, required)
        required = {'CONFIG_SECOND': 'm', 'CONFIG_FIRST': 'y'}
        self.assertEqual(mismatched_symbols({'CONFIG_FIRST': 'm'}, required),
                         ['CONFIG_SECOND', 'CONFIG_FIRST'])
        with self.assertRaisesRegex(ValueError, 'CONFIG_SECOND=m$'):
            verify_required_config({}, required)
        verify_required_config({'CONFIG_FIRST': 'y', 'CONFIG_SECOND': 'm'}, required)
