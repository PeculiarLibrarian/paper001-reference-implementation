from contracts.architecture_validator import ArchitectureValidator

from orchestrator.execution_engine import ExecutionEngine

from kernel.runtime_descriptor import RuntimeDescriptor


class Orchestrator:

    def __init__(self):

        self.validator = ArchitectureValidator()

        self.engine = ExecutionEngine()

        self.runtime = RuntimeDescriptor()

    def run(self, ttl=None):

        #
        # Validate architecture before execution
        #

        self.validator.validate()

        #
        # Execute runtime
        #

        result = self.engine.run()

        outputs = result.get("outputs", {})

        ranked = []

        explanations = []

        #
        # Assemble decision outputs
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

        #
        # Attach canonical runtime descriptor
        #

        result["runtime"] = self.runtime.build()

        return result
