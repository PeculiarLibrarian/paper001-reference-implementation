from rdflib import Graph
from rdflib.namespace import RDF

from contracts.manager_contract import ManagerContract


class OntologyManager(ManagerContract):

    def __init__(self):
        self.graph = Graph()

    @property
    def name(self):
        return "OntologyManager"

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
            "schemas/ontology/peculiarlibrarian.owl",
            format="turtle",
        )

    def discover(self):
        return {
            "graph": self.graph,
            "classes": self._get_classes(),
            "properties": self._get_properties(),
            "ontology": {
                "triple_count": len(self.graph)
            },
        }

    def validate(self, payload):
        return len(payload["graph"]) > 0

    def expose(self):
        return self.discover()

    def execute(self):
        self.load()
        bundle = self.discover()

        if not self.validate(bundle):
            raise RuntimeError("Ontology validation failed")

        return bundle

    def _get_classes(self):
        return [
            str(s)
            for s, _, o in self.graph.triples((None, RDF.type, None))
            if str(o).endswith("Class")
        ]

    def _get_properties(self):
        return [
            str(s)
            for s, _, o in self.graph.triples((None, RDF.type, None))
            if str(o).endswith("Property")
        ]
