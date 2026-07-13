"""
PADI Technical Standard

Management Service

Purpose
-------
Canonical application service connecting the
validated Runtime, deterministic Inference,
and the Management Information System.
"""

from peculiarlibrary.RUNTIME.canonical_runtime import (
    build_canonical_view,
)

from peculiarlibrary.INFERENCE.rule_registry import (
    build_rule_registry,
)

from peculiarlibrary.INFERENCE.inference_pipeline_executor import (
    InferencePipelineExecutor,
)

from peculiarlibrary.MIS.interfaces.runtime_adapter import (
    RuntimeMISAdapter,
)

from peculiarlibrary.MIS.mis_pipeline_executor import (
    MISPipelineExecutor,
)


class ManagementService:
    """
    Canonical application orchestration service.
    """

    def __init__(self):

        self.adapter = RuntimeMISAdapter()

        self.registry = build_rule_registry()

        self.inference = InferencePipelineExecutor(
            self.registry
        )

        self.mis = MISPipelineExecutor()

    def execute(self):

        #
        # Stage 1
        # Canonical Runtime
        #
        dataset = build_canonical_view()

        #
        # Stage 2
        # Deterministic Inference
        #
        inference_result = self.inference.execute(
            dataset
        )

        #
        # Stage 3
        # Runtime → MIS Boundary
        #
        knowledge = self.adapter.adapt(
            dataset,
            inference_result,
        )

        #
        # Stage 4
        # Management Information System
        #
        return self.mis.execute(
            knowledge
        )
