"""
PADI Rule Engine
Version: 1.0.0

Deterministic RDF-driven rule execution engine.

Responsibilities
----------------
- Evaluate executable inference rules.
- Use OperatorLibrary for comparisons.
- Produce immutable rule results.

Non-responsibilities
--------------------
- Graph mutation
- Validation
- Persistence
- Provenance materialization
"""

from __future__ import annotations

from dataclasses import dataclass

from rdflib import Graph

from peculiarlibrary.INFERENCE.operator_library import (
    OperatorLibrary,
)


@dataclass(frozen=True)
class RuleResult:
    subject: str
    assertion: str
    rule_id: str
    supporting_facts: tuple[str, ...]


class RuleEngine:

    def __init__(self, operators: OperatorLibrary | None = None):

        self.operators = operators or OperatorLibrary()

    def execute(
        self,
        rules: Graph,
        evidence: list[dict],
    ) -> list[RuleResult]:

        results: list[RuleResult] = []

        for item in evidence:

            previous = item.get("previous")
            current = item.get("current")

            if previous is None or current is None:
                continue

            operator = item.get("operator")

            if operator is None:
                continue

            if self.operators.evaluate(
                operator,
                previous,
                current,
            ):

                results.append(
                    RuleResult(
                        subject=item["entity"],
                        assertion=item["assertion"],
                        rule_id=item["rule_id"],
                        supporting_facts=(
                            item["previous_fact"],
                            item["current_fact"],
                        ),
                    )
                )

        return results
