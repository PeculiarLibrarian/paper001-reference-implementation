from peculiarlibrary.queries.sparql_engine import SPARQLEngine


class FinanceIntelligenceQueries:
    """
    Executive-level SPARQL queries for financial intelligence.
    Uses existing SPARQL engine (no duplication).
    """

    def __init__(self):
        from peculiarlibrarian.engine.runtime.operator_runtime import OperatorRuntime

        rt = OperatorRuntime()
        graph = rt.materialize_finance_graph(
            "peculiarlibrary/datasets/safaricom/canonical_facts.json"
        )

        self.engine = SPARQLEngine(graph)

    def total_revenue(self):
        query = """
        PREFIX pf: <https://peculiarlibrary.org/finance#>

        SELECT (SUM(?value) AS ?totalRevenue)
        WHERE {
            ?s a pf:Revenue ;
               pf:hasMetric ?value .
        }
        """
        return self.engine.graph.query(query)

    def total_cost(self):
        query = """
        PREFIX pf: <https://peculiarlibrary.org/finance#>

        SELECT (SUM(?value) AS ?totalCost)
        WHERE {
            ?s a pf:Cost ;
               pf:hasMetric ?value .
        }
        """
        return self.engine.graph.query(query)

    def profit(self):
        query = """
        PREFIX pf: <https://peculiarlibrary.org/finance#>

        SELECT (SUM(?rev) - SUM(?cost) AS ?profit)
        WHERE {
            {
                ?r a pf:Revenue ;
                   pf:hasMetric ?rev .
            }
            UNION
            {
                ?c a pf:Cost ;
                   pf:hasMetric ?cost .
            }
        }
        """
        return self.engine.graph.query(query)

    def mece_financial_breakdown(self):
        query = """
        PREFIX pf: <https://peculiarlibrary.org/finance#>

        SELECT ?type (SUM(?value) AS ?total)
        WHERE {
            ?s a ?type ;
               pf:hasMetric ?value .
            FILTER(?type IN (pf:Revenue, pf:Cost, pf:Profit))
        }
        GROUP BY ?type
        """
        return self.engine.graph.query(query)
