"""
PADI Technical Standard

MIS Semantic Adapter

Purpose
-------
Bridges validated runtime knowledge with semantic
business concepts.

Rules
-----
- Does not modify canonical facts.
- Does not perform inference.
- Does not validate data.
- Only exposes semantic interpretation.
"""

from rdflib import Namespace

PADI = Namespace("http://padi.engine/ontology#")


class MISSemanticAdapter:

    def adapt(self, knowledge: dict, semantic_graph):

        metrics = []

        for subject, predicate, obj in semantic_graph:

            if str(predicate).endswith("sourcePredicate"):

                metrics.append({
                    "concept": str(subject),
                    "source_predicate": str(obj),
                })

        return {
            **knowledge,
            "semantic_metrics": metrics,
        }
