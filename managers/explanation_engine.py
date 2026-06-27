class ExplanationEngine:

    def load(self):
        pass

    def execute(self, context=None):

        ranked = (context or {}).get("ranked_opportunities", [])
        facts = (context or {}).get("facts", [])

        # index facts by opportunity label
        fact_index = {}

        for f in facts:
            label = f.get("label")
            if label:
                fact_index.setdefault(label, []).append(f)

        explanations = []

        for opp in ranked:

            label = opp.get("opportunity")
            score = opp.get("score", 0)

            related_facts = fact_index.get(label, [])

            explanations.append({
                "opportunity": label,
                "score": score,
                "why": self._build_reasoning_chain(opp, related_facts)
            })

        return {
            "explanations": explanations
        }

    def _build_reasoning_chain(self, opp, facts):

        chain = []

        score = opp.get("score", 0)

        # --------------------------
        # 1. score interpretation
        # --------------------------
        if score >= 0.7:
            chain.append("Strong semantic alignment")
        elif score >= 0.5:
            chain.append("Moderate semantic alignment")
        else:
            chain.append("Weak structural alignment")

        # --------------------------
        # 2. fact-driven reasoning
        # --------------------------
        for f in facts[:3]:  # limit noise
            chain.append(f.get("type", "SignalDetected") + " signal")

        # --------------------------
        # 3. fallback reasoning
        # --------------------------
        if not facts:
            chain.append("Derived from ontology structure")

        return chain
