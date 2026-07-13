"""
PADI Inference Integration Test
Version: 3.0.0

End-to-end validation of the deterministic inference pipeline.
"""

from rdflib import Graph

from peculiarlibrary.RUNTIME.canonical_runtime import build_canonical_view
from peculiarlibrary.RUNTIME.evidence_runtime import EvidenceRuntime
from peculiarlibrary.INFERENCE.rule_registry import build_rule_registry
from peculiarlibrary.INFERENCE.inference_pipeline_executor import (
    InferencePipelineExecutor,
)
from peculiarlibrary.INFERENCE.inference_validator import (
    InferenceValidator,
)


def main():

    print("=" * 60)
    print("PADI INFERENCE INTEGRATION TEST")
    print("=" * 60)

    dataset = build_canonical_view()

    evidence = EvidenceRuntime().build_records(
        dataset.facts
    )

    print()
    print("RUNTIME")
    print("-" * 60)
    print("Triples          :", len(dataset.graph))
    print("Canonical facts  :", len(dataset.facts))
    print("Evidence records :", len(evidence))

    registry = build_rule_registry()

    executor = InferencePipelineExecutor(registry)

    result = executor.execute(dataset)

    print()
    print("PIPELINE")
    print("-" * 60)

    derived_graph = result["derived_graph"]

    print("Derived triples :", len(derived_graph))

    rule_graph = Graph()

    rule_graph.parse(
        "peculiarlibrary/INFERENCE/inference_rules.ttl",
        format="turtle",
    )

    validator = InferenceValidator()

    valid = validator.validate(
        canonical_graph=dataset.graph,
        derived_graph=derived_graph,
        rule_graph=rule_graph,
    )

    print()
    print("VALIDATOR")
    print("-" * 60)
    print("Conforms :", valid)

    if not valid:
        print("Errors")
        for error in validator.errors:
            print(" -", error)
        raise SystemExit(1)

    print()
    print("=" * 60)
    print("SYSTEM STATUS : PASS")
    print("=" * 60)


if __name__ == "__main__":
    main()
