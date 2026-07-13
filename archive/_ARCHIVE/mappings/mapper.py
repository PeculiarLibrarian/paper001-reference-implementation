"""
Canonical Mapping Grammar
Version: 1.2.0

STRICT CONTRACT MODE:
- No optional structural fields allowed to be missing
- Deterministic schema enforcement
"""

from rdflib import URIRef


class Mapper:

    VERSION = "1.2.0"

    REQUIRED_FIELDS = {"subject", "predicate", "object", "period"}

    def __init__(self):
        pass

    def _validate_fact(self, fact: dict):

        missing = self.REQUIRED_FIELDS - fact.keys()

        if missing:
            raise ValueError(
                f"Mapping Integrity violation: missing fields {sorted(missing)}"
            )

    def _resolve_predicate(self, predicate: str):

        return URIRef(
            "http://padi.s.m.gitandu.bs/ontology#" + predicate
        )

    def map(self, dataset):

        if "facts" not in dataset:
            raise KeyError("Dataset missing required 'facts' field")

        commands = []

        for fact in dataset["facts"]:

            self._validate_fact(fact)

            commands.append({
                "factory": "fin",
                "arguments": {
                    "subject": URIRef(
                        "http://padi.s.m.gitandu.bs/entity/"
                        + fact["subject"].replace(" ", "_")
                    ),
                    "predicate": self._resolve_predicate(fact["predicate"]),
                    "object": fact["object"],
                    "period": fact["period"],
                    "unit": fact.get("unit"),
                    "confidence": fact.get("confidence"),
                    "source": fact.get("source"),
                },
            })

        return commands
