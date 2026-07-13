"""
PADI Assertion Builder
Version: 2.0.0

Purpose
-------
Materialize deterministic inference assertions into RDF.

Responsibilities
----------------
- Convert derived assertions into RDF resources.
- Preserve rule provenance.
- Preserve supporting facts.
- Produce derived assertion graph.

Non-responsibilities
--------------------
- NO inference execution.
- NO rule evaluation.
- NO validation.
- NO persistence.
"""

from __future__ import annotations

from rdflib import Graph, Literal, Namespace, RDF, URIRef
from rdflib.namespace import XSD


PADI = Namespace(
    "http://padi.s.m.gitandu.bs/core#"
)


class AssertionBuilder:

    def __init__(self):

        self._counter = 0


    # ---------------------------------------------------------

    def build(self, assertions) -> Graph:

        graph = Graph()

        graph.bind(
            "padi",
            PADI,
        )

        for assertion in assertions:

            self._counter += 1

            assertion_node = URIRef(
                PADI[
                    f"DerivedAssertion_{self._counter:06d}"
                ]
            )

            provenance_node = URIRef(
                PADI[
                    f"InferenceProvenance_{self._counter:06d}"
                ]
            )

            #
            # Assertion resource
            #

            graph.add(
                (
                    assertion_node,
                    RDF.type,
                    PADI.DerivedAssertion,
                )
            )

            graph.add(
                (
                    assertion_node,
                    PADI.subject,
                    URIRef(
                        PADI[
                            self._clean(assertion.subject)
                        ]
                    ),
                )
            )

            graph.add(
                (
                    assertion_node,
                    PADI.predicate,
                    URIRef(
                        PADI[
                            self._clean(assertion.predicate)
                        ]
                    ),
                )
            )

            graph.add(
                (
                    assertion_node,
                    PADI.object,
                    URIRef(
                        PADI[
                            self._clean(assertion.obj)
                        ]
                    ),
                )
            )

            #
            # Provenance
            #

            graph.add(
                (
                    provenance_node,
                    RDF.type,
                    PADI.InferenceProvenance,
                )
            )

            graph.add(
                (
                    provenance_node,
                    PADI.generatedByRule,
                    Literal(
                        assertion.rule_id
                    ),
                )
            )

            graph.add(
                (
                    assertion_node,
                    PADI.hasProvenance,
                    provenance_node,
                )
            )

            #
            # Supporting evidence
            #

            for fact in assertion.supporting_facts:

                graph.add(
                    (
                        provenance_node,
                        PADI.supportedByFact,
                        Literal(fact),
                    )
                )

        return graph


    # ---------------------------------------------------------

    @staticmethod
    def _clean(value):

        return (
            str(value)
            .replace(" ", "")
            .replace(",", "")
            .replace("(", "")
            .replace(")", "")
        )
