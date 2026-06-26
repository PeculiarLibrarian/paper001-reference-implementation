from rdflib import URIRef


class CompetencyNormalizer:

    def normalize(self, graph):

        normalized = set()

        mapping = {}

        for s, p, o in graph:

            s = URIRef(s)
            p = URIRef(p)
            o = URIRef(o)

            # -----------------------------
            # NORMALIZE COMPETENCY SPACE
            # -----------------------------
            if "Capability" in str(o):

                canonical = str(o).replace("Capability", "Competency")

                mapping[str(o)] = canonical

                normalized.add((s, p, URIRef(canonical)))

            elif "Competency" in str(o):

                normalized.add((s, p, o))

            else:

                normalized.add((s, p, o))

        # rebuild graph-compatible iterable
        graph.__iter__ = lambda: iter(normalized)

        return graph
