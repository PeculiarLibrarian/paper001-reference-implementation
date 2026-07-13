"""
PADI Inference Institution
Growth Projection

Version: 4.0.0

Consumes deterministic trend assertions and derives
constitutionally valid growth projections.

Stateless.
Deterministic.
"""

from __future__ import annotations

from peculiarlibrary.INFERENCE.model import (
    DerivedAssertion,
    GrowthProjectionAssertion,
)


class GrowthProjection:

    NAME = "GrowthProjection"

    RULE_ID = "Rule0002"

    _MAPPING = {
        "PositiveTrend": "PositiveGrowthProjection",
        "NegativeTrend": "NegativeGrowthProjection",
        "StableTrend": "StableGrowthProjection",
    }

    def infer(self, trend_assertions):

        projections = []

        for trend in trend_assertions:

            if not trend.predicate.endswith("Trend"):
                continue

            projection = self._MAPPING.get(trend.obj)

            if projection is None:
                continue

            projections.append(

                GrowthProjectionAssertion(

                    subject=trend.subject,

                    predicate="hasGrowthProjection",

                    obj=projection,

                    supporting_facts=trend.supporting_facts,

                    rule_id=self.RULE_ID,
                )
            )

        return tuple(projections)

