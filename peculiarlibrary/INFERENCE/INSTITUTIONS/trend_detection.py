"""
PADI Inference Institution
Trend Detection

Version: 4.0.0

Consumes canonical evidence and derives immutable trend
assertions.

This institution is deterministic and stateless.
"""

from __future__ import annotations

from collections import defaultdict

from peculiarlibrary.INFERENCE.model import DerivedAssertion


class TrendDetection:

    NAME = "TrendDetection"

    RULE_ID = "Rule0001"

    POSITIVE = "PositiveTrend"
    NEGATIVE = "NegativeTrend"
    STABLE = "StableTrend"

    METRIC_LABELS = {
        "service_revenue": "Revenue",
        "mpesa_revenue": "MpesaRevenue",
        "ebitda": "EBITDA",
    }

    def infer(self, evidence):

        grouped = defaultdict(list)

        for record in evidence:
            grouped[
                (
                    record.entity,
                    record.metric,
                )
            ].append(record)

        assertions = []

        for (entity, metric), records in grouped.items():

            ordered = sorted(
                records,
                key=lambda r: r.period,
            )

            if len(ordered) < 2:
                continue

            previous = ordered[-2]
            current = ordered[-1]

            if current.value > previous.value:
                trend = self.POSITIVE

            elif current.value < previous.value:
                trend = self.NEGATIVE

            else:
                trend = self.STABLE

            metric_label = self.METRIC_LABELS.get(
                metric,
                metric.replace("_", "").title(),
            )

            assertions.append(

                DerivedAssertion(

                    subject=entity,

                    predicate=f"has{metric_label}Trend",

                    obj=trend,

                    supporting_facts=(
                        previous.fact_id,
                        current.fact_id,
                    ),

                    rule_id=self.RULE_ID,
                )
            )

        return tuple(assertions)

