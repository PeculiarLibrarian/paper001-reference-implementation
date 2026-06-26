class OpportunityEngine:

    def rank_opportunities(self, graph, instances=None):

        if instances is None:
            instances = {"competencies": [], "opportunities": []}

        # 🔥 BOOTSTRAP MODE (no instances → derive from graph)
        if not instances.get("competencies"):

            competencies = set()
            opportunities = set()

            for s, p, o in graph:

                ps = str(p)

                if "Competency" in str(o):
                    competencies.add(str(s))

                if "Opportunity" in str(o):
                    opportunities.add(str(s))

            instances["competencies"] = list(competencies)
            instances["opportunities"] = list(opportunities)

        ranked = []

        for opp in instances.get("opportunities", []):

            ranked.append({
                "opportunity": opp,
                "score": 1.0,
                "explanation": "Bootstrapped match from ontology structure"
            })

        return ranked
