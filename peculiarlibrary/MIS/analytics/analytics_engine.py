"""
PADI Technical Standard

Management Information System (MIS)

Semantic Analytics Engine
Version: 4.1.0

Purpose
-------
Transforms validated semantic knowledge and deterministic
inference into management analytics.

Responsibilities
----------------
- Consume validated runtime knowledge.
- Consume deterministic inference output.
- Produce analytical views only.
- Never modify canonical knowledge.
"""

from dataclasses import dataclass, field

from peculiarlibrary.MIS.analytics.knowledge_analytics_engine import (
    KnowledgeAnalyticsEngine,
)


@dataclass(slots=True)
class AnalyticsResult:

    metrics: dict = field(default_factory=dict)
    summaries: dict = field(default_factory=dict)


class AnalyticsEngine:

    def __init__(self):

        self.knowledge_engine = KnowledgeAnalyticsEngine()

    def execute(self, knowledge: dict) -> AnalyticsResult:

        result = AnalyticsResult()

        graph = knowledge.get("graph", [])
        facts = knowledge.get("facts", [])
        records = knowledge.get("records", [])

        result.metrics["triples"] = len(graph)
        result.metrics["canonical_facts"] = len(facts)
        result.metrics["evidence_records"] = len(records)

        subjects = {
            fact.entity.name
            for fact in facts
            if fact.entity is not None
        }

        predicates = {
            fact.metric.name
            for fact in facts
            if fact.metric is not None
        }

        result.metrics["subjects"] = len(subjects)
        result.metrics["predicates"] = len(predicates)

        dataset = knowledge.get("dataset")

        if dataset is not None:

            analytics = self.knowledge_engine.analyze(
                dataset
            )

            result.metrics.update(
                analytics.metrics
            )

            result.summaries.update(
                analytics.summaries
            )

        revenue = [
            fact
            for fact in facts
            if fact.metric.name == "service_revenue"
        ]

        if revenue:

            ordered = sorted(
                revenue,
                key=lambda record: record.period.label,
            )

            first = ordered[0].value
            last = ordered[-1].value

            growth = round(
                ((last - first) / first) * 100,
                2,
            )

            result.metrics["revenue_periods"] = len(
                ordered
            )

            result.metrics["revenue_growth_percent"] = growth

            result.summaries["revenue_analysis"] = (
                f"Service revenue increased from "
                f"{first} to {last} KES Millions."
            )

        result.metrics["trend_assertions"] = len(
            knowledge.get("trend_assertions", ())
        )

        result.metrics["growth_projections"] = len(
            knowledge.get("growth_projections", ())
        )

        result.metrics["risk_assertions"] = len(
            knowledge.get("risk_assertions", ())
        )

        result.metrics["opportunity_assertions"] = len(
            knowledge.get("opportunity_assertions", ())
        )

        result.metrics["recommendations"] = len(
            knowledge.get("recommendations", ())
        )

        if result.metrics["trend_assertions"] > 0:

            result.summaries["reasoning_state"] = (
                "Deterministic inference completed."
            )

        else:

            result.summaries["reasoning_state"] = (
                "Inference unavailable."
            )

        return result
