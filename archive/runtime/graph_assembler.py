from rdflib import Graph, URIRef, Literal
from pathlib import Path


class GraphAssembler:
    """
    Deterministic RDF graph composer.

    RULES:
    - NO None values allowed
    - ONLY valid RDF terms allowed
    - Always sanitizes incoming graphs
    """

    def __init__(self, runtime_graph: Graph, ledger_graph: Graph):
        if not isinstance(runtime_graph, Graph):
            raise TypeError("runtime_graph must be rdflib.Graph")

        if not isinstance(ledger_graph, Graph):
            raise TypeError("ledger_graph must be rdflib.Graph")

        self.runtime_graph = self._sanitize(runtime_graph)
        self.ledger_graph = self._sanitize(ledger_graph)

        self.ontology_graph = self._load("RDF/OWL/ontology.ttl")
        self.skos_graph = self._load("SKOS/taxonomy.ttl")

    def build(self) -> Graph:
        g = Graph()

        for triple in self.runtime_graph:
            g.add(triple)

        for triple in self.ledger_graph:
            g.add(triple)

        for triple in self.ontology_graph:
            g.add(triple)

        for triple in self.skos_graph:
            g.add(triple)

        return g

    def _sanitize(self, graph: Graph) -> Graph:
        """
        Removes invalid RDF triples (None-safe enforcement).
        """
        clean = Graph()

        for s, p, o in graph:
            if s is None or p is None or o is None:
                continue

            clean.add((s, p, o))

        return clean

    def _load(self, path: str) -> Graph:
        g = Graph()
        file_path = Path("peculiarlibrary") / path

        if file_path.exists():
            g.parse(str(file_path), format="turtle")

        return g
