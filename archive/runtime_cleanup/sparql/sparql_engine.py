from rdflib import Graph
from rdflib.plugins.sparql import prepareQuery
from pathlib import Path


class SPARQLEngine:
    """
    PURE in-memory SPARQL execution layer (FINAL CORRECT MODEL)

    Contract:
    - Accepts ONLY rdflib.Graph
    - Never touches ledger
    - Never loads files internally
    """

    def __init__(self, graph: Graph):
        if not isinstance(graph, Graph):
            raise TypeError("SPARQLEngine expects rdflib.Graph")

        self.graph = graph

    def execute(self, query_ref):

        # Always resolve query file ONLY (no graph loading here)
        if isinstance(query_ref, (str, Path)):
            query_path = Path(query_ref)

            registry = Path("peculiarlibrary/RUNTIME/sparql/query_library")

            if not query_path.exists():
                query_path = (registry / query_path.name)

            if not query_path.exists():
                raise FileNotFoundError(
                    f"SPARQL query not found: {query_path}"
                )

            query_text = query_path.read_text()

        else:
            raise TypeError("Query must be a file path")

        query = prepareQuery(query_text)

        # CRITICAL FIX: run ONLY against in-memory graph
        return self.graph.query(query)
