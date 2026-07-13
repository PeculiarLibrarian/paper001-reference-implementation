from collections import Counter
from dataclasses import dataclass
from pathlib import Path

from rdflib.plugins.sparql import prepareQuery

from peculiarlibrary.SPARQL.query_library import (
    QueryIR,
    build_ir_registry,
)

DEFAULT_LIBRARY = Path(
    "peculiarlibrary/SPARQL/libraries/core_library.sparql"
)


@dataclass(frozen=True)
class QueryPlan:
    """
    Immutable execution plan.
    """

    ir: QueryIR
    strategy: str
    category: str
    query_type: str


class PlannedIRSPARQLEngine:
    """
    Deterministic SPARQL execution engine.

    Pipeline

        Registry
            ↓
        Query IR
            ↓
        Query Plan
            ↓
        Compiled SPARQL
            ↓
        Execution
    """

    def __init__(
        self,
        graph,
        registry=None,
        library_path: Path = DEFAULT_LIBRARY,
    ):
        self.graph = graph

        self._registry = (
            registry
            if registry is not None
            else build_ir_registry(library_path)
        )

    # ---------------------------------------------------------
    # Registry inspection
    # ---------------------------------------------------------

    def available_queries(self):
        return sorted(self._registry)

    def available_categories(self):
        return sorted(
            {ir.category for ir in self._registry.values()}
        )

    def available_query_types(self):
        return sorted(
            {ir.query_type for ir in self._registry.values()}
        )

    def queries_by_category(self, category):
        return sorted(
            name
            for name, ir in self._registry.items()
            if ir.category == category
        )

    def queries_by_type(self, query_type):
        return sorted(
            name
            for name, ir in self._registry.items()
            if ir.query_type == query_type
        )

    # ---------------------------------------------------------
    # Registry access
    # ---------------------------------------------------------

    def get_ir(self, name):
        return self._registry[name]

    # ---------------------------------------------------------
    # Planning
    # ---------------------------------------------------------

    def plan_query(self, name):

        ir = self.get_ir(name)

        return QueryPlan(
            ir=ir,
            strategy="STATIC",
            category=ir.category,
            query_type=ir.query_type,
        )

    # ---------------------------------------------------------
    # Compilation
    # ---------------------------------------------------------

    def compile_query(self, name):

        plan = self.plan_query(name)

        return prepareQuery(plan.ir.text)

    # ---------------------------------------------------------
    # Execution
    # ---------------------------------------------------------

    def execute(self, name):

        compiled = self.compile_query(name)

        return self.graph.query(compiled)

    # ---------------------------------------------------------
    # Registry analytics
    # ---------------------------------------------------------

    def registry_summary(self):

        return Counter(
            ir.category
            for ir in self._registry.values()
        )

    def registry_statistics(self):

        return {
            "queries": len(self._registry),
            "categories": len(
                self.available_categories()
            ),
            "query_types": len(
                self.available_query_types()
            ),
        }
