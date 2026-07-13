"""
PADI Canonical Period Model

Represents the temporal label associated
with a canonical fact.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class Period:
    """
    Immutable reporting period identity.
    """

    label: str

    def __str__(self) -> str:
        return self.label
