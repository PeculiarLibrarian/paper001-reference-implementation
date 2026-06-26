from rdflib import RDF, OWL


class InstanceManager:

    def load(self):
        pass

    def execute(self, context=None):

        graph = context.get("graph") if isinstance(context, dict) else None

        if graph is None:
            raise ValueError("InstanceManager requires 'graph' in context")

        instances = []

        for uri in graph.subjects(RDF.type, OWL.Class):

            if "Opportunity" not in str(uri):
                continue

            instances.append({
                "uri": str(uri),
                "label": self._label(graph, uri),
            })

        # 🔥 CRITICAL FIX: match contract
        return {
            "instances": {
                "opportunities": instances
            }
        }

    def _label(self, graph, uri):
        from rdflib.namespace import RDFS

        for _, _, label in graph.triples((uri, RDFS.label, None)):
            return str(label)

        return uri.split("/")[-1]
