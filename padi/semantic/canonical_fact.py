from dataclasses import dataclass
from numbers import Number

from .observation import Observation
from .entity import Entity
from .metric import Metric
from .reporting_period import ReportingPeriod
from .measurement_unit import MeasurementUnit
from .source_record import SourceRecord


@dataclass(frozen=True, slots=True)
class CanonicalFact(Observation):
    """
    Atomic semantic observation.

    This is the canonical semantic object exchanged throughout
    the PADI Control Plane.

    No RDF.
    No URI.
    No Graph.

    One Entity
    One Metric
    One Value
    One Reporting Period
    """

    entity: Entity
    metric: Metric
    value: Number
    period: ReportingPeriod

    unit: MeasurementUnit | None = None
    source: SourceRecord | None = None

    confidence: float = 1.0
