from orchestrator.orchestrator import Orchestrator
from pprint import pprint


def test_runtime():

    ttl = """
    @prefix pl: <https://peculiarlibrarian.org/ontology/> .

    pl:Alice a pl:Person ;
        pl:hasCompetency pl:SemanticOrchestration .

    pl:OpportunityA a pl:Opportunity ;
        pl:requiresCompetency pl:SemanticOrchestration .
    """

    runtime = Orchestrator().run(ttl)

    print("===== STATUS =====")
    print(runtime["status"])
    print("READY:", runtime["ready"])

    print("\n===== SUMMARY =====")
    pprint(runtime["summary"])

    print("\n===== DECISIONS =====")
    pprint(runtime["decisions"]["ranked_opportunities"])

    assert runtime["ready"] is True
    assert runtime["status"] == "validated"
    assert len(runtime["decisions"]["ranked_opportunities"]) >= 1


if __name__ == "__main__":
    test_runtime()
