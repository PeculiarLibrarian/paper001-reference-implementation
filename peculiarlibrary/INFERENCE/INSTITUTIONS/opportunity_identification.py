"""
PADI Inference Institution
Opportunity Identification

Version: 4.0.0

Consumes deterministic growth projections and risk assessments
to derive constitutionally valid opportunity assessments.

Stateless.
Deterministic.
"""

from __future__ import annotations

from peculiarlibrary.INFERENCE.model import (
    GrowthProjectionAssertion,
    RiskAssertion,
    OpportunityAssertion,
)


class OpportunityIdentification:

    NAME = "OpportunityIdentification"

    RULE_ID = "Rule0004"

    def infer(self, projections, risks):

        projection_index = {
            projection.subject: projection
            for projection in projections
        }

        opportunities = []

        for risk in risks:

            projection = projection_index.get(risk.subject)

            if projection is None:
                continue

            if (
                projection.obj == "PositiveGrowthProjection"
                and risk.obj == "LowRisk"
            ):
                opportunity = "HighOpportunity"

            elif (
                projection.obj == "StableGrowthProjection"
                and risk.obj == "ModerateRisk"
            ):
                opportunity = "ModerateOpportunity"

            else:
                opportunity = "LowOpportunity"

            supporting = tuple(
                sorted(
                    set(
                        projection.supporting_facts
                        + risk.supporting_facts
                    )
                )
            )

            opportunities.append(

                OpportunityAssertion(

                    subject=risk.subject,

                    predicate="hasOpportunityAssessment",

                    obj=opportunity,

                    supporting_facts=supporting,

                    rule_id=self.RULE_ID,
                )

            )

        return tuple(opportunities)

