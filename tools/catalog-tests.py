#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Classify host tests by AST, without importing tests or phone transports."""
import ast
import json
import os
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from portkit.core.evidence import write_evidence
from portkit.core.hashes import sha256


def catalog():
    entries = []
    tests_root = ROOT / 'tools/tests'
    policy = json.loads((ROOT/'manifests/tests.json').read_text())
    toolkit_only = policy.get('catalog_scope') == 'toolkit-only'
    paths = ([] if toolkit_only else list(tests_root.glob('test_*.py'))) + list((tests_root / 'toolkit').glob('test_*.py'))
    for path in sorted(paths):
        code = path.read_text(encoding='utf-8')
        tree = ast.parse(code)
        for cls in tree.body:
            if not isinstance(cls, ast.ClassDef):
                continue
            for method in cls.body:
                if not isinstance(method, ast.FunctionDef) or not method.name.startswith('test_'):
                    continue
                snippet = ast.get_source_segment(code, method)
                decorators = ' '.join(ast.unparse(n) for n in cls.decorator_list + method.decorator_list)
                labels = ['offline']
                c_helper = any(isinstance(node, ast.Call) and
                               ((isinstance(node.func, ast.Name) and node.func.id == 'run_c') or
                                (isinstance(node.func, ast.Attribute) and node.func.attr == 'run_c'))
                               for node in ast.walk(method))
                if c_helper or any(token in snippet + decorators for token in ("'cc'", '"cc"', "'gcc'", '"gcc"')):
                    labels.extend(['compilacao-c', 'wsl-qemu'])
                elif any(token in decorators for token in ('linux', 'WSL', 'POSIX')):
                    labels.append('wsl-qemu')
                module = '.'.join(path.relative_to(tests_root).with_suffix('').parts)
                entries.append({'id': f'{module}.{cls.name}.{method.name}',
                                'source': path.relative_to(ROOT).as_posix(),
                                'source_sha256': sha256(path), 'classes': labels,
                                'private_fixture_possible': any(s in code for s in ('work/', 'artifacts/', 'sources/', '/home/')),
                                'phone_transport_authorized': False})
    if toolkit_only:
        return {'schema': 1, 'classification_basis': 'AST inventory of independent toolkit tests only',
                'note': 'Classification is not execution. Device integration and historical kernel results belong to the port repository.',
                'tests': entries}
    # The only current inheritance reuses two base tests with a different source.
    inherited = [entry for entry in entries if entry['id'].startswith('test_k40s_pwrap_handoff_v2.PwrapHandoffV2Tests.')]
    defined_v3 = {entry['id'].rsplit('.', 1)[1] for entry in entries
                  if entry['id'].startswith('test_k40s_pwrap_handoff_v3.PwrapHandoffV3Tests.')}
    for entry in inherited:
        method = entry['id'].rsplit('.', 1)[1]
        if method not in defined_v3:
            entries.append(dict(entry, id='test_k40s_pwrap_handoff_v3.PwrapHandoffV3Tests.' + method,
                                inherited_from=entry['id']))
    runtime_manifest = ROOT / 'manifests/kunit-uml-verification-20261025.json'
    uml_passed = (runtime_manifest.is_file() and
                  json.loads(runtime_manifest.read_text()).get('uml_passed') is True)
    car_manifest = ROOT / 'manifests/mt6357-car-extraction-verification-20261025.json'
    car_passed = car_manifest.is_file() and json.loads(car_manifest.read_text()).get('uml_passed') is True
    iio_manifest = ROOT / 'manifests/mt6357-auxadc-error-verification-20261025.json'
    iio_passed = iio_manifest.is_file() and json.loads(iio_manifest.read_text()).get('uml_passed') is True
    native_manifest = ROOT / 'manifests/mt6765-i2c-native-offline-verification-20261025.json'
    native_passed = native_manifest.is_file() and json.loads(native_manifest.read_text()).get('uml_passed') is True
    return {'schema': 1, 'classification_basis': 'AST inventory; reviewed host unittest fixtures/mocks, no physical execution',
            'note': 'wsl-qemu means POSIX/toolchain requirement, NOT proof of QEMU execution. Phone tests are separately authorized operations in tests.json.',
            'tests': entries,
            'kernel_tests': {'kunit': ['all_statuses', 'late_error_and_one_notification', 'bounded_spurious_and_cancel'],
                             'status': ('ARM32 object compiled; UML host runtime passed three cases' if uml_passed
                                        else 'ARM32 object compiled only; runtime not yet executed'),
                             'runtime_evidence': runtime_manifest.relative_to(ROOT).as_posix() if uml_passed else None,
                             'classes': ['offline', 'compilacao-c', 'wsl-qemu']},
            'component_kernel_tests': {'mt6357-car-raw': {
                'cases': ['all_car_payloads', 'ignored_bits_and_sentinels', 'invalid_inputs_preserve_output'],
                'status': 'ARM32 object compiled; UML passed' if car_passed else 'runtime not yet recorded',
                'runtime_evidence': car_manifest.relative_to(ROOT).as_posix() if car_passed else None,
                'classes': ['offline', 'compilacao-c', 'wsl-qemu']}},
            'upstream_kernel_tests': {'iio-multiply': {
                'source': 'drivers/iio/test/iio-test-multiply.c',
                'origin': 'linux-6.18.58',
                'cases': ['iio_test_iio_multiply_value_integer', 'iio_test_iio_multiply_value_fixedpoint',
                          'iio_test_iio_multiply_value_fractional', 'iio_test_iio_multiply_value_fractional_log2'],
                'status': 'UML passed; upstream suite unmodified' if iio_passed else 'runtime not yet recorded',
                'runtime_evidence': iio_manifest.relative_to(ROOT).as_posix() if iio_passed else None,
                'limitations': 'Core arithmetic only; not ADC patch or physical validation',
                'classes': ['offline', 'compilacao-c', 'wsl-qemu']}},
            'native_i2c_kernel_tests': {'mt6765-i2c-timing': {
                'source': 'kernel/tests/kunit/mt6765_i2c_timing_test.c',
                'cases': ['divider_vectors', 'divider_encoding_and_donor_khz_bound', 'invalid_dividers_preserve_outputs'],
                'classes': ['offline', 'compilacao-c', 'wsl-qemu'],
                'status': 'ARM32 object compiled; official KUnit/UML passed' if native_passed else 'runtime not yet recorded',
                'runtime_evidence': native_manifest.relative_to(ROOT).as_posix() if native_passed else None,
                'limitations': 'Pure divider encoding only, no physical I2C/IRQ/DMA or bus frequency proof'}},
            'selftests': {'portkit.sh': {'classes': ['offline', 'wsl-qemu'], 'framework': 'kselftest TEST_PROGS/TAP'}}}


if __name__ == '__main__':
    refresh = sys.argv[1:] == ['--refresh']
    destination = (ROOT / 'manifests/test-catalog.json' if refresh or len(sys.argv) == 1 else ROOT / Path(sys.argv[1]))
    if len(sys.argv) > 2:
        raise SystemExit('Usage: catalog-tests.py [new-output.json]')
    output = catalog()
    if refresh:
        staged = destination.with_suffix('.new.json')
        write_evidence(staged, output)
        os.replace(staged, destination)
    else:
        write_evidence(destination, output)
    print(f"Classified {len(output['tests'])} host tests without importing them; create-only output")
