"""
RDF Execution Ledger
Converts execution DAG into SPARQL-queryable RDF graph.
"""

from rdflib import Graph, URIRef, Literal, Namespace
from rdflib.namespace import RDF

PADI = Namespace("http://padi.engine/runtime#")


class RDFExecutionLedger:

    def __init__(self):
        self.graph = Graph()
        self.graph.bind("padi", PADI)

    def materialize_node(self, node_hash: str, node: dict):
        subject = URIRef(f"http://padi.engine/node/{node_hash}")

        self.graph.add((subject, PADI.hash, Literal(node_hash)))
        self.graph.add((subject, PADI.operator, Literal(node["operator"])))
        self.graph.add((subject, PADI.stage, Literal(node["stage"])))

        if node.get("parent"):
            self.graph.add((subject, PADI.parent, Literal(node["parent"])))

    def ingest_dag(self, dag_snapshot: dict):
        for node_hash, node in dag_snapshot["nodes"].items():
            self.materialize_node(node_hash, node)

    def query(self, sparql: str):
        return self.graph.query(sparql)

    def serialize(self, format="turtle"):
        return self.graph.serialize(format=format)
