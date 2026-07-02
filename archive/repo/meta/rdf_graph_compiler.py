from rdflib import Graph, Namespace, Literal
from rdflib.namespace import RDF, XSD

FIN = Namespace("https://peculiarlibrarian.org/ontology/finance#")
CORE = Namespace("https://peculiarlibrarian.org/ontology/core#")
ORG = Namespace("https://peculiarlibrarian.org/ontology/organization#")

def compile_graph(rows):
    g = Graph()

    for r in rows:
        obs = FIN[f"obs-{r['fact_id']}"]
        res = FIN[f"res-{r['fact_id']}"]

        g.add((obs, RDF.type, FIN[r["type"]]))
        g.add((obs, FIN.observedEntity, ORG[r["entity"]]))
        g.add((obs, CORE.hasResult, res))
        g.add((res, FIN.amount, Literal(r["value"], datatype=XSD.decimal)))
        g.add((res, FIN.currency, Literal(r["currency"])))

    return g
