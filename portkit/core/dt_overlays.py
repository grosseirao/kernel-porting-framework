# SPDX-License-Identifier: MIT
"""Snapshot independent DT overlays using DTC, without board selection or phone I/O."""
from pathlib import Path
import tempfile

from .processes import run_bounded


def overlay_snapshots(base, overlays, snapshot):
    """Apply each (label, blob) to the original base, never cumulatively.

    Callers own backup authentication, variant completeness and snapshot policy.
    Failures propagate; temporary raw blobs are removed even on callback failure.
    """
    variants = list(overlays)
    labels = [label for label, _ in variants]
    if any(not isinstance(label, str) or not label or label == 'base' for label in labels):
        raise ValueError('Nonempty overlay labels distinct from base are required')
    if len(set(labels)) != len(labels):
        raise ValueError('Duplicate overlay label')
    snapshots = {'base': snapshot(base)}
    with tempfile.TemporaryDirectory(prefix='portkit-dt-private-') as directory:
        root = Path(directory)
        base_path, overlay_path, merged_path = (root / name for name in
                                                ('base.dtb', 'overlay.dtbo', 'merged.dtb'))
        base_path.write_bytes(base)
        for label, blob in variants:
            overlay_path.write_bytes(blob)
            merged_path.unlink(missing_ok=True)
            run_bounded(['fdtoverlay', '-i', str(base_path), '-o', str(merged_path),
                         str(overlay_path)], capture_output=True, timeout=15)
            snapshots[label] = snapshot(merged_path.read_bytes())
    return snapshots
