#!/bin/sh
# SPDX-License-Identifier: MIT
# kselftest TEST_PROGS/TAP entrypoint. No phone transport.
set -eu
# Explicit override wins; empty/relative/invalid never falls back to this tree.
if [ "${PORTKIT_ROOT+x}" = x ]; then
    root=$PORTKIT_ROOT
    case "$root" in
        /*) ;;
        *) printf '%s\n' 'PORTKIT_ROOT must be an absolute project directory' >&2; exit 2 ;;
    esac
    case "$root/" in
        //*|*/../*|*'\'*|*"$(printf '\r')"*|*'
'*) printf '%s\n' 'Invalid PORTKIT_ROOT; no fallback' >&2; exit 2 ;;
    esac
else
    root=$(CDPATH= cd -- "$(dirname -- "$0")/../../../.." && pwd)
fi
if [ ! -d "$root" ] || [ ! -f "$root/tools/test-offline.py" ]; then
    printf '%s\n' 'Selected project is missing tools/test-offline.py; no fallback' >&2
    exit 2
fi
output=$(mktemp)
trap 'rm -f -- "$output"' EXIT HUP INT TERM
printf 'TAP version 13\n1..1\n'
if python3 "$root/tools/test-offline.py" >"$output" 2>&1; then
    sed 's/^/# /' "$output"
    printf 'ok 1 - portkit offline host interfaces\n'
else
    sed 's/^/# /' "$output"
    printf 'not ok 1 - portkit offline host interfaces\n'
    exit 1
fi
