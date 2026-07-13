from peculiarlibrarian.engine.runtime.sparql_runtime import SPARQLRuntime


class SPARQLOperator:

    VERSION = "2.0.0"

    def execute(self, payload):

        graph = payload["graph"]
        query = payload["query"]

        runtime = SPARQLRuntime(graph)
        raw = runtime.query(query)

        rows = []

        for row in raw["results"]:

            rows.append(
                {
                    key: str(value)
                    for key, value in row.items()
                }
            )

        return {
            "status": "ok",
            "results": rows,
            "row_count": len(rows),
            "graph": graph,
        }
