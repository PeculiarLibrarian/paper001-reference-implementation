class OpportunityEngine:

    def load(self):
        pass

    def execute(self, context=None):

        instances = {}

        if isinstance(context, dict):
            instances = context.get("instances", {})

        opportunities = instances.get("opportunities", []) if isinstance(instances, dict) else []

        ranked = self._rank(opportunities)

        # 🔥 FIX: must match dependency contract EXACTLY
        return {
            "ranked_opportunities": ranked
        }

    def _rank(self, opportunities):

        ranked = []

        for opp in opportunities:

            ranked.append({
                "opportunity": opp["label"],
                "score": 0.5,
                "explanation": "Opportunity signal"
            })

        return ranked
