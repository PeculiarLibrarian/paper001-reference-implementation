from rdflib import Graph, SKOS

class SKOSExpander:

    def __init__(self, graph: Graph):
        self.graph = graph

    def expand_concept(self, concept_uri: str):
        """
        Expands a concept into all broader/narrower nodes
        """

        expanded = set()
        expanded.add(concept_uri)

        for s, p, o in self.graph:
            if str(s) == concept_uri:
                expanded.add(str(o))

            if str(o) == concept_uri:
                expanded.add(str(s))

        return expanded
