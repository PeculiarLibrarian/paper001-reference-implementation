"""
PADI Semantic Reasoner
Version: 1.0.0

SPARQL-based deterministic reasoning layer over the Semantic Dataset.
"""

from rdflib import Graph


class SemanticReasoner:

    VERSION = "1.0.0"

    def __init__(self, graph: Graph):
        self.graph = graph

    # -------------------------------------------------
    # CORE QUERY EXECUTOR
    # -------------------------------------------------

    def query(self, sparql: str):
        return list(self.graph.query(sparql))

    # -------------------------------------------------
    # HIGH-LEVEL SEMANTIC QUERIES
    # -------------------------------------------------

    def facts_by_entity(self, entity_uri: str):
        return self.query(f"""
            SELECT ?fact ?metric ?value ?period
            WHERE {{
                ?fact <http://padi.s.m.gitandu.bs/core#aboutEntity> <{entity_uri}> ;
                      <http://padi.s.m.gitandu.bs/core#hasMetric> ?metric ;
                      <http://padi.s.m.gitandu.bs/core#factValue> ?value ;
                      <http://padi.s.m.gitandu.bs/core#reportingPeriod> ?period .
            }}
        """)

    def facts_by_metric(self, metric_uri: str):
        return self.query(f"""
            SELECT ?fact ?entity ?value ?period
            WHERE {{
                ?fact <http://padi.s.m.gitandu.bs/core#hasMetric> <{metric_uri}> ;
                      <http://padi.s.m.gitandu.bs/core#aboutEntity> ?entity ;
                      <http://padi.s.m.gitandu.bs/core#factValue> ?value ;
                      <http://padi.s.m.gitandu.bs/core#reportingPeriod> ?period .
            }}
        """)

    def time_series(self, entity_uri: str, metric_uri: str):
        return self.query(f"""
            SELECT ?period ?value
            WHERE {{
                ?fact <http://padi.s.m.gitandu.bs/core#aboutEntity> <{entity_uri}> ;
                      <http://padi.s.m.gitandu.bs/core#hasMetric> <{metric_uri}> ;
                      <http://padi.s.m.gitandu.bs/core#factValue> ?value ;
                      <http://padi.s.m.gitandu.bs/core#reportingPeriod> ?period .
            }}
            ORDER BY ?period
        """)
