from rdflib.namespace import RDF, RDFS, OWL

from contracts.manager_contract import ManagerContract


class InstanceManager(ManagerContract):

    def __init__(self):
        self.instances = {}

    @property
    def name(self):
        return "InstanceManager"

    def handshake(self):
        return {
            "manager": self.name,
            "version": "1.0",
            "contract": "manager_contract",
            "capabilities": [
                "load",
                "discover",
                "validate",
                "expose",
                "execute",
            ],
        }

    def load(self, graph=None):
        self.graph = graph

    def discover(self):

        opportunities = []

        for subject, _, obj in self.graph.triples((None, RDF.type, OWL.Class)):
            uri = str(subject)

            if uri.endswith("Opportunity") or "Opportunity" in uri:
                opportunities.append({
                    "uri": uri,
                    "label": uri.rsplit("/", 1)[-1]
                })

        self.instances = {
            "person_competencies": {},
            "opportunities": opportunities,
        }

        return self.instances

    def validate(self, payload):
        return isinstance(payload, dict)

    def expose(self):
        return self.instances

    def execute(self, graph):
        self.load(graph)
        payload = self.discover()

        if not self.validate(payload):
            raise RuntimeError("Instance validation failed")

        return payload
