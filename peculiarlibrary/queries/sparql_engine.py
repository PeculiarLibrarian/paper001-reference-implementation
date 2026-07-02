from rdflib import Graph

class SPARQLEngine:

    def __init__(self, graph: Graph):
        self.graph = graph

    def execute(self, query: str):
        # IMPORTANT: ensure rdflib namespace resolution is used
        return self.graph.query(query)

    def select_all(self):
        return self.graph.query("""
        SELECT ?s ?p ?o
        WHERE { ?s ?p ?o . }
        """)
