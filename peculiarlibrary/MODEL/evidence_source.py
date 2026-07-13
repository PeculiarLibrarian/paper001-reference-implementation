"""
PADI Canonical Evidence Source Model

Represents provenance information attached
to canonical knowledge facts.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class EvidenceSource:
    """
    Immutable provenance record.
    """

    document: str
    page: int | None = None
    section: str | None = None
    context: str | None = None

    def __str__(self) -> str:
        return self.document
