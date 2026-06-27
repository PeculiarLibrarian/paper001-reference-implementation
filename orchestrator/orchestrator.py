from orchestrator.execution_engine import ExecutionEngine


class Orchestrator:

    def __init__(self):
        self.engine = ExecutionEngine()

    def run(self, ttl):

        result = self.engine.run()

        outputs = result.get("outputs", {})

        ranked = []
        explanations = []

        # --------------------------
        # SAFE CONTRACT ASSEMBLY
        # --------------------------
        for _, payload in outputs.items():

            if isinstance(payload, dict):

                if "ranked_opportunities" in payload:
                    ranked = payload["ranked_opportunities"]

                if "explanations" in payload:
                    explanations = payload["explanations"]

        result["decisions"] = {
            "ranked_opportunities": ranked,
            "explanations": explanations
        }

        return result
