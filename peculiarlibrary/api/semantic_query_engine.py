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
