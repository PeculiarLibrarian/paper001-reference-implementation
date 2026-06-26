class ReasoningManager:

    def load(self):
        pass

    def execute(self, context=None):

        core = None

        if isinstance(context, dict):
            core = context.get("core")

        if core is None:
            raise ValueError("ReasoningManager requires 'core' in context")

        facts = [
            {
                "confidence": 1.0,
                "label": "Opportunity",
                "source": "ontology",
                "type": "OpportunityDetected",
                "uri": "https://peculiarlibrarian.org/ontology/Opportunity",
            }
        ]

        return {
            "facts": facts
        }
