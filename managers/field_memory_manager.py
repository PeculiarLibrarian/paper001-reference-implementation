from contracts.manager_contract import ManagerContract


class FieldMemoryManager(ManagerContract):

    @property
    def name(self):
        return "FieldMemoryManager"

    def __init__(self):
        self.memory = {}

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
        self.memory = {
            "semantic_state": {},
            "reasoning_state": {},
            "opportunities": [],
            "explanations": [],
            "provenance": [],
            "runtime": {},
        }

    def discover(self):
        return self.memory

    def validate(self, payload):
        return isinstance(payload, dict)

    def expose(self):
        return self.memory

    def update(self, field, value):
        self.memory[field] = value

    def append(self, field, value):
        self.memory.setdefault(field, [])
        self.memory[field].append(value)

    def get(self, field):
        return self.memory.get(field)

    def execute(self):

        self.load()

        payload = self.discover()

        assert self.validate(payload)

        return self.expose()

