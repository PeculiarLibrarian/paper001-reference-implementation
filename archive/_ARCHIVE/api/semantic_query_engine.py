from peculiarlibrary.queries.sparql_engine import SPARQLEngine
from peculiarlibrary.api.nl_to_sparql import NLToSPARQL

class SemanticQueryEngine:

    def __init__(self, graph):
        self.graph = graph
        self.sparql = SPARQLEngine(graph)
        self.translator = NLToSPARQL()

    def ask(self, question: str):
        print(f"🧠 Interpreting: {question}")

        query = self.translator.translate(question)

        print("\n🔍 SPARQL GENERATED:\n")
        print(query)

        results = self.sparql.execute(query)

        print("\n📊 RESULTS:\n")
        for r in results:
            print(r)

        return results

from peculiarlibrary.api.finance_intelligence_queries import FinanceIntelligenceQueries


class ExtendedSemanticQueryEngine:
    """
    Wrapper extending semantic query engine with finance intelligence layer.
    """

    def __init__(self):
        self.finance = FinanceIntelligenceQueries()

    def revenue(self):
        return self.finance.total_revenue()

    def cost(self):
        return self.finance.total_cost()

    def profit(self):
        return self.finance.profit()

    def mece(self):
        return self.finance.mece_financial_breakdown()
