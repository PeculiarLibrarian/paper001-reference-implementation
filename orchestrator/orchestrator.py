from contracts.manager_registry import discover_managers
from contracts.execution_resolver import resolve_execution_order


class Orchestrator:

    def __init__(self):
        self.managers = discover_managers()

    def run(self, ttl):

        context = {
            "ttl": ttl,
            "decisions": {"ranked_opportunities": []},
            "status": None,
            "ready": False
        }

        ordered = resolve_execution_order(self.managers)

        ontology_graph = None
        instances = {"competencies": [], "opportunities": []}

        for manager in ordered:

            manager.discover()
            manager.load()
            manager.parse()

            context = manager.bind(context)
            manager.validate(context)

            exposed = manager.expose()

            # 🔥 CRITICAL FIX: capture graph early and persist it
            if isinstance(exposed, dict):

                if "graph" in exposed and ontology_graph is None:
                    ontology_graph = exposed["graph"]

                if "instances" in exposed:
                    instances.update(exposed["instances"])

                if "triples" in exposed and ontology_graph is None:
                    ontology_graph = manager.graph

        from managers.opportunity_engine import OpportunityEngine

        engine = OpportunityEngine()

        ranked = engine.rank_opportunities(
            ontology_graph,
            instances
        )

        context["decisions"]["ranked_opportunities"] = ranked

        context["status"] = "validated"
        context["ready"] = True

        context["summary"] = {
            "ontology_triples": len(ontology_graph) if ontology_graph else 0,
            "ranked_opportunities": len(ranked),
            "shape_triples": 0
        }

        return context
