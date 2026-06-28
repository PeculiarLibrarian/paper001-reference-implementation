from rdflib import Graph

class RDFGraphClient:

    def __init__(self, ttl_files: list[str]):
        self.graph = Graph()

        for file in ttl_files:
            self.graph.parse(file, format="turtle")

    def query(self, sparql_query: str):
        return self.graph.query(sparql_query)
