"""
PADI Technical Standard

Management Information System (MIS)

Report Engine

Purpose
-------
Transforms validated analytical results into
management-ready reports.

Principles
----------
- Consumes AnalyticsResult only.
- Never performs inference.
- Never queries ontology directly.
- Produces deterministic reports.
"""

from dataclasses import dataclass, field

from peculiarlibrary.MIS.analytics.analytics_engine import AnalyticsResult


@dataclass(slots=True)
class Report:
    """
    Canonical management report.
    """

    title: str
    sections: dict = field(default_factory=dict)


class ReportEngine:
    """
    Canonical MIS reporting engine.
    """

    def execute(self, analytics: AnalyticsResult) -> Report:

        report = Report(
            title="Management Information Report"
        )

        report.sections["executive_summary"] = {
            "status": analytics.summaries.get(
                "status"
            ),
            "knowledge_state": analytics.summaries.get(
                "knowledge_state"
            ),
            "revenue_analysis": analytics.summaries.get(
                "revenue_analysis",
                "No revenue analysis available."
            ),
        }

        report.sections["financial_indicators"] = {
            "canonical_facts": analytics.metrics.get(
                "canonical_facts",
                0
            ),
            "revenue_periods": analytics.metrics.get(
                "revenue_periods",
                0
            ),
            "revenue_growth_percent": analytics.metrics.get(
                "revenue_growth_percent",
                0
            ),
        }

        report.sections["evidence_coverage"] = {
            "triples": analytics.metrics.get(
                "triples",
                0
            ),
            "evidence_records": analytics.metrics.get(
                "evidence_records",
                0
            ),
        }

        report.sections["management_signals"] = {
            "knowledge_state": analytics.summaries.get(
                "knowledge_state",
                "unknown"
            ),
            "evidence_status": (
                "Evidence coverage complete."
                if analytics.metrics.get(
                    "evidence_records",
                    0
                ) >= analytics.metrics.get(
                    "canonical_facts",
                    0
                )
                else "Evidence coverage requires review."
            ),
            "revenue_direction": (
                "Positive growth trend identified."
                if analytics.metrics.get(
                    "revenue_growth_percent",
                    0
                ) > 0
                else "No positive revenue growth identified."
            ),
        }

        return report
