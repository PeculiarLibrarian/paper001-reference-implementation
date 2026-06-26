from typing import Any, Dict, List

from contracts.manager_contract import ManagerContract


class ExplanationEngine(ManagerContract):

    @property
    def name(self) -> str:
        return "ExplanationEngine"

    def __init__(self):
        self.state = {}

    def handshake(self):
        return {
            "manager": self.name,
            "version": "1.0",
            "contract": "manager_contract",
            "capabilities": [
                "load",
                "discover",
                "validate",
                "expose",
                "execute",
            ],
        }

    def load(self):
        self.state = {}

    def discover(self):
        return self.state

    def validate(self, payload: Dict[str, Any]) -> bool:
        return isinstance(payload, dict) and "explanations" in payload

    def expose(self):
        return self.state

    def _explain(self, opportunity: Dict[str, Any]) -> Dict[str, Any]:

        label = opportunity.get("opportunity")

        score = opportunity.get("score", 0)

        reasons = []

        if score >= 0.6:
            reasons.append("Strong semantic match")
        elif score >= 0.4:
            reasons.append("Moderate semantic match")
        else:
            reasons.append("Weak structural match")

        raw = opportunity.get("explanation", "")
        if raw:
            reasons.append(raw)

        return {
            "opportunity": label,
            "score": score,
            "why": reasons,
        }

    def execute(self, ranked):

        # normalize input shape
        if isinstance(ranked, dict) and "ranked_opportunities" in ranked:
            ranked = ranked["ranked_opportunities"]

        explanations = []

        for opp in ranked:
            explanations.append(self._explain(opp))

        self.state = {
            "explanations": explanations
        }

        assert self.validate(self.state)

        return self.expose()
