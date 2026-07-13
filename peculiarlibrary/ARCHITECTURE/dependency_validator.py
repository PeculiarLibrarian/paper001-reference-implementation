"""
PADI Architecture Dependency Validator

Checks architectural layer dependencies using Python imports.
"""

import ast
from pathlib import Path


RULES = {
    "APPLICATION": {
        "APPLICATION",
        "MIS",
        "INFERENCE",
        "RUNTIME",
    },
    "MIS": {
        "MIS",
    },
    "INFERENCE": {
        "INFERENCE",
        "RUNTIME",
    },
    "RUNTIME": {
        "RUNTIME",
    },
}


def detect_layer(path: Path):

    for part in path.parts:
        if part in RULES:
            return part

    return None


def imported_layers(tree):

    layers = set()

    for node in ast.walk(tree):

        if isinstance(node, ast.Import):

            for alias in node.names:

                name = alias.name

                for layer in RULES:

                    if name.startswith(
                        f"peculiarlibrary.{layer}"
                    ):
                        layers.add(layer)

        elif isinstance(node, ast.ImportFrom):

            if node.module is None:
                continue

            for layer in RULES:

                if node.module.startswith(
                    f"peculiarlibrary.{layer}"
                ):
                    layers.add(layer)

    return layers


def validate():

    violations = []

    root = Path("peculiarlibrary")

    for file in root.rglob("*.py"):

        source = detect_layer(file)

        if source is None:
            continue

        tree = ast.parse(
            file.read_text(encoding="utf-8")
        )

        for target in imported_layers(tree):

            if target not in RULES[source]:

                violations.append(
                    f"{source} -> {target}: {file}"
                )

    return violations


if __name__ == "__main__":

    violations = validate()

    if violations:

        print("ARCHITECTURE VIOLATIONS")

        for violation in violations:
            print(violation)

    else:

        print("ARCHITECTURE STATUS : PASS")
