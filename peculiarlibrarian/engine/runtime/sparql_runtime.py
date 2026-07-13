"""
SPARQL Runtime
Version: 1.2.0

Queries an already-materialized RDF graph.
"""

from peculiarlibrary.queries.sparql_engine import SPARQLEngine


class SPARQLRuntime:

    VERSION = "1.2.0"

    def __init__(self, graph, replay_engine=None):

        if graph is None:
            raise RuntimeError(
                "No RDF graph available. Execute 'compile' before querying."
            )

        self.engine = SPARQLEngine(graph)
        self.replay = replay_engine

        self.last_query = None
        self.last_result = None

    def query(self, sparql: str):

        self.last_query = sparql

        raw = list(self.engine.execute(sparql))

        rows = []

        for row in raw:

            if hasattr(row, "asdict"):
                rows.append(
                    {
                        str(k): str(v)
                        for k, v in row.asdict().items()
                    }
                )

            else:
                rows.append(str(row))

        self.last_result = rows

        if self.replay is not None:
            try:
                self.replay.record(
                    runtime=self,
                    operator_name="sparql_query",
                    payload={"query": sparql},
                    result={"count": len(rows)}
                )
            except Exception:
                pass

        return {
            "query": sparql,
            "results": rows,
            "count": len(rows)
        }

    def explain(self):

        return {
            "query": self.last_query,
            "results": self.last_result
        }
