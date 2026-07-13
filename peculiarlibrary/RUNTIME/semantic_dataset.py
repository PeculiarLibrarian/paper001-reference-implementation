"""
PADI Runtime Semantic Dataset

Purpose
-------
Immutable in-memory representation of canonical semantic state.

Responsibilities
----------------
- Hold RDF graph.
- Hold canonical facts.
- Hold immutable inference evidence records.
- Expose graph statistics.

Non-responsibilities
--------------------
- NO loading from disk.
- NO SPARQL execution.
- NO reasoning.
- NO inference execution.
"""

from rdflib import Graph


class SemanticDataset:

    def __init__(
        self,
        graph: Graph,
        facts: tuple = (),
        records: tuple = (),
    ):
        self._graph = graph
        self._facts = facts
        self._records = records

    @property
    def graph(self) -> Graph:
        return self._graph

    @property
    def facts(self) -> tuple:
        return self._facts

    @property
    def records(self) -> tuple:
        return self._records

    @property
    def triple_count(self) -> int:
        return len(self._graph)

    def __len__(self):
        return len(self._graph)
