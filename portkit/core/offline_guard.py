# SPDX-License-Identifier: MIT
"""Deny accidental phone transport, network and unreviewed subprocess use.

Defense in depth for a fixed, reviewed suite, NOT a sandbox for hostile code.
It deliberately has no override permitting USB, SSH, ADB or fastboot.
"""
import importlib.abc
from pathlib import Path
import shutil
import sys
import tempfile

FORBIDDEN_IMPORTS = frozenset({'usb', 'serial', 'mtkclient', 'lglaf', 'paramiko',
                              'adb_shell', 'pyftdi', 'fastboot', 'libusb1', 'usb1'})


class NoTransports(importlib.abc.MetaPathFinder):
    def find_spec(self, fullname, path=None, target=None):
        if fullname.split('.')[0] in FORBIDDEN_IMPORTS:
            raise ImportError('OFFLINE_ONLY: phone transport import forbidden')
        return None


def install(project):
    root = Path(project).resolve()
    loaded = FORBIDDEN_IMPORTS.intersection(sys.modules)
    if loaded:
        raise RuntimeError('OFFLINE_ONLY: a transport was already loaded')
    sys.meta_path.insert(0, NoTransports())
    commands = {str(Path(value).resolve()) for name in ('cc', 'gcc', 'patch', 'dtc', 'fdtoverlay')
                if (value := shutil.which(name))}
    # Reviewed local schema tools from this interpreter's environment only.
    # Do not permit arbitrary Python -m/-c or widen this to phone transports.
    commands.update(str(path.resolve()) for name in
                    ('dt-doc-validate', 'dt-mk-schema', 'dt-validate')
                    if (path := Path(sys.executable).parent / name).is_file())
    python = Path(sys.executable).resolve()
    temporary = Path(tempfile.gettempdir()).resolve()
    packer = root / 'tools/build-boot-image.py'

    def audit(event, args):
        if event.startswith('socket.'):
            raise PermissionError('OFFLINE_ONLY: network forbidden')
        if event in ('os.system', 'os.exec', 'os.posix_spawn', 'os.fork', 'pty.spawn'):
            raise PermissionError('OFFLINE_ONLY: unreviewed execution forbidden')
        if event == 'open' and isinstance(args[0], (str, bytes)):
            name = str(args[0])
            if name.startswith(('/dev/bus/usb', '/dev/tty', '/dev/serial', '/dev/mmc',
                                '/dev/sd', '/dev/mem', '\\\\.\\')):
                raise PermissionError('OFFLINE_ONLY: device access forbidden')
        if event == 'subprocess.Popen':
            executable, argv = args[0], args[1]
            resolved = Path(shutil.which(str(executable)) or str(executable)).resolve()
            if resolved == python:
                if len(argv) < 2 or Path(argv[1]).resolve() != packer:
                    raise PermissionError('OFFLINE_ONLY: unreviewed Python subprocess')
            elif str(resolved) not in commands:
                # The reviewed C fixtures only execute freshly compiled files in /tmp.
                if not resolved.is_relative_to(temporary) or not resolved.is_file():
                    raise PermissionError('OFFLINE_ONLY: unreviewed executable')
    sys.addaudithook(audit)


def assert_no_transports():
    if FORBIDDEN_IMPORTS.intersection(sys.modules):
        raise RuntimeError('OFFLINE_ONLY: transport unexpectedly loaded')
