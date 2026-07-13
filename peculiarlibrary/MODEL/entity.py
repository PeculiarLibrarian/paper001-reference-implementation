"""
PADI Canonical Entity Model

Represents a stable semantic entity in the canonical knowledge layer.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class Entity:
    """
    Immutable entity identity.
    """

    name: str

    def __str__(self) -> str:
        return self.name
