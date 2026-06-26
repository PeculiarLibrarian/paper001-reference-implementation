from rdflib import Graph
from rdflib.namespace import RDF
from contracts.manager_contract import ManagerContract


class TaxonomyManager(ManagerContract):

    @property
    def name(self):
        return "TaxonomyManager"

    def handshake(self):
        return {
            "manager": self.name,
            "version": "1.0",
            "contract": "manager_contract",
            "capabilities": [
                "load",
                "discover",
                "validate",
                "expose",
                "execute",
            ],
        }

    def load(self):
        self.graph = Graph()
        self.graph.parse(
            "schemas/taxonomy/competency_registry_v1.0.ttl",
            format="turtle",
        )

    def discover(self):

        concepts = []

        for subject, _, obj in self.graph.triples(
            (None, RDF.type, None)
        ):
            if str(obj).endswith("Concept"):
                concepts.append(
                    {
                        "uri": str(subject)
                    }
                )

        self.bundle = {
            "graph": self.graph,
            "taxonomy": {
                "concept_count": len(concepts)
            },
            "concepts": concepts,
        }

        return self.bundle

    def validate(self, payload):
        return (
            "graph" in payload
            and "concepts" in payload
        )

    def expose(self):
        return self.bundle

    def execute(self):

        self.load()

        payload = self.discover()

        if not self.validate(payload):
            raise RuntimeError("Taxonomy validation failed")

        return self.expose()
