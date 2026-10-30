#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Safe, fixed offline suite. No discovery of transport/physical tests."""
import json
from pathlib import Path
import re
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]


def main():
    if sys.argv[1:]:
        raise SystemExit('No test names, commands or hardware switches accepted')
    if not sys.platform.startswith('linux'):
        raise SystemExit('somente WSL/Linux: execute python3 tools/test-offline.py dentro do WSL')
    sys.path.insert(0, str(ROOT))
    sys.path.insert(0, str(ROOT / 'tools/tests'))
    from portkit.core.offline_guard import install, assert_no_transports
    install(ROOT)
    manifest = json.loads((ROOT / 'manifests/tests.json').read_text())
    modules = manifest['safe_offline_modules']
    if (not modules or len(modules) != len(set(modules)) or
            any(not re.fullmatch(r'(?:toolkit\.)?test_[a-z0-9_]+', name) or
                not (ROOT / 'tools/tests' / (name.replace('.', '/') + '.py')).is_file() for name in modules)):
        raise ValueError('Invalid offline allowlist')
    # Names are a checked-in allowlist, not CLI input or discovered tests.
    print('OFFLINE_ONLY: no phone transport; fixed allowlist; no network', flush=True)
    suite = unittest.defaultTestLoader.loadTestsFromNames(modules)
    result = unittest.TextTestRunner(verbosity=2).run(suite)
    assert_no_transports()
    print('OFFLINE_ONLY: no transport loaded; legacy laboratory suite is separate')
    return 0 if result.wasSuccessful() else 1


if __name__ == '__main__':
    raise SystemExit(main())
