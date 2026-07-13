"""
PADI Execution Plan
Version: 1.0.0

Immutable execution contract for the execution plane.

Execution components consume an ExecutionPlan.
They never invent their own execution contracts.
"""

from dataclasses import dataclass, field
from typing import Any


@dataclass(frozen=True, slots=True)
class ExecutionStep:
    """
    One deterministic execution step.
    """

    stage: str
    operation: str
    parameters: dict[str, Any] = field(default_factory=dict)


@dataclass(frozen=True, slots=True)
class ExecutionPlan:
    """
    Immutable execution plan.
    """

    version: str
    request_id: str
    steps: tuple[ExecutionStep, ...]

    def __len__(self):
        return len(self.steps)

    def __iter__(self):
        return iter(self.steps)

    def stage_names(self):
        return tuple(step.stage for step in self.steps)
