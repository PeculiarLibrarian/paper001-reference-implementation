from rdflib import URIRef, RDF, Namespace

PL = Namespace("https://peculiarlibrarian.org/ontology/")


class InstanceManager:

    def discover(self):
        self.assets = []

    def load(self):
        self.instances = {}

    def parse(self):
        return self.instances

    def bind(self, context):
        context["instances"] = self.instances
        return context

    def validate(self, context):
        return True

    def expose(self):
        return self.instances

    def materialize_into_graph(self, graph):

        for s, p, o in list(graph):

            # ALWAYS convert safely
            s_uri = URIRef(str(s))
            p_uri = URIRef(str(p)) if str(p).startswith("http") else None
            o_uri = URIRef(str(o)) if str(o).startswith("http") else None

            # -------------------------
            # ONLY TYPE ASSERTIONS
            # -------------------------
            if "Competency" in str(s):
                graph.add((s_uri, RDF.type, PL.Person))

            if "CapabilityRegistry" in str(s):
                graph.add((s_uri, RDF.type, PL.Opportunity))

        return graph
