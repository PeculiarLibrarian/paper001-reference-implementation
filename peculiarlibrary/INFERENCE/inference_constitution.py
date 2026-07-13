"""
PADI Inference Constitution
Executable Enforcement Layer
Version: 1.0.0

Enforces constitutional preconditions before inference
execution may begin.

This module does not perform inference.

It determines whether inference is constitutionally
permitted.
"""

from __future__ import annotations

from pathlib import Path

from rdflib import Graph


class InferenceConstitution:

    def __init__(self):

        self._violations = []

    # ---------------------------------------------------------

    def evaluate(
        self,
        canonical_graph: Graph,
        rule_graph: Graph,
        runtime_sealed: bool,
        constitution_path: str | Path,
    ) -> bool:

        self._violations.clear()

        # ---------------------------------------------
        # Constitution exists
        # ---------------------------------------------

        constitution = Path(constitution_path)

        if not constitution.exists():

            self._violations.append(
                "Inference Constitution missing."
            )

        # ---------------------------------------------
        # Canonical graph exists
        # ---------------------------------------------

        if len(canonical_graph) == 0:

            self._violations.append(
                "Canonical graph is empty."
            )

        # ---------------------------------------------
        # Rule library exists
        # ---------------------------------------------

        if len(rule_graph) == 0:

            self._violations.append(
                "Inference rule library is empty."
            )

        # ---------------------------------------------
        # Runtime already sealed
        # ---------------------------------------------

        if not runtime_sealed:

            self._violations.append(
                "Runtime Finality has not been sealed."
            )

        return len(self._violations) == 0

    # ---------------------------------------------------------

    @property
    def conforms(self):

        return len(self._violations) == 0

    # ---------------------------------------------------------

    @property
    def violations(self):

        return list(self._violations)

