# SPDX-License-Identifier: MIT
"""Create-only JSON evidence; publication is atomic and refuses replacement."""
import json
import os
from pathlib import Path
import tempfile


def write_evidence(path, value):
    path = Path(path)
    # Serialize before creating even a temporary output.
    payload = (json.dumps(value, sort_keys=True, indent=2, ensure_ascii=False,
                          allow_nan=False) + '\n').encode('utf-8')
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, name = tempfile.mkstemp(prefix='.evidence-', dir=path.parent)
    temporary = Path(name)
    try:
        with os.fdopen(fd, 'wb') as stream:
            stream.write(payload)
            stream.flush()
            os.fsync(stream.fileno())
        # Hard-link publication is atomic and fails if destination exists.
        # No rename/replace fallback: preserve the create-only guarantee.
        os.link(temporary, path)
        if os.name == 'posix':
            directory = os.open(path.parent, os.O_RDONLY | os.O_DIRECTORY)
            try:
                os.fsync(directory)
            finally:
                os.close(directory)
    finally:
        temporary.unlink(missing_ok=True)
    return path
