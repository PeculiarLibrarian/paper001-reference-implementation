from rdflib import URIRef


class CompetencyInferenceManager:

    def infer(self, graph):

        inferred_edges = []

        for s, p, o in list(graph):

            s = str(s)
            p = str(p)
            o = str(o)

            # -----------------------------
            # TAXONOMY ALIGNMENT RULE
            # -----------------------------
            if "Competency" in s and "Capability" in o:

                inferred_edges.append((
                    URIRef(s),
                    URIRef("https://peculiarlibrarian.org/ontology/hasCompetency"),
                    URIRef(o)
                ))

            if "Opportunity" in s and "Competency" in o:

                inferred_edges.append((
                    URIRef(s),
                    URIRef("https://peculiarlibrarian.org/ontology/requiresCompetency"),
                    URIRef(o)
                ))

        for edge in inferred_edges:
            graph.add(edge)

        return graph
