from contracts.architecture_validator import ArchitectureValidator
from orchestrator.execution_engine import ExecutionEngine


class Orchestrator:

    def __init__(self):

        self.validator = ArchitectureValidator()

        self.engine = ExecutionEngine()

    def run(self, ttl=None):

        #
        # Architecture gate
        #

        self.validator.validate()

        #
        # Runtime execution
        #

        result = self.engine.run()

        outputs = result.get("outputs", {})

        ranked = []

        explanations = []

        #
        # Safe contract assembly
        #

        for payload in outputs.values():

            if not isinstance(payload, dict):
                continue

            ranked.extend(
                payload.get(
                    "ranked_opportunities",
                    [],
                )
            )

            explanations.extend(
                payload.get(
                    "explanations",
                    [],
                )
            )

        result["decisions"] = {
            "ranked_opportunities": ranked,
            "explanations": explanations,
        }

        return result
