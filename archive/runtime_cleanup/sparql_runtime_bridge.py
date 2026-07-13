from peculiarlibrary.RUNTIME.graph_assembler import GraphAssembler
from peculiarlibrary.LEDGER.materialization_ledger import MaterializationLedger


def build_sparql_graph(runtime_graph):

    ledger = MaterializationLedger().load_graph()

    assembler = GraphAssembler(runtime_graph, ledger)

    return assembler.build()
