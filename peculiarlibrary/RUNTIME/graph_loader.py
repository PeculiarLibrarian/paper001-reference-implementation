"""
PADI Graph Loader

Responsibility
--------------
Load a canonical graph from the graphstore.

Selection Policy
----------------
The graph loader never guesses.

If multiple graph snapshots exist, the newest snapshot
(by modification time) is selected deterministically.

Future versions may replace this policy with a signed
manifest or ledger pointer without changing callers.
"""

from pathlib import Path
from rdflib import Graph

from peculiarlibrary.RUNTIME.semantic_dataset import SemanticDataset


GRAPHSTORE = Path("peculiarlibrary/LIBRARIES/graphstore")


def discover_graph():
    files = sorted(
        GRAPHSTORE.glob("*.ttl"),
        key=lambda p: p.stat().st_mtime,
    )

    if not files:
        raise RuntimeError("Graphstore is empty.")

    # Deterministic selection policy
    return files[-1]


def load_full_graph():
    graph_file = discover_graph()

    g = Graph()
    g.parse(graph_file, format="turtle")

    return SemanticDataset(g)
