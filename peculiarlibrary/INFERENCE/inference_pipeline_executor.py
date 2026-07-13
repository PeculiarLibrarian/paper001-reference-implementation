"""
PADI Inference Pipeline Executor
Version: 3.0.0
"""

from peculiarlibrary.RUNTIME.evidence_runtime import EvidenceRuntime
from peculiarlibrary.INFERENCE.assertion_builder import AssertionBuilder


class InferencePipelineExecutor:

    def __init__(self, registry):

        self.registry = registry
        self.evidence_runtime = EvidenceRuntime()
        self.builder = AssertionBuilder()

    def execute(self, dataset):

        current = self.evidence_runtime.build_records(
            dataset.facts
        )

        all_assertions = []

        outputs = {}

        for registered in self.registry:

            institution = registered.institution

            name = institution.NAME

            if name == "TrendDetection":

                current = institution.infer(current)

                outputs["trend_assertions"] = current

            elif name == "GrowthProjection":

                current = institution.infer(current)

                outputs["growth_projections"] = current

            elif name == "RiskIdentification":

                current = institution.infer(current)

                outputs["risk_assertions"] = current

            elif name == "OpportunityIdentification":

                current = institution.infer(
                    outputs["growth_projections"],
                    outputs["risk_assertions"],
                )

                outputs["opportunity_assertions"] = current

            elif name == "RecommendationGeneration":

                current = institution.infer(current)

                outputs["recommendations"] = current

            all_assertions.extend(current)

        derived_graph = self.builder.build(all_assertions)

        return {
            "derived_graph": derived_graph,
            "derived_assertions": tuple(all_assertions),
            **outputs,
        }
