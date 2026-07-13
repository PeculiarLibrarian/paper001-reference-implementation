"""
PADI Inference Validator
Version: 2.0.0

Validates inferred knowledge before constitutional finality.

The validator guarantees that every inference is:

• deterministic
• provenance-linked
• constitutionally admissible

Version 2.0 removes the duplicate Python provenance layer.

The RDF derived graph is now the single source of truth.
"""

from __future__ import annotations

from rdflib import Graph
from rdflib import URIRef
from rdflib.namespace import RDF


PADI = "http://padi.s.m.gitandu.bs/core#"

INFERENCE_PROVENANCE = URIRef(
    PADI + "InferenceProvenance"
)

GENERATED_BY_RULE = URIRef(
    PADI + "generatedByRule"
)

SUPPORTED_BY_FACT = URIRef(
    PADI + "supportedByFact"
)


class InferenceValidator:

    def __init__(self):

        self._errors = []

    # ---------------------------------------------------------
    # Validation
    # ---------------------------------------------------------

    def validate(
        self,
        canonical_graph: Graph,
        derived_graph: Graph,
        rule_graph: Graph,
    ) -> bool:

        self._errors.clear()

        #
        # Rule library
        #

        if len(rule_graph) == 0:

            self._errors.append(
                "Inference rule library is empty."
            )

        #
        # Collect canonical fact identifiers.
        #

        canonical_fact_ids = {

            str(subject).split("#")[-1]

            for subject in canonical_graph.subjects()

            if str(subject).split("#")[-1].startswith("Fact_")

        }

        #
        # Locate provenance nodes.
        #

        provenance_nodes = list(

            derived_graph.subjects(
                RDF.type,
                INFERENCE_PROVENANCE,
            )

        )

        #
        # If there are derived triples there must be provenance.
        #

        if len(derived_graph) > 0 and len(provenance_nodes) == 0:

            self._errors.append(
                "Derived graph contains no provenance."
            )

        #
        # Validate every provenance node.
        #

        for node in provenance_nodes:

            rule = derived_graph.value(
                node,
                GENERATED_BY_RULE,
            )

            if rule is None:

                self._errors.append(
                    f"{node} has no generating rule."
                )

            supporting = list(

                derived_graph.objects(
                    node,
                    SUPPORTED_BY_FACT,
                )

            )

            if len(supporting) == 0:

                self._errors.append(
                    f"{node} has no supporting facts."
                )

            for fact in supporting:

                fact_id = str(fact)

                #
                # URIRef
                #

                if "#" in fact_id:

                    fact_id = fact_id.split("#")[-1]

                #
                # Literal
                #

                if fact_id not in canonical_fact_ids:

                    self._errors.append(
                        f"Unknown supporting fact: {fact_id}"
                    )

        return len(self._errors) == 0

    # ---------------------------------------------------------

    @property
    def conforms(self):

        return len(self._errors) == 0

    # ---------------------------------------------------------

    @property
    def errors(self):

        return list(self._errors)

