"""
Layer Boundary Guard
Prevents cross-plane contamination in imports.
"""

import ast
from pathlib import Path


FORBIDDEN_CROSS_IMPORTS = {
    "peculiarlibrarian.engine": ["peculiarlibrary"],
    "peculiarlibrary": ["peculiarlibrarian.engine"]
}


class LayerBoundaryGuard:

    @staticmethod
    def scan_file(file_path: str):
        source = Path(file_path).read_text()
        tree = ast.parse(source)

        violations = []

        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                for n in node.names:
                    violations.extend(
                        LayerBoundaryGuard._check(n.name, file_path)
                    )

            if isinstance(node, ast.ImportFrom):
                if node.module:
                    violations.extend(
                        LayerBoundaryGuard._check(node.module, file_path)
                    )

        return violations

    @staticmethod
    def _check(module_name: str, file_path: str):

        violations = []

        for root, forbidden in FORBIDDEN_CROSS_IMPORTS.items():
            if module_name.startswith(root):
                for f in forbidden:
                    if f in module_name:
                        violations.append({
                            "file": file_path,
                            "violation": f"{root} -> {f}",
                            "module": module_name
                        })

        return violations
