from rdflib import Graph
from rdflib.namespace import SKOS

from contracts.manager_contract import ManagerContract


class CanonicalizationManager(ManagerContract):

    @property
    def name(self):
        return "CanonicalizationManager"

    def __init__(self):
        self.graph = Graph()
        self.index = {}

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
        self.graph.parse(
            "schemas/taxonomy/competency_registry.ttl",
            format="turtle",
        )

    def discover(self):

        self.index = {}

        for uri, label in self.graph.subject_objects(SKOS.prefLabel):

            canonical = str(label).strip().lower()

            self.index[canonical] = str(uri)

            fragment = str(uri).split("/")[-1].lower()

            self.index[fragment] = str(uri)

        return self.index

    def validate(self, payload):
        return len(payload) > 0

    def expose(self):
        return self.index

    def canonicalize(self, value):

        if value is None:
            return None

        key = str(value).strip().lower()

        return self.index.get(key)

    def execute(self):

        self.load()

        index = self.discover()

        assert self.validate(index)

        return self.expose()

