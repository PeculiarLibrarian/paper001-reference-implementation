"""
Pipeline Contract Schema
Defines strict I/O expectations for all operators.
"""

PIPELINE_CONTRACT = {
    "compile": {
        "required_output_keys": ["status", "graph"]
    },
    "reason": {
        "required_output_keys": ["status", "graph"]
    },
    "validate": {
        "required_output_keys": ["status", "conforms"]
    }
}


class ContractViolation(Exception):
    pass


def validate_contract(operator_name: str, result: dict):

    if operator_name not in PIPELINE_CONTRACT:
        return

    required = PIPELINE_CONTRACT[operator_name]["required_output_keys"]

    missing = [k for k in required if k not in result]

    if missing:
        raise ContractViolation(
            f"{operator_name} missing required keys: {missing}"
        )
