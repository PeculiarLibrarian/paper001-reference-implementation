class ReasoningManager:

    def load(self):
        pass

    def execute(self, context=None):

        instances = (context or {}).get("instances", {})
        ranked = (context or {}).get("ranked_opportunities", [])
        memory = (context or {}).get("semantic_state", {}).get("adaptive_state", {})

        facts = []

        weights = memory.get("opportunity_weights", {})
        updated_weights = {}

        # --------------------------
        # ontology signals
        # --------------------------
        for opp in instances.get("opportunities", []):

            facts.append({
                "type": "OpportunityDetected",
                "label": opp["label"],
                "confidence": 0.9,
                "source": "ontology"
            })

        # --------------------------
        # reasoning + learning loop
        # --------------------------
        for opp in ranked:

            label = opp.get("opportunity")
            score = opp.get("score", 0)

            facts.append({
                "type": "RankedOpportunity",
                "label": label,
                "confidence": self._confidence(score),
                "score": score,
                "source": "reasoning"
            })

            # learning signal
            old = weights.get(label, 0.0)

            if score > 0.7:
                delta = 0.05
            elif score > 0.5:
                delta = 0.02
            else:
                delta = -0.01

            new = (old + delta) * 0.98

            updated_weights[label] = self._clamp(new)

        return {
            "facts": facts,
            "semantic_state": {
                "adaptive_state": {
                    "opportunity_weights": updated_weights
                },
                "ontology": len(instances.get("opportunities", [])),
                "taxonomy": 121
            }
        }

    def _confidence(self, score):

        if score > 0.7:
            return 1.0
        elif score > 0.5:
            return 0.8
        return 0.5

    def _clamp(self, v):

        if v > 1.0:
            return 1.0
        if v < -0.2:
            return -0.2
        return v
