# SPDX-License-Identifier: MIT
"""POSIX process-group deadline/cleanup for isolated offline build jobs."""
import os
import signal
import subprocess
import sys


def run_group(command, *, cwd, env, log, timeout):
    if not sys.platform.startswith('linux'):
        raise ValueError('somente WSL/Linux: POSIX process groups required')
    if isinstance(command, (str, bytes)) or not command or not 0 < timeout <= 900:
        raise ValueError('Explicit argv and deadline (max 900s) required')
    process = subprocess.Popen(list(map(str, command)), cwd=cwd, env=env,
                               stdout=log, stderr=subprocess.STDOUT,
                               start_new_session=True)
    try:
        code = process.wait(timeout=timeout)
        if code:
            raise subprocess.CalledProcessError(code, command)
    except BaseException:
        # The group may outlive the leader (make/compiler children).
        try:
            os.killpg(process.pid, signal.SIGTERM)
        except ProcessLookupError:
            pass
        try:
            process.wait(timeout=3)
        except subprocess.TimeoutExpired:
            pass
        try:
            os.killpg(process.pid, signal.SIGKILL)
        except ProcessLookupError:
            pass
        process.wait(timeout=3)
        raise
