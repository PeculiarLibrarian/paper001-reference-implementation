from rdflib import Graph, URIRef
from rdflib.namespace import SKOS, RDFS


class CompetencyInferenceManager:

    def __init__(self):
        self.graph = Graph()

    def handshake(self):
        return {
            "manager": "CompetencyInferenceManager",
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

    def execute(self):
        self.load()

    def _label(self, uri):

        label = self.graph.value(uri, SKOS.prefLabel)

        if label:
            return str(label)

        label = self.graph.value(uri, RDFS.label)

        if label:
            return str(label)

        return str(uri).split("/")[-1]

    def _node(self, uri):

        return {
            "uri": str(uri),
            "label": self._label(uri),
        }

    def infer(self, competency):

        broader = [
            self._node(parent)
            for parent in self.graph.objects(
                competency,
                SKOS.broader,
            )
        ]

        narrower = [
            self._node(child)
            for child in self.graph.subjects(
                SKOS.broader,
                competency,
            )
        ]

        related = [
            self._node(rel)
            for rel in self.graph.objects(
                competency,
                SKOS.related,
            )
        ]

        return {
            "competency": self._node(competency),
            "broader": broader,
            "narrower": narrower,
            "related": related,
        }
