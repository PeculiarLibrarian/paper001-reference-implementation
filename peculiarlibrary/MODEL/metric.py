"""
PADI Canonical Metric Model

Represents a stable semantic measurement type
within the canonical knowledge layer.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class Metric:
    """
    Immutable metric identity.
    """

    name: str

    def __str__(self) -> str:
        return self.name
