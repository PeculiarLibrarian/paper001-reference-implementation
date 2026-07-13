"""
PADI Inference Institution
Recommendation Generation

Version: 4.0.0

Consumes constitutionally valid opportunity assessments
and derives deterministic advisory recommendations.

Stateless.
Deterministic.
"""

from __future__ import annotations

from peculiarlibrary.INFERENCE.model import (
    OpportunityAssertion,
    RecommendationAssertion,
)


class RecommendationGeneration:

    NAME = "RecommendationGeneration"

    RULE_ID = "Rule0005"

    _MAPPING = {
        "HighOpportunity": "RecommendInvest",
        "ModerateOpportunity": "RecommendMonitor",
        "LowOpportunity": "RecommendAvoid",
    }

    def infer(self, opportunities):

        recommendations = []

        for opportunity in opportunities:

            if opportunity.predicate != "hasOpportunityAssessment":
                continue

            recommendation = self._MAPPING.get(opportunity.obj)

            if recommendation is None:
                continue

            recommendations.append(

                RecommendationAssertion(

                    subject=opportunity.subject,

                    predicate="hasRecommendation",

                    obj=recommendation,

                    supporting_facts=opportunity.supporting_facts,

                    rule_id=self.RULE_ID,
                )

            )

        return tuple(recommendations)

