"""
PADI Canonical Unit Model

Represents the measurement unit attached
to a canonical fact value.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class Unit:
    """
    Immutable measurement unit identity.
    """

    name: str

    def __str__(self) -> str:
        return self.name
