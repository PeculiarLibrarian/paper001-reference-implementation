"""
IngestionManager (MECE Layer 1)

Responsibility:
- Accept raw inputs (files, strings, RDF graphs, TTL, SPARQL results)
- Normalize into a unified internal representation
- DO NOT interpret meaning
- DO NOT validate semantics
- DO NOT transform ontology logic
"""

from rdflib import Graph


class IngestionManager:
    def __init__(self):
        self.source_type = None

    def load(self, source):
        """
        Load raw input into a normalized graph object.
        """
        if isinstance(source, Graph):
            self.source_type = "rdflib.Graph"
            return source

        if isinstance(source, str):
            g = Graph()
            try:
                g.parse(data=source, format="turtle")
                self.source_type = "ttl_string"
                return g
            except Exception:
                # fallback: treat as identifier-only graph seed
                self.source_type = "string_seed"
                return self._seed_graph(source)

        raise TypeError("Unsupported ingestion type")

    def _seed_graph(self, seed):
        """
        Minimal deterministic placeholder graph.
        No inference allowed here.
        """
        g = Graph()
        return g

    def validate(self, graph):
        """
        Structural sanity check only.
        """
        if graph is None:
            raise ValueError("Graph cannot be None")

        return True

    def expose(self, graph):
        """
        Return raw graph unchanged.
        """
        return graph
