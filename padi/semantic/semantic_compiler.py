from rdflib import Graph, URIRef, Literal


class SemanticCompiler:
    """
    Deterministic normalization layer.

    Dataset package → RDF-ready graph + CanonicalFacts

    PADI owns semantic compilation.
    Ingestion belongs to the execution layer.
    """

    def __init__(self):
        pass

    def compile(self, package):

        graph = Graph()
        facts = []
        triples_count = 0

        if package["__type__"] == "json.dataset":

            raw = package["data"].get(
                "facts",
                package["data"]
            )

            for item in raw:
                try:
                    s = URIRef(
                        f"http://padi.s.m.gitandu.bs/entity/{item['subject'].replace(' ', '_')}"
                    )

                    p = URIRef(
                        f"http://padi.s.m.gitandu.bs/metric/{item['predicate']}"
                    )

                    value = item["object"]

                    if isinstance(value, (dict, list)):
                        continue

                    o = Literal(value)

                    graph.add((s, p, o))

                    facts.append(
                        {
                            "subject": str(s),
                            "predicate": str(p),
                            "object": value,
                            "period": item.get("period"),
                            "confidence": item.get(
                                "confidence",
                                1.0
                            )
                        }
                    )

                    triples_count += 1

                except Exception:
                    continue

        elif package["__type__"] == "rdf.dataset":

            graph = package["graph"]
            triples_count = len(graph)

        return {
            "__type__": "compiled.graph",
            "graph": graph,
            "facts": facts,
            "triples": triples_count
        }
