from peculiarlibrary.validation.shacl_validator import SHACLValidator


class ValidateOperator:
    """
    Deterministic SHACL validation operator.

    Contract:
    - Input: rdflib.Graph (from ReasonOperator)
    - Output: validated graph + integrity flag
    """

    def __init__(self):
        self.validator = SHACLValidator()

    def execute(self, payload):
        graph = payload.get("graph")

        if graph is None:
            raise ValueError("ValidateOperator requires 'graph' from ReasonOperator")

        # Run SHACL validation (now ACTIVATED)
        try:
            conforms = self.validator.validate(graph)
        except Exception as e:
            raise RuntimeError(f"SHACL validation failed: {str(e)}")

        return {
            "status": "validated",
            "conforms": conforms,
            "graph": graph
        }
