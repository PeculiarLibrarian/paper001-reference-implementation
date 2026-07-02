"""
Safaricom Mapping Grammar
Version: 0.2.0

Transforms canonical JSON-LD facts into generic compiler commands.

The mapper performs NO RDF generation.

Output contract:

{
    "factory": "...",
    "arguments": {...}
}
"""

from rdflib import URIRef

from peculiarlibrary.ontology.ontology_registry import OntologyRegistry


class SafaricomMapper:

    VERSION = "0.2.0"

    def __init__(self):

        self.registry = OntologyRegistry()

    def map(self, dataset):

        commands = []

        for fact in dataset["facts"]:

            predicate = self.registry.resolve(
                fact["predicate"]
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
