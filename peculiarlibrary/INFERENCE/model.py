"""
PADI Inference Model
Version: 1.0.0

Canonical immutable inference data structures.

This module is the ONLY location that defines inference
artifacts exchanged between inference institutions.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class DerivedAssertion:
    subject: str
    predicate: str
    obj: str
    supporting_facts: tuple[str, ...]
    rule_id: str


@dataclass(frozen=True)
class GrowthProjectionAssertion:
    subject: str
    predicate: str
    obj: str
    supporting_facts: tuple[str, ...]
    rule_id: str


@dataclass(frozen=True)
class RiskAssertion:
    subject: str
    predicate: str
    obj: str
    supporting_facts: tuple[str, ...]
    rule_id: str


@dataclass(frozen=True)
class OpportunityAssertion:
    subject: str
    predicate: str
    obj: str
    supporting_facts: tuple[str, ...]
    rule_id: str


@dataclass(frozen=True)
class RecommendationAssertion:
    subject: str
    predicate: str
    obj: str
    supporting_facts: tuple[str, ...]
    rule_id: str
