# SPDX-License-Identifier: MIT
"""Explicit subprocess invocation; no shell, automatic retry or phone policy."""
import subprocess


def run_checked(command, **kwargs):
    if isinstance(command, (str, bytes)) or not command:
        raise ValueError('An explicit argv sequence is required')
    if kwargs.get('shell') or kwargs.get('check') is False:
        raise ValueError('No shell or unchecked execution')
    kwargs.pop('check', None)
    return subprocess.run(list(map(str, command)), check=True, **kwargs)


def run_bounded(command, *, timeout, **kwargs):
    if not isinstance(timeout, (int, float)) or not 0 < timeout <= 60:
        raise ValueError('Explicit deadline required, at most 60 seconds')
    return run_checked(command, timeout=timeout, **kwargs)
