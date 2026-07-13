"""
SPARQL Execution Bridge
Enables query-driven semantic execution over RDF ledger.
"""

class SPARQLExecutionBridge:

    def __init__(self, runtime):
        self.runtime = runtime

    def query(self, sparql: str):
        return self.runtime.rdf.query(sparql)

    def trigger(self, sparql: str):
        """
        Query + optionally trigger execution based on results.
        """

        results = self.runtime.rdf.query(sparql)

        triggered = []

        for row in results:
            # Expecting ?operator binding
            if "operator" in row.labels():
                op = str(row["operator"])

                # deterministic safe execution only
                out = self.runtime.execute(op, {})
                triggered.append(out)

        return {
            "results": results,
            "triggered": triggered
        }
