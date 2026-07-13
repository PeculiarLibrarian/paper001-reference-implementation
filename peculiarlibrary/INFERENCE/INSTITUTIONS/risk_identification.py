"""
PADI Inference Institution
Risk Identification

Version: 4.0.0

Consumes deterministic growth projections and derives
constitutionally valid risk assessments.

Stateless.
Deterministic.
"""

from __future__ import annotations

from peculiarlibrary.INFERENCE.model import (
    GrowthProjectionAssertion,
    RiskAssertion,
)


class RiskIdentification:

    NAME = "RiskIdentification"

    RULE_ID = "Rule0003"

    _MAPPING = {
        "PositiveGrowthProjection": "LowRisk",
        "StableGrowthProjection": "ModerateRisk",
        "NegativeGrowthProjection": "HighRisk",
    }

    def infer(self, projections):

        risks = []

        for projection in projections:

            if projection.predicate != "hasGrowthProjection":
                continue

            risk = self._MAPPING.get(projection.obj)

            if risk is None:
                continue

            risks.append(

                RiskAssertion(

                    subject=projection.subject,

                    predicate="hasRiskAssessment",

                    obj=risk,

                    supporting_facts=projection.supporting_facts,

                    rule_id=self.RULE_ID,
                )

            )

        return tuple(risks)

