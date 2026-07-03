"""
Canonical Mapping Grammar
Version: 0.3.0

Transforms canonical JSON facts into deterministic compiler commands.

Output contract:
{
    "factory": "fin",
    "arguments": {...}
}
"""

from rdflib import URIRef

from peculiarlibrary.ontology.ontology_registry import OntologyRegistry


class CanonicalMapper:

    VERSION = "0.3.0"

    def __init__(self):
        self.registry = OntologyRegistry()

    def map(self, dataset):

        commands = []

        for fact in dataset["facts"]:

            predicate = self.registry.resolve(fact["predicate"])

            if predicate is None:
                raise ValueError(
                    f"Unknown predicate: {fact['predicate']}"
                )

            arguments = {
                "subject": URIRef(
                    "http://padi.s.m.gitandu.bs/entity/"
                    + fact["subject"].replace(" ", "_")
                ),
                "predicate": predicate,
                "object": fact["object"],
                "period": fact["period"],
                "unit": fact.get("unit"),
                "confidence": fact.get("confidence"),
                "source": fact.get("source"),
            }

            commands.append(
                {
                    "factory": "fin",
                    "arguments": arguments,
                }
            )

        return commands
