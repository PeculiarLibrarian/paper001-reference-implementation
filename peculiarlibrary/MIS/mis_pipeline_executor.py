"""
PADI Technical Standard
Management Information System (MIS)

MIS Pipeline Executor

Purpose
-------
Canonical execution entry point for the MIS layer.

Pipeline
--------
Validated Knowledge
        │
        ▼
MIS Orchestrator
        │
        ▼
Analytics
        │
        ▼
Reports
        │
        ▼
Dashboard
        │
        ▼
Decision Support
"""

from peculiarlibrary.MIS.orchestration.mis_orchestrator import MISOrchestrator


class MISPipelineExecutor:
    """
    Canonical MIS pipeline executor.
    """

    def __init__(self):
        self.orchestrator = MISOrchestrator()

    def execute(self, knowledge: dict | None = None):
        """
        Execute the complete MIS pipeline.

        Parameters
        ----------
        knowledge : dict | None
            Validated organizational knowledge.

        Returns
        -------
        MISContext
        """
        return self.orchestrator.execute(knowledge)
