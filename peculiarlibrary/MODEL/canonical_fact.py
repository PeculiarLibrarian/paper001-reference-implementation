"""
PADI Canonical Fact Model

Immutable semantic fact representation.

A CanonicalFact is the atomic unit of
validated knowledge flowing through the runtime.
"""

from dataclasses import dataclass

from peculiarlibrary.MODEL.entity import Entity
from peculiarlibrary.MODEL.metric import Metric
from peculiarlibrary.MODEL.period import Period
from peculiarlibrary.MODEL.unit import Unit
from peculiarlibrary.MODEL.evidence_source import EvidenceSource


@dataclass(frozen=True)
class CanonicalFact:
    """
    Immutable canonical semantic fact.
    """

    entity: Entity
    metric: Metric
    value: float
    unit: Unit | None
    period: Period
    source: EvidenceSource | None = None
    confidence: float = 1.0

    def __post_init__(self):
        if not 0.0 <= self.confidence <= 1.0:
            raise ValueError(
                "Confidence must be between 0.0 and 1.0"
            )

    def __str__(self) -> str:
        return (
            f"{self.entity.name} | "
            f"{self.metric.name} | "
            f"{self.value} {self.unit} | "
            f"{self.period.label}"
        )
