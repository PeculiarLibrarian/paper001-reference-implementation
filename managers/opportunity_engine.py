class OpportunityEngine:

    def load(self):
        pass

    def execute(self, context=None):

        instances = (context or {}).get("instances", {})
        memory = (context or {}).get("semantic_state", {}).get("adaptive_state", {})

        opportunities = instances.get("opportunities", [])

        weights = memory.get("opportunity_weights", {})

        ranked = []

        for opp in opportunities:

            base = self._score(opp)

            label = opp.get("label", "")

            adaptive = weights.get(label, 0.0)

            score = min(base + adaptive, 1.0)

            ranked.append({
                "opportunity": label,
                "score": score,
                "explanation": self._explain(score)
            })

        ranked.sort(key=lambda x: x["score"], reverse=True)

        return {
            "ranked_opportunities": ranked
        }

    def _score(self, opp):

        label = opp.get("label", "").lower()

        score = 0.4

        if "job" in label:
            score += 0.2

        if "fellowship" in label:
            score += 0.15

        return score

    def _explain(self, score):

        if score > 0.7:
            return "Strong semantic alignment"
        elif score > 0.5:
            return "Moderate semantic alignment"
        return "Weak structural alignment"
