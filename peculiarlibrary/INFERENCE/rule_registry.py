"""
PADI Inference Rule Registry
Version: 2.1.0

Canonical registry of inference institutions.
"""

from dataclasses import dataclass
from typing import Iterable

from peculiarlibrary.INFERENCE.INSTITUTIONS.trend_detection import TrendDetection
from peculiarlibrary.INFERENCE.INSTITUTIONS.growth_projection import GrowthProjection
from peculiarlibrary.INFERENCE.INSTITUTIONS.risk_identification import RiskIdentification
from peculiarlibrary.INFERENCE.INSTITUTIONS.opportunity_identification import OpportunityIdentification
from peculiarlibrary.INFERENCE.INSTITUTIONS.recommendation_generation import RecommendationGeneration


@dataclass(frozen=True)
class RegisteredRule:
    name: str
    institution: object


class InferenceRuleRegistry:

    def __init__(self):
        self._rules: list[RegisteredRule] = []

    def register(self, institution) -> None:
        self._rules.append(
            RegisteredRule(
                name=institution.NAME,
                institution=institution,
            )
        )

    def names(self) -> tuple[str, ...]:
        return tuple(rule.name for rule in self._rules)

    def institutions(self) -> tuple:
        return tuple(rule.institution for rule in self._rules)

    def records(self) -> tuple[RegisteredRule, ...]:
        return tuple(self._rules)

    def __iter__(self) -> Iterable:
        return iter(self._rules)

    def __len__(self) -> int:
        return len(self._rules)


def build_rule_registry():

    registry = InferenceRuleRegistry()

    registry.register(TrendDetection())
    registry.register(GrowthProjection())
    registry.register(RiskIdentification())
    registry.register(OpportunityIdentification())
    registry.register(RecommendationGeneration())

    return registry
