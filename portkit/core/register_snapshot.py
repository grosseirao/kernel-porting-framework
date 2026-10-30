# SPDX-License-Identifier: MIT
"""Validate an explicit read-only register log protocol, not register semantics."""
import re


def register_snapshot(text, *, prefix, required_markers, fields, sample_count):
    """Return only ordered, allowlisted values within their export masks.

    Fields are (bank, offset, allowed_value_bits). No address translation,
    register access, unit decoding or electrical/safety inference is performed.
    """
    if not isinstance(prefix, str) or not re.fullmatch(r'[A-Za-z0-9][A-Za-z0-9_-]{0,63}: ', prefix):
        raise ValueError('Explicit literal diagnostic prefix required')
    if (not isinstance(required_markers, (list, tuple)) or not required_markers or
            any(not isinstance(value, str) or not value or '\0' in value or '\n' in value or '\r' in value
                for value in required_markers)):
        raise ValueError('Explicit single-line capture markers required')
    if type(sample_count) is not int or not 1 <= sample_count <= 16:
        raise ValueError('Expected sample count 1..16')
    if not isinstance(fields, (list, tuple)) or not 1 <= len(fields) <= 128:
        raise ValueError('Explicit bounded register allowlist required')
    pairs, masks = [], {}
    for field in fields:
        if (not isinstance(field, (list, tuple)) or len(field) != 3 or
                any(type(value) is not int for value in field)):
            raise ValueError('Each field requires integer bank, offset and export mask')
        bank, offset, mask = field
        if not 0 <= bank <= 0xffff or not 0 <= offset <= 0xffffffff or not 0 <= mask <= 0xffffffff:
            raise ValueError('Register field outside supported encoding')
        pair = (bank, offset)
        if pair in masks:
            raise ValueError('Duplicate register field')
        pairs.append(pair)
        masks[pair] = mask
    if any(marker not in text for marker in required_markers):
        raise ValueError('Expected diagnostic capture markers')
    if text.count(prefix + 'begin version=1 read_only=1') != 1:
        raise ValueError('Expected one complete diagnostic boot; preserve capture for inspection')
    if prefix + 'refused' in text or prefix + 'map_failed' in text:
        raise ValueError('Diagnostic refused/failed, not a completed snapshot')
    matches = re.findall(re.escape(prefix) +
                         r'sample=(\d+) bank=(\d+) offset=0x([0-9a-f]+) value=0x([0-9a-f]{8})(?![0-9a-f])', text)
    if len(matches) != sample_count * len(pairs):
        raise ValueError('Unexpected number of field records')
    samples = [{} for _ in range(sample_count)]
    for index, (sample, bank, offset, value) in enumerate(matches):
        sample, bank, offset, value = int(sample), int(bank), int(offset, 16), int(value, 16)
        pair = (bank, offset)
        if sample != index // len(pairs) or pair != pairs[index % len(pairs)]:
            raise ValueError('Unexpected field order, duplicate or sample index')
        if value & ~masks[pair]:
            raise ValueError('Unexpected masked register bits; refuse exporting disallowed datum')
        samples[sample][f'{bank}:{offset:03x}'] = value
    stable = all(sample == samples[0] for sample in samples)
    end = re.findall(re.escape(prefix) +
                     f'end samples={sample_count} fields={len(pairs)} stable=([01]) read_only=1', text)
    if end != [str(int(stable))]:
        raise ValueError('Missing/inconsistent diagnostic completion marker')
    return {'samples': samples, 'stable': stable}
