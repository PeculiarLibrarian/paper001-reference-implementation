"""
PADI Execution Context
Version: 1.0.0

Canonical mutable state for the execution plane.

Every execution handler receives and returns the same
ExecutionContext instance.
"""

from dataclasses import dataclass, field
from pathlib import Path
from rdflib import Graph
from typing import Any


@dataclass(slots=True)
class ExecutionContext:
    """
    Mutable execution state.

    The planner never modifies this object.
    The runtime owns its lifecycle.
    """

    request_id: str

    dataset: Path | None = None

    graph: Graph = field(default_factory=Graph)

    materialization_id: str | None = None

    ledger: Any = None

    query: str | None = None

    results: Any = None

    metadata: dict[str, Any] = field(default_factory=dict)

    state: dict[str, Any] = field(default_factory=dict)

    def record(self, key: str, value: Any):
        self.state[key] = value

    def fetch(self, key: str, default=None):
        return self.state.get(key, default)
