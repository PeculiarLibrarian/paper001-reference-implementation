"""
PADI Technical Standard

Management Information System (MIS)

Canonical MIS Orchestrator

Responsibilities
----------------
- Consume validated knowledge package.
- Consume deterministic inference products.
- Produce management information outputs.

Restrictions
-------------
- Does not access Runtime.
- Does not execute Inference.
- Does not mutate knowledge.
"""

from dataclasses import dataclass, field

from peculiarlibrary.MIS.analytics.analytics_engine import (
    AnalyticsEngine,
)

from peculiarlibrary.MIS.interfaces.knowledge_adapter import (
    MISKnowledgeAdapter,
)

from peculiarlibrary.MIS.reports.report_engine import (
    ReportEngine,
)

from peculiarlibrary.MIS.dashboards.dashboard_engine import (
    DashboardEngine,
)

from peculiarlibrary.MIS.decision_support.decision_support_engine import (
    DecisionSupportEngine,
)

from peculiarlibrary.MIS.signals.management_signal_engine import (
    ManagementSignalEngine,
)


@dataclass(slots=True)
class MISContext:

    knowledge: dict = field(default_factory=dict)

    inference: dict = field(default_factory=dict)

    analytics: dict = field(default_factory=dict)

    reports: dict = field(default_factory=dict)

    dashboard: dict = field(default_factory=dict)

    recommendations: dict = field(default_factory=dict)

    management_signals: dict = field(default_factory=dict)



class MISOrchestrator:

    def __init__(self):

        self.adapter = MISKnowledgeAdapter()

        self.analytics_engine = AnalyticsEngine()

        self.report_engine = ReportEngine()

        self.dashboard_engine = DashboardEngine()

        self.decision_support_engine = DecisionSupportEngine()

        self.signal_engine = ManagementSignalEngine()


    def execute(self, knowledge=None):

        knowledge = knowledge or {}

        context = MISContext()


        # -------------------------
        # Knowledge Boundary
        # -------------------------

        validated_knowledge = self.adapter.adapt(
            knowledge
        )

        context.knowledge = validated_knowledge


        # -------------------------
        # Inference Product
        # -------------------------

        inference_result = {
            "trend_assertions": knowledge.get(
                "trend_assertions",
                ()
            ),

            "growth_projections": knowledge.get(
                "growth_projections",
                ()
            ),

            "risk_assertions": knowledge.get(
                "risk_assertions",
                ()
            ),

            "opportunity_assertions": knowledge.get(
                "opportunity_assertions",
                ()
            ),

            "recommendations": knowledge.get(
                "recommendations",
                ()
            ),
        }


        context.inference = inference_result


        analytics_payload = {
            **validated_knowledge,
            "inference": inference_result,
        }


        # -------------------------
        # Analytics
        # -------------------------

        analytics = self.analytics_engine.execute(
            analytics_payload
        )


        context.analytics = {
            "metrics": analytics.metrics,
            "summaries": analytics.summaries,
        }


        # -------------------------
        # Reporting
        # -------------------------

        report = self.report_engine.execute(
            analytics
        )


        context.reports = {
            "title": report.title,
            "sections": report.sections,
        }


        # -------------------------
        # Dashboard
        # -------------------------

        dashboard = self.dashboard_engine.execute(
            report
        )


        context.dashboard = {
            "title": dashboard.title,
            "widgets": dashboard.widgets,
        }


        # -------------------------
        # Decision Support
        # -------------------------

        decision = self.decision_support_engine.execute(
            report
        )


        context.recommendations = {
            "recommendations": decision.recommendations,
            "rationale": decision.rationale,
        }


        # -------------------------
        # Signals
        # -------------------------

        signals = self.signal_engine.execute(
            report
        )


        context.management_signals = {
            "signals": signals.signals,
            "indicators": signals.indicators,
        }


        return context
