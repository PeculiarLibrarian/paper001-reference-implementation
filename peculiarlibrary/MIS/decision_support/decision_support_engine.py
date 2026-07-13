"""
PADI Technical Standard

Management Information System (MIS)

Decision Support Engine

Purpose
-------
Transforms validated management information into
decision-support recommendations.

Principles
----------
- Consumes management reports.
- Never performs inference.
- Never modifies ontology.
- Produces deterministic recommendations.
"""

from dataclasses import dataclass, field

from peculiarlibrary.MIS.reports.report_engine import Report


@dataclass(slots=True)
class DecisionSupportResult:
    """
    Canonical decision-support result.
    """

    recommendations: list[str] = field(default_factory=list)
    rationale: dict = field(default_factory=dict)


class DecisionSupportEngine:
    """
    Canonical MIS Decision Support Engine.
    """

    def execute(self, report: Report) -> DecisionSupportResult:

        result = DecisionSupportResult()

        indicators = report.sections.get(
            "financial_indicators",
            {}
        )

        evidence = report.sections.get(
            "evidence_coverage",
            {}
        )

        facts = indicators.get(
            "canonical_facts",
            0
        )

        evidence_records = evidence.get(
            "evidence_records",
            0
        )

        triples = evidence.get(
            "triples",
            0
        )

        if facts == 0 or triples == 0:

            result.recommendations.append(
                "Acquire additional validated organizational knowledge."
            )

        elif evidence_records < facts:

            result.recommendations.append(
                "Review evidence coverage before strategic decision-making."
            )

        else:

            result.recommendations.append(
                "Proceed with evidence-backed management review using validated information."
            )

        result.rationale = {
            "triples": triples,
            "canonical_facts": facts,
            "evidence_records": evidence_records,
            "report": report.title,
        }

        return result
