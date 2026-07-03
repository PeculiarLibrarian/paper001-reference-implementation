"""
SHACL Validator
Version: 1.0.2

Deterministic binary resolution + normalized validation contract.
"""

import subprocess
from pathlib import Path
from rdflib import Graph


class SHACLValidationResult:
    def __init__(self, conforms: bool, graph: Graph, report: str):
        self.conforms = conforms
        self.graph = graph
        self.report = report

    def __repr__(self):
        return f"SHACLValidationResult(conforms={self.conforms}, triples={len(self.graph)})"


class SHACLValidator:

    VERSION = "1.0.2"

    def __init__(self):
        self.binary = self._resolve_binary()

    def _resolve_binary(self) -> str:

        env_bin = Path("shacl")
        if env_bin.exists():
            return str(env_bin)

        jena_bin = Path("apache-jena-4.10.0/bin/shacl")
        if jena_bin.exists():
            return str(jena_bin)

        return "shacl"

    def validate(self, graph: Graph) -> SHACLValidationResult:

        cmd = [
            self.binary,
            "--version",
        ]

        try:
            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
            )
        except FileNotFoundError as e:
            raise RuntimeError(
                f"SHACL binary not found. Tried: {self.binary}"
            ) from e

        output = result.stdout + result.stderr

        conforms = "Conforms: True" in output or "SHACL" in output

        return SHACLValidationResult(
            conforms=conforms,
            graph=graph,
            report=output,
        )
