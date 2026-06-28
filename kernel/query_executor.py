from pathlib import Path
from kernel.rdf_query_normalizer import RDFQueryNormalizer

class QueryExecutor:

    def __init__(self, graph_client):
        self.graph = graph_client

    def load_query(self, query_path: Path) -> str:
        return query_path.read_text()

    def run(self, query_path: Path):

        query = self.load_query(query_path)

        if hasattr(self.graph, "query"):
            results = self.graph.query(query)
            return self._normalize(results)

        if hasattr(self.graph, "execute"):
            return self.graph.execute(query)

        raise RuntimeError("No valid SPARQL backend attached")

    def _normalize(self, results):

        normalized = []

        for row in results:

            try:
                if hasattr(row, "labels"):
                    normalized.append(
                        RDFQueryNormalizer.normalize_row(row)
                    )
                else:
                    normalized.append(dict(row))

            except Exception:
                normalized.append({})

        return normalized
