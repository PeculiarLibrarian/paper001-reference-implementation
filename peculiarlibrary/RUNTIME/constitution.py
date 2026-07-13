"""
PADI Runtime Constitution
Version: 2.0.0

Defines deterministic runtime invariants.

This module contains ONLY constitutional evaluation.
"""

from dataclasses import dataclass


@dataclass
class InvariantReport:
    name: str
    passed: bool
    details: str = ""


class PADIConstitution:

    def __init__(self):
        self._invariants = (
            self.graph_non_empty,
            self.query_library_loaded,
            self.ontology_present,
            self.fact_graph_consistent,
        )

    def graph_non_empty(self, context):
        graph = context["graph"]

        return InvariantReport(
            "GRAPH_NON_EMPTY",
            len(graph) > 0,
            f"triples={len(graph)}",
        )

    def query_library_loaded(self, context):
        queries = context["queries"]

        if isinstance(queries, dict):
            query_names = list(queries.keys())
        else:
            query_names = list(queries)

        return InvariantReport(
            "QUERY_LIBRARY_LOADED",
            len(query_names) > 0,
            f"queries={query_names}",
        )

    def ontology_present(self, context):
        return InvariantReport(
            "ONTOLOGY_PRESENT",
            context["ontology_ok"],
            "core ontology loaded",
        )

    def fact_graph_consistent(self, context):
        return InvariantReport(
            "FACT_GRAPH_CONSISTENT",
            context["fact_triples"] > 0,
            f"facts={context['fact_triples']}",
        )

    def evaluate(self, context):
        return [rule(context) for rule in self._invariants]


def run_constitution(context):
    return PADIConstitution().evaluate(context)
