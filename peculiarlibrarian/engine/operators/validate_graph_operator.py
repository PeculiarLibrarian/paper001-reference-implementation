from peculiarlibrary.engine.validation.graph_contract_validator import GraphContractValidator


class ValidateGraphOperator:

    def execute(self, payload):

        graph = payload["graph"]

        validator = GraphContractValidator()
        report = validator.validate(graph)

        payload["validation_report"] = report

        if not report["valid"]:
            payload["status"] = "invalid_graph"

        return payload
