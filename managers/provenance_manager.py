class ProvenanceManager:
    """
    Canonical provenance manager.

    Responsibility:
        Trace semantic derivation chains.

    Does NOT:
        mutate facts
        perform inference
        rank outputs
    """

    def handshake(self):

        return {
            "manager": "ProvenanceManager",
            "version": "1.0",
            "contract": "manager_contract",
            "capabilities": [
                "trace",
                "provenance",
                "execute",
            ],
        }

    def execute(self, context):

        facts = context.get("facts", [])

        provenance = []

        for fact in facts:

            if isinstance(fact, dict):

                fact_value = fact.get("fact")

                confidence = fact.get("confidence", 1.0)

            else:

                fact_value = fact

                confidence = 1.0

            provenance.append({

                "fact": fact_value,

                "confidence": confidence,

                "derived_from": [

                    "Ontology",

                    "Instances",

                    "SemanticCore",

                    "Reasoning",

                ],

            })

        return {

            "provenance": provenance

        }
