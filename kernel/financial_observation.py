from dataclasses import dataclass


@dataclass(frozen=True)
class FinancialObservation:
    """
    Canonical financial observation model.
    """

    # Identity
    identifier: str

    # Observation target
    company: str
    reporting_scope: str

    # Semantic meaning
    metric: str
    reporting_period: str

    # Measured value
    value: str

    currency: str
    scale: str
    measurement_unit: str

    # Provenance
    evidence: str
    citation: str

    # Quality
    observation_status: str
    observation_confidence: str

    def as_dict(self) -> dict:

        return {

            "identifier": self.identifier,
            "company": self.company,
            "reporting_scope": self.reporting_scope,
            "metric": self.metric,
            "reporting_period": self.reporting_period,
            "value": self.value,
            "currency": self.currency,
            "scale": self.scale,
            "measurement_unit": self.measurement_unit,
            "evidence": self.evidence,
            "citation": self.citation,
            "observation_status": self.observation_status,
            "observation_confidence": self.observation_confidence,
        }

    @property
    def iri(self):

        return f"fin:{self.identifier}"
