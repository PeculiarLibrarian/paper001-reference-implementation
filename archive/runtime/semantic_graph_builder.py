from rdflib import Graph, Namespace
from pathlib import Path

PADI = Namespace("http://padi.s.m.gitandu.bs/core#")


class SemanticGraphBuilder:
    """
    Enriches RDF graph with OWL + SKOS semantics BEFORE SPARQL execution.

    PIPELINE ORDER (now enforced):
        RAW FACTS
            ↓
        LEDGER MERGE
            ↓
        OWL + SKOS ENRICHMENT
            ↓
        SPARQL QUERY LAYER
    """

    def __init__(self, base_graph: Graph):
        if not isinstance(base_graph, Graph):
            raise TypeError("base_graph must be rdflib.Graph")

        self.base_graph = base_graph

        self.owl_graph = self._load("RDF/OWL/ontology.ttl")
        self.skos_graph = self._load("SKOS/taxonomy.ttl")

    def build(self) -> Graph:
        g = Graph()

        # 1. raw factual graph
        for triple in self.base_graph:
            g.add(triple)

        # 2. OWL enrichment layer
        for triple in self.owl_graph:
            g.add(triple)

        # 3. SKOS conceptual layer
        for triple in self.skos_graph:
            g.add(triple)

        return g

    def _load(self, path: str) -> Graph:
        g = Graph()
        file_path = Path("peculiarlibrary") / path

        if file_path.exists():
            g.parse(str(file_path), format="turtle")

        return g
