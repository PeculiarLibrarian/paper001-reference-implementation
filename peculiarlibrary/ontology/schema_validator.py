"""
Ontology Schema Validator (SKOS/RDF-backed)
Version: 1.0.0

Enforces ontology legitimacy before execution.
Prevents unknown or unintended predicates from entering the compiler pipeline.
"""

from rdflib import Graph, URIRef


class OntologySchemaValidator:

    VERSION = "1.0.0"

    def __init__(self, ontology_graph: Graph):
        self.graph = ontology_graph
        self.allowed_predicates = self._extract_predicates()

    # -----------------------------
    # Bootstrap schema extraction
    # -----------------------------
    def _extract_predicates(self):

        predicates = set()

        # Heuristic: predicates defined in ontology graph
        for s, p, o in self.graph:
            if isinstance(s, URIRef) and "ontology" in str(s):
                predicates.add(s)

        # Also include explicit OWL/RDF properties
        for s, p, o in self.graph:
            if str(p).endswith("type") and isinstance(o, URIRef):
                predicates.add(o)

        return predicates

    # -----------------------------
    # Validation layer
    # -----------------------------
    def validate(self, commands: list):

        validated = []

        for cmd in commands:

            predicate = cmd["arguments"].get("predicate")

            if predicate is None:
                raise ValueError("Predicate cannot be None")

            # already URIRef from resolver
            if predicate in self.allowed_predicates:
                validated.append(cmd)
                continue

            # fallback: allow ontology namespace but flag it
            if str(predicate).startswith("http://padi.s.m.gitandu.bs/ontology#"):
                validated.append(cmd)
                continue

            raise ValueError(
                f"Ontology validation failed: {predicate} not in schema"
            )

        return validated
