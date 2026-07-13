"""
CompileOperator
Version: 7.0.0

The operator does not compile data.

Compilation already occurs inside the Canonical Runtime.

This operator simply exposes the immutable canonical dataset
to the Operator Plane.
"""

from peculiarlibrary.RUNTIME.canonical_runtime import build_canonical_view


class CompileOperator:
    VERSION = "7.0.0"

    def execute(self, payload=None):
        dataset = build_canonical_view()

        return {
            "status": "success",
            "runtime": {
                "dataset": dataset,
                "graph": dataset.graph,
                "facts": dataset.facts,
                "records": dataset.records,
            },
            "integrity": {
                "valid": True,
                "fact_count": len(dataset.facts),
                "record_count": len(dataset.records),
                "triple_count": dataset.triple_count,
            },
        }
