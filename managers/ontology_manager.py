from rdflib import Graph


class OntologyManager:

    def __init__(self):
        self.graph = Graph()

    def discover(self):
        return self

    def load(self):

        self.graph = Graph()
        self.graph.parse("schemas/ontology/peculiarlibrarian.owl", format="turtle")

        return self

    def parse(self):
        return self

    def bind(self, context):
        return context

    def validate(self, context):
        return True

    def expose(self):

        return {
            "graph": self.graph,
            "triples": len(self.graph)
        }
