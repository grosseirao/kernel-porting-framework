# SPDX-License-Identifier: MIT
"""Result vocabulary only; no implicit execution or recovery retries."""
from dataclasses import dataclass
from enum import Enum


class TestClass(str, Enum):
    OFFLINE = 'offline'
    C_COMPILE = 'compilacao-c'
    WSL_QEMU = 'wsl-qemu'
    PHONE_READONLY = 'telefone-somente-leitura'
    PHONE_TEMP_WRITE = 'telefone-escrita-temporaria'
    RECOVERY_REQUIRED = 'recuperacao-obrigatoria'


class State(str, Enum):
    PENDING = 'pending'
    PASSED = 'passed'
    FAILED = 'failed'
    SKIPPED = 'skipped'
    RECOVERY_REQUIRED = 'recovery-required'


@dataclass(frozen=True)
class StepResult:
    name: str
    state: State
    classification: TestClass
    evidence_path: str | None = None
