"""
PADI Technical Standard

MIS Integration Test

Validates the complete Runtime → Inference → MIS pipeline.
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


def main():

    dataset = build_canonical_view()

    registry = build_rule_registry()

    inference = InferencePipelineExecutor(
        registry
    ).execute(dataset)

    knowledge = RuntimeMISAdapter().adapt(
        dataset,
        inference,
    )

    context = MISPipelineExecutor().execute(
        knowledge
    )

    print("=" * 60)
    print("MIS INTEGRATION TEST")
    print("=" * 60)

    print("\nKNOWLEDGE")
    print("-" * 60)
    print("Triples :", len(knowledge["graph"]))
    print("Facts   :", len(knowledge["facts"]))
    print("Records :", len(knowledge["records"]))

    print("\nINFERENCE")
    print("-" * 60)
    print("Trend Assertions       :", len(knowledge["trend_assertions"]))
    print("Growth Projections     :", len(knowledge["growth_projections"]))
    print("Risk Assertions        :", len(knowledge["risk_assertions"]))
    print("Opportunity Assertions :", len(knowledge["opportunity_assertions"]))
    print("Recommendations        :", len(knowledge["recommendations"]))

    print("\nANALYTICS")
    print("-" * 60)
    print(context.analytics)

    print("\nREPORTS")
    print("-" * 60)
    print(context.reports["title"])

    print("\nDASHBOARD")
    print("-" * 60)
    print(context.dashboard["title"])

    print("\nDECISION SUPPORT")
    print("-" * 60)
    print(context.recommendations["recommendations"][0])

    print("\nMANAGEMENT SIGNALS")
    print("-" * 60)
    print(context.management_signals)

    print("\n" + "=" * 60)
    print("SYSTEM STATUS : PASS")
    print("=" * 60)


if __name__ == "__main__":
    main()
