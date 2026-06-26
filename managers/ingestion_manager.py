from contracts.manager_contract import ManagerContract


class IngestionManager(ManagerContract):

    @property
    def name(self):
        return "IngestionManager"

    def __init__(self):
        self.payload = {}

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

    def load(self):
        self.payload = {}

    def discover(self):
        return self.payload

    def validate(self, payload):
        return isinstance(payload, dict)

    def expose(self):
        return self.payload

    def ingest(self, source):

        self.payload = {
            "person": source.get("person", {}),
            "competencies": source.get("competencies", []),
            "projects": source.get("projects", []),
            "repositories": source.get("repositories", []),
            "publications": source.get("publications", []),
            "organizations": source.get("organizations", []),
            "evidence": source.get("evidence", []),
        }

        return self.payload

    def execute(self):

        self.load()

        payload = self.discover()

        assert self.validate(payload)

        return self.expose()

