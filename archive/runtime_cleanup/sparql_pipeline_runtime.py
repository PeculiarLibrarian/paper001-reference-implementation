from rdflib import Graph
from peculiarlibrary.RUNTIME.graph_assembler import GraphAssembler
from peculiarlibrary.RUNTIME.semantic_graph_builder import SemanticGraphBuilder
from peculiarlibrary.LEDGER.materialization_ledger import MaterializationLedger
from pathlib import Path


def build_runtime_graph(runtime_graph: Graph) -> Graph:
    """
    FULL SEMANTIC PIPELINE:

    runtime → ledger → OWL → SKOS → SPARQL
    """

    # ledger fallback (graphstore safe)
    store = Path("peculiarlibrary/LEDGER/graphstore")
    ledger_graph = Graph()

    files = sorted(store.glob("*.ttl"))
    if files:
        ledger_graph.parse(str(files[-1]), format="turtle")

    # 1. assemble base factual layer
    assembler = GraphAssembler(runtime_graph, ledger_graph)
    unified = assembler.build()

    # 2. semantic enrichment layer (OWL + SKOS)
    builder = SemanticGraphBuilder(unified)
    enriched = builder.build()

    return enriched
