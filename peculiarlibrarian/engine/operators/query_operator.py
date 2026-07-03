"""
Query Operator
Version: 1.0.0

Executes SPARQL queries over RDF graphs stored in runtime context.
"""

from rdflib import Graph


class QueryOperator:

    VERSION = "1.0.0"

    def execute(self, payload: dict):

        graph = payload.get("graph")
        query = payload.get("query")

        if not isinstance(graph, Graph):
            raise ValueError("QueryOperator requires RDF Graph")
        if not query:
            raise ValueError("QueryOperator requires SPARQL query")

        results = graph.query(query)

        output = []
        for row in results:
            output.append([str(x) for x in row])

        return {
            "status": "queried",
            "row_count": len(output),
            "results": output,
        }
