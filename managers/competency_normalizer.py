from contracts.manager_contract import ManagerContract
from managers.canonicalization_manager import CanonicalizationManager


class CompetencyNormalizer(ManagerContract):

    @property
    def name(self):
        return "CompetencyNormalizer"

    def __init__(self):
        self.canonicalizer = CanonicalizationManager()

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
        self.canonicalizer.execute()

    def discover(self):
        return self.canonicalizer.expose()

    def validate(self, payload):
        return len(payload) > 0

    def expose(self):
        return self.canonicalizer.expose()

    def normalize(self, competency):
        return self.canonicalizer.canonicalize(competency)

    def execute(self):
        self.load()
        payload = self.discover()
        assert self.validate(payload)
        return self.expose()

