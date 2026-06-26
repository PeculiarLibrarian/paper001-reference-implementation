"""
Field Memory Layer

Stores temporal evolution of semantic field weights.
Enables feedback-driven adaptation of reasoning priorities.
"""

class FieldMemory:

    def __init__(self):
        self.history = []

        self.current_state = {
            "GraphReasoningField": 0.25,
            "SemanticQueryField": 0.25,
            "ConceptTraversalField": 0.25,
            "StructuralInferenceField": 0.25
        }

    def update(self, field, execution_trace):
        """
        Update field weights based on execution outcomes.
        """

        self.history.append({
            "field": field,
            "trace_length": len(execution_trace)
        })

        # Simple adaptive reinforcement:
        for k in field:
            if k in self.current_state:
                self.current_state[k] = (
                    0.9 * self.current_state[k] + 0.1 * field[k]
                )

        return self.current_state

    def get(self):
        return self.current_state
