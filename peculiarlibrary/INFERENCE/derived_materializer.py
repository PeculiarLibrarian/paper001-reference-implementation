"""
PADI Derived Materializer
Version: 2.0.0

Transforms immutable inference assertions into a derived RDF graph.

The materializer is the ONLY bridge between the inference
institutions and the semantic knowledge graph.

Responsibilities
----------------
• Materialize inference assertions as RDF
• Preserve provenance
• Never modify canonical facts

This module SHALL NOT:
• perform inference
• validate inference
• write persistence
• seal execution
"""

from __future__ import annotations

from rdflib import Graph, Literal, URIRef
from rdflib.namespace import RDF

from peculiarlibrary.INFERENCE.model import DerivedAssertion


PADI = "http://padi.s.m.gitandu.bs/core#"


class DerivedMaterializer:

    def __init__(self):

        self.InferenceResult = URIRef(PADI + "InferenceResult")
        self.InferenceProvenance = URIRef(PADI + "InferenceProvenance")

        self.generatedByRule = URIRef(PADI + "generatedByRule")
        self.supportedByFact = URIRef(PADI + "supportedByFact")
        self.hasProvenance = URIRef(PADI + "hasProvenance")

    # ---------------------------------------------------------

    def materialize(
        self,
        assertions: tuple[DerivedAssertion, ...] | list[DerivedAssertion],
    ) -> Graph:

        graph = Graph()

        for index, assertion in enumerate(assertions, start=1):

            result_uri = URIRef(
                PADI + f"InferenceResult_{index}"
            )

            provenance_uri = URIRef(
                PADI + f"InferenceProvenance_{index}"
            )

            #
            # Result node
            #

            graph.add(
                (
                    result_uri,
                    RDF.type,
                    self.InferenceResult,
                )
            )

            graph.add(
                (
                    result_uri,
                    URIRef(PADI + assertion.predicate),
                    Literal(assertion.obj),
                )
            )

            graph.add(
                (
                    result_uri,
                    URIRef(PADI + "aboutEntity"),
                    URIRef(PADI + assertion.subject),
                )
            )

            #
            # Provenance node
            #

            graph.add(
                (
                    provenance_uri,
                    RDF.type,
                    self.InferenceProvenance,
                )
            )

            graph.add(
                (
                    provenance_uri,
                    self.generatedByRule,
                    Literal(assertion.rule_id),
                )
            )

            for fact in assertion.supporting_facts:

                graph.add(
                    (
                        provenance_uri,
                        self.supportedByFact,
                        Literal(fact),
                    )
                )

            graph.add(
                (
                    result_uri,
                    self.hasProvenance,
                    provenance_uri,
                )
            )

        return graph

