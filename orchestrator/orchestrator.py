from contracts.manager_registry import discover_managers
from managers.opportunity_engine import OpportunityEngine


class Orchestrator:
    def __init__(self):
        self.managers = discover_managers()
        self.engine = OpportunityEngine()

    def run(self, ttl):
        ontology_manager = self.managers["OntologyManager"]

        ontology = ontology_manager.discover()
        graph = ontology["graph"]
        instances = ontology["instances"]

        ranked = self.engine.rank_opportunities(graph, instances)

        return {
            # 🔑 GLOBAL CONTRACT SURFACE
            "ready": True,
            "status": "validated",

            # CORE SUMMARY
            "summary": {
                "ontology_triples": len(graph),
                "ranked_opportunities": len(ranked),
                "shape_triples": 0
            },

            # DECISIONS LAYER
            "decisions": {
                "ranked_opportunities": ranked
            }
        }
