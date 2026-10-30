# SPDX-License-Identifier: MIT
"""Literal saved-Kconfig values and requirement comparison, not a resolver.

Keep quoting/escapes verbatim. Kconfig/olddefconfig still owns dependencies,
symbol validity and the final configuration. Duplicate assignments use the
last occurrence, matching the existing fragment/workspace behavior.
"""


def config_values(text):
    result = {}
    for line in text.splitlines():
        if line.startswith('CONFIG_') and '=' in line:
            key, value = line.split('=', 1)
            result[key] = value
        elif line.startswith('# CONFIG_') and line.endswith(' is not set'):
            result[line[2:-11]] = 'n'
    return result


def mismatched_symbols(actual, required):
    """List divergent names in fragment order without exposing private values.

    A missing disabled option is equivalent to n, as for invisible booleans in
    saved .config. Missing y/m/string/number is never silently satisfied.
    """
    return [key for key, value in required.items() if actual.get(key, 'n') != value]


def verify_required_config(actual, required):
    """Compatibility check for the build workspace's fail-fast error contract."""
    mismatches = mismatched_symbols(actual, required)
    if mismatches:
        key = mismatches[0]
        raise ValueError(f'Kconfig dropped/changed required option {key}={required[key]}')
