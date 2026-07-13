"""
PADI Operator Library
Version: 1.0.0

Deterministic comparison operators used by the RDF-driven
Inference Rule Engine.

Responsibilities
----------------
- Execute primitive comparison operations.
- Provide immutable operator dispatch.
- Never mutate evidence.
- Never perform inference orchestration.
"""

from __future__ import annotations

from typing import Callable


class OperatorLibrary:
    """
    Canonical deterministic operator dispatcher.
    """

    def __init__(self):

        self._operators: dict[str, Callable[[float, float], bool]] = {

            "GreaterThan": self._greater_than,
            "LessThan": self._less_than,
            "EqualTo": self._equal_to,
            "GreaterThanOrEqual": self._greater_than_or_equal,
            "LessThanOrEqual": self._less_than_or_equal,
            "NotEqualTo": self._not_equal_to,

        }

    # ---------------------------------------------------------
    # Primitive operators
    # ---------------------------------------------------------

    @staticmethod
    def _greater_than(left: float, right: float) -> bool:
        return left > right

    @staticmethod
    def _less_than(left: float, right: float) -> bool:
        return left < right

    @staticmethod
    def _equal_to(left: float, right: float) -> bool:
        return left == right

    @staticmethod
    def _greater_than_or_equal(left: float, right: float) -> bool:
        return left >= right

    @staticmethod
    def _less_than_or_equal(left: float, right: float) -> bool:
        return left <= right

    @staticmethod
    def _not_equal_to(left: float, right: float) -> bool:
        return left != right

    # ---------------------------------------------------------
    # Public API
    # ---------------------------------------------------------

    def evaluate(
        self,
        operator: str,
        left: float,
        right: float,
    ) -> bool:

        fn = self._operators.get(operator)

        if fn is None:
            raise ValueError(
                f"Unknown inference operator: {operator}"
            )

        return fn(left, right)

    # ---------------------------------------------------------

    @property
    def operators(self) -> tuple[str, ...]:
        return tuple(sorted(self._operators.keys()))

    # ---------------------------------------------------------

    def __contains__(self, operator: str) -> bool:
        return operator in self._operators

