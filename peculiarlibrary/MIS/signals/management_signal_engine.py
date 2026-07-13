"""
PADI Technical Standard

Management Information System (MIS)

Management Signal Engine

Purpose
-------
Transforms management reports into deterministic
operational signals.

Principles
----------
- Consumes Report only.
- Never performs inference.
- Never modifies knowledge.
- Produces management indicators only.
"""

from dataclasses import dataclass, field

from peculiarlibrary.MIS.reports.report_engine import Report


@dataclass(slots=True)
class ManagementSignals:
    """
    Canonical management signal output.
    """

    signals: list[str] = field(default_factory=list)
    indicators: dict = field(default_factory=dict)


class ManagementSignalEngine:
    """
    Deterministic MIS signal processor.
    """

    def execute(self, report: Report) -> ManagementSignals:

        result = ManagementSignals()

        financial = report.sections.get(
            "financial_indicators",
            {}
        )

        evidence = report.sections.get(
            "evidence_coverage",
            {}
        )

        growth = financial.get(
            "revenue_growth_percent",
            0
        )

        facts = financial.get(
            "canonical_facts",
            0
        )

        records = evidence.get(
            "evidence_records",
            0
        )

        if growth >= 40:
            result.signals.append(
                "Strong revenue growth trajectory detected."
            )
        elif growth > 0:
            result.signals.append(
                "Positive revenue growth detected."
            )
        else:
            result.signals.append(
                "Revenue growth requires review."
            )

        if records >= facts:
            result.signals.append(
                "Evidence coverage is complete."
            )
        else:
            result.signals.append(
                "Evidence coverage requires improvement."
            )

        result.indicators = {
            "revenue_growth_percent": growth,
            "canonical_facts": facts,
            "evidence_records": records,
            "signal_state": "generated",
        }

        return result
