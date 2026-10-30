# SPDX-License-Identifier: MIT
"""Structural contract for future backends, not a flash implementation."""
from typing import Protocol
from portkit.core.results import StepResult


class RecoveryBackend(Protocol):
    """Opaque plans are backend-specific; a BROM plan is NOT a Firehose plan.

    Implementations must require explicit identity/profile/authorization and
    bounded operations, persist evidence, never retry uncertain writes, and
    report verified recovery separately from a command acknowledgement.
    """
    def inspect(self, *, board: dict, timeout: float) -> dict: ...
    def validate_plan(self, *, board: dict, plan: dict) -> dict: ...
    def execute_once(self, *, plan: dict, authorization: str,
                     timeout: float) -> StepResult: ...
    def recover(self, *, board: dict, evidence: dict,
                authorization: str, timeout: float) -> StepResult: ...


class HostTransport(Protocol):
    """ADB/fastboot adapter contract only; no discovery on import."""
    def identify(self, *, timeout: float) -> dict: ...
    def run_authorized(self, *, argv: tuple[str, ...], authorization: str,
                       timeout: float) -> StepResult: ...
