# SPDX-License-Identifier: MIT
"""Board-owned SSH contract with synthetic endpoints; never opens a connection."""
import copy
import json
from pathlib import Path
import tempfile
import unittest

from portkit.profiles import load_lab


class SshPolicyTests(unittest.TestCase):
    def fixture(self, root, identity):
        contract = dict(normal_ssh_user='device', normal_ssh_port=2200,
                        usb_ssh_host='192.0.2.1', usb_ssh_user='recovery', usb_ssh_port=2201)
        board = dict(id='fixture', lab_configuration='.env', ssh_contract=contract)
        lab = dict(contract, normal_ssh_host='192.0.2.2', ssh_identity_file=str(identity),
                   strict_host_key_checking=True)
        self.write_env(root, lab)
        return board, lab

    def write_env(self, root, lab):
        (root / '.env').write_text('\n'.join(
            'KPF_FIXTURE_' + key.upper() + '=' + json.dumps(value)
            for key, value in lab.items()) + '\n', encoding='utf-8')

    def test_explicit_board_policy_accepts_only_matching_endpoints(self):
        with tempfile.TemporaryDirectory() as folder, tempfile.TemporaryDirectory() as external:
            root = Path(folder)
            board, lab = self.fixture(root, Path(external) / 'identity')
            self.assertEqual(load_lab(root, board), lab)
            for key, value in (('normal_ssh_user', 'other'), ('normal_ssh_port', 2202),
                               ('usb_ssh_host', '192.0.2.3'), ('usb_ssh_user', 'other'),
                               ('usb_ssh_port', 2202)):
                changed = dict(lab, **{key: value})
                self.write_env(root, changed)
                with self.subTest(field=key), self.assertRaisesRegex(ValueError, 'validated SSH contract'):
                    load_lab(root, board)
            self.write_env(root, dict(lab, strict_host_key_checking=False))
            with self.assertRaisesRegex(ValueError, 'strict SSH'):
                load_lab(root, board)

    def test_missing_or_malformed_policy_has_no_implicit_device_defaults(self):
        with tempfile.TemporaryDirectory() as folder, tempfile.TemporaryDirectory() as external:
            root = Path(folder)
            board, _ = self.fixture(root, Path(external) / 'identity')
            policies = [None, {}, [], dict(board['ssh_contract'], unknown='extra')]
            for name, value in (('normal_ssh_port', True), ('normal_ssh_port', 0),
                                ('usb_ssh_port', 65536), ('usb_ssh_port', '2201'),
                                ('normal_ssh_user', '-bad'), ('usb_ssh_user', 'bad\nname'),
                                ('usb_ssh_host', 'host.example'), ('usb_ssh_host', 123)):
                policies.append(dict(board['ssh_contract'], **{name: value}))
            for policy in policies:
                changed = copy.deepcopy(board)
                changed['ssh_contract'] = policy
                with self.subTest(policy=policy), self.assertRaises(ValueError):
                    load_lab(root, changed)
            del board['ssh_contract']
            with self.assertRaisesRegex(ValueError, 'no default policy'):
                load_lab(root, board)
