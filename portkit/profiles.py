# SPDX-License-Identifier: MIT
"""Board profile loading, independent from any USB/flash backend."""
import json
import ipaddress
import os
from pathlib import Path, PureWindowsPath, PurePosixPath
import re
import subprocess


def _unique_object(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError('Duplicate board profile field: ' + key)
        result[key] = value
    return result


def _invalid_constant(value):
    raise ValueError('Non-JSON numeric constant: ' + value)


def _workspace_root(project):
    """Explicit workspace input, never the package location or terminal cwd."""
    try:
        root = Path(project)
    except TypeError:
        raise ValueError('Expected an explicit absolute workspace root') from None
    if not root.is_absolute() or any(c in str(root) for c in '\0\r\n'):
        raise ValueError('Expected an explicit absolute workspace root')
    return root.resolve()


def load_board(project, name):
    if not isinstance(name, str) or not re.fullmatch('[a-z0-9][a-z0-9-]*', name):
        raise ValueError('Invalid board identifier')
    root = _workspace_root(project)
    path = root / 'boards' / name / 'profile.json'
    if not path.resolve().is_relative_to(root / 'boards') or path.is_symlink():
        raise ValueError('Escaping board profile')
    board = json.loads(path.read_text(encoding='utf-8'), object_pairs_hook=_unique_object,
                       parse_constant=_invalid_constant)
    if not isinstance(board, dict) or type(board.get('schema')) is not int or board.get('schema') != 1 or board.get('id') != name:
        raise ValueError('Unknown board schema or identity')
    profile = board['kernel']['default_profile']
    relative = Path(profile)
    if relative.is_absolute() or '..' in relative.parts:
        raise ValueError('Escaping kernel profile')
    return board


def development_root(board, override=None, *, project=None):
    """Explicit CLI path wins; otherwise read the board's runtime from root .env."""
    if override is not None:
        value = override
    else:
        root = _workspace_root(project)
        settings = _load_lab_data(root, board).get('development')
        if not isinstance(settings, dict):
            raise ValueError('Configure KPF_' + board['id'].upper().replace('-', '_') + '_RUNTIME_ROOT in .env or --runtime-root')
        value = settings.get('runtime_root')
    if (not isinstance(value, (str, Path)) or not str(value) or
            any(c in str(value) for c in '\0\r\n') or
            str(value).startswith(('\\\\', '//')) or
            '..' in PurePosixPath(value).parts or '..' in PureWindowsPath(value).parts or
            not Path(value).is_absolute()):
        raise ValueError('Expected an absolute local development runtime root for this host')
    runtime = Path(value)
    if os.name == 'posix' and runtime.resolve().is_relative_to(Path('/mnt')):
        raise ValueError('Use a Linux development runtime outside /mnt; no fallback')
    return runtime


def cycle_defaults(project, board):
    """Read only the two migrated defaults; never load a phone transport."""
    root = _workspace_root(project)
    image = board['recovery']['image']
    release = board['kernel']['normal_release']
    if (not isinstance(image, str) or not image or '\\' in image or ':' in image
            or Path(image).is_absolute() or '..' in Path(image).parts):
        raise ValueError('Invalid recovery image path')
    target = root / image
    if not target.resolve().is_relative_to(root):
        raise ValueError('Escaping recovery image path')
    if not isinstance(release, str) or not re.fullmatch(r'[A-Za-z0-9][A-Za-z0-9._+-]*', release):
        raise ValueError('Invalid normal kernel release')
    return target, release


def da_board_defaults(board):
    """Board data only; DA protocol and transport stay in the legacy backend."""
    recovery = board['recovery']
    sector, size = recovery['boot_a_sector'], recovery['boot_a_bytes']
    page, digest = recovery['sector_bytes'], recovery['sha256']
    if (type(page) is not int or page != 512 or type(sector) is not int
            or type(size) is not int or not 0 < sector < 2**32
            or not 0 < size <= 2**32 or size % page
            or sector + size // page > 2**32):
        raise ValueError('Invalid DA boot geometry')
    if not isinstance(digest, str) or not re.fullmatch('[0-9a-f]{64}', digest):
        raise ValueError('Invalid DA recovery SHA-256')
    regions = []
    for name in ('pstore', 'lklog', 'atflog'):
        region = board['dram'][name]
        address, length = region['address'], region['bytes']
        if (type(address) is not int or type(length) is not int
                or not 0 < address < 2**32 or not 0 < length <= 0x100000
                or address % 4 or length % 4 or address + length > 2**32):
            raise ValueError('Invalid DA capture region: ' + name)
        if any(address < start + count and start < address + length
               for _, start, count in regions):
            raise ValueError('Overlapping DA capture regions')
        regions.append((name, address, length))
    return sector, size, digest, tuple(regions)


def _load_lab_data(project, board):
    """Read strict literal dotenv settings without executing/exporting/interpolating.

    CLI overrides are handled by consumers. Process environment and legacy JSON
    are not fallback sources; duplicates, malformed values and symlinks fail.
    """
    root = _workspace_root(project)
    expected = '.env'
    if board.get('lab_configuration') != expected:
        raise ValueError('Unexpected local laboratory configuration path')
    path = root / expected
    if path.is_symlink() or path.resolve().parent != root:
        raise ValueError('Escaping laboratory configuration')
    fields = {'RUNTIME_ROOT', 'NORMAL_SSH_HOST', 'NORMAL_SSH_USER', 'NORMAL_SSH_PORT',
              'USB_SSH_HOST', 'USB_SSH_USER', 'USB_SSH_PORT', 'SSH_IDENTITY_FILE',
              'STRICT_HOST_KEY_CHECKING', 'KNOWN_HOSTS_FILE', 'NOTE', 'AUTHORITY'}
    prefix = 'KPF_' + board['id'].upper().replace('-', '_') + '_'
    lab, seen = {}, set()
    for number, line in enumerate(path.read_text(encoding='utf-8-sig').splitlines(), 1):
        line = line.strip()
        if not line or line.startswith('#'):
            continue
        key, separator, value = line.partition('=')
        key, value = key.strip(), value.strip()
        if not separator or not re.fullmatch(r'[A-Z][A-Z0-9_]*', key) or key in seen:
            raise ValueError(f'Invalid or duplicate .env assignment at line {number}')
        seen.add(key)
        if value.startswith('"'):
            try:
                value = json.loads(value)
            except ValueError:
                raise ValueError(f'Invalid quoted .env value at line {number}') from None
        elif value.startswith("'"):
            if len(value) < 2 or not value.endswith("'") or "'" in value[1:-1]:
                raise ValueError(f'Invalid quoted .env value at line {number}')
            value = value[1:-1]
        if not isinstance(value, str) or any(c in value for c in '\0\r\n'):
            raise ValueError(f'Invalid .env value at line {number}')
        if not key.startswith(prefix):
            continue
        field = key[len(prefix):]
        if field not in fields:
            raise ValueError(f'Unknown board .env setting at line {number}')
        if field.endswith('_PORT'):
            if not re.fullmatch(r'[0-9]+', value):
                raise ValueError(f'Expected integer port at line {number}')
            value = int(value)
        elif field == 'STRICT_HOST_KEY_CHECKING':
            if value not in ('true', 'false'):
                raise ValueError(f'Expected literal boolean at line {number}')
            value = value == 'true'
        if field == 'RUNTIME_ROOT':
            lab['development'] = {'runtime_root': value}
        else:
            lab[field.lower()] = value
    return lab


def load_lab(project, board):
    """Private SSH configuration, read lazily before any transport is opened."""
    root = _workspace_root(project)
    lab = _load_lab_data(root, board)
    if lab.get('strict_host_key_checking') is not True:
        raise ValueError('Laboratory requires strict SSH host key verification')
    host = lab.get('normal_ssh_host')
    if not isinstance(host, str):
        raise ValueError('Normal SSH host must be an IPv4 address')
    ipaddress.IPv4Address(host)
    contract = board.get('ssh_contract')
    fields = {'normal_ssh_user', 'normal_ssh_port', 'usb_ssh_host', 'usb_ssh_user', 'usb_ssh_port'}
    if not isinstance(contract, dict) or set(contract) != fields:
        raise ValueError('Missing or invalid board SSH contract; no default policy')
    for name in ('normal_ssh_user', 'usb_ssh_user'):
        value = contract[name]
        if not isinstance(value, str) or not re.fullmatch(r'[A-Za-z_][A-Za-z0-9_-]{0,63}', value):
            raise ValueError('Invalid board SSH user contract')
    for name in ('normal_ssh_port', 'usb_ssh_port'):
        if type(contract[name]) is not int or not 1 <= contract[name] <= 65535:
            raise ValueError('Invalid board SSH port contract')
    if not isinstance(contract['usb_ssh_host'], str):
        raise ValueError('Invalid board USB SSH host contract')
    ipaddress.IPv4Address(contract['usb_ssh_host'])
    if any(type(lab.get(name)) is not type(contract[name]) or lab[name] != contract[name]
           for name in fields):
        raise ValueError('Laboratory settings differ from the validated SSH contract')
    identity = lab.get('ssh_identity_file')
    if (not isinstance(identity, str) or any(c in identity for c in '\x00\r\n')
            or identity.startswith(('\\\\', '//'))
            or not (PureWindowsPath(identity).is_absolute() or PurePosixPath(identity).is_absolute())
            or '..' in PureWindowsPath(identity).parts or '..' in PurePosixPath(identity).parts):
        raise ValueError('SSH identity must be an absolute external path')
    # Check both native paths and Windows paths as seen from WSL.
    windows = PureWindowsPath(identity)
    candidate = Path(identity)
    if windows.is_absolute() and not candidate.is_absolute():
        try:
            converted = subprocess.run(['wslpath', '-a', '-u', identity], check=True,
                                       capture_output=True, text=True, timeout=10)
        except (OSError, subprocess.SubprocessError):
            raise ValueError('Cannot validate foreign SSH identity path; configure a native path or working wslpath') from None
        value = converted.stdout.removesuffix('\n').removesuffix('\r')
        if (converted.stderr or not value or any(c in value for c in '\0\r\n') or
                not Path(value).is_absolute() or value.startswith('//') or
                '..' in PurePosixPath(value).parts or '\\' in value):
            raise ValueError('Invalid wslpath result for SSH identity; no fallback')
        candidate = Path(value)
    if candidate.resolve().is_relative_to(root):
        raise ValueError('SSH private key must remain outside the repository')
    return lab
