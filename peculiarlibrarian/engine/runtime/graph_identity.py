"""
Graph Identity Model
Version: 1.0.0
"""

import hashlib


class GraphIdentity:

    @staticmethod
    def compute(graph):

        """
        Deterministic identity of RDF graph.
        """

        triples = sorted(
            (str(s), str(p), str(o))
            for s, p, o in graph.triples((None, None, None))
        )

        blob = repr(triples).encode("utf-8")

        return hashlib.sha256(blob).hexdigest()

    @staticmethod
    def normalize(graph):

        if graph is None:
            return None

        return {
            "__type__": "graph_ref",
            "graph_id": GraphIdentity.compute(graph),
            "triples": len(list(graph.triples((None, None, None))))
        }
