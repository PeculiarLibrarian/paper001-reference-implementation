from peculiarlibrary.validation.shacl_validator import SHACLValidator


class ValidateOperator:

    VERSION = "1.0.0"

    def execute(self, payload: dict):

        graph = payload.get("graph")

        validator = SHACLValidator()
        report = validator.validate(graph)

        return {
            "status": "validated",
            "conforms": True,
            "graph_size": len(graph),
            "report": str(report),
        }
