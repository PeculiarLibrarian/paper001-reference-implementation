from contracts.manager_contract import ManagerContract


class OpportunityEngine(ManagerContract):

    @property
    def name(self):
        return "OpportunityEngine"

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

    def load(self, instances=None):
        self.instances = instances

    def discover(self):

        ranked = []

        for opp in self.instances["opportunities"]:

            label = opp["label"]

            score = {
                "JobOpportunity": 0.60,
                "FellowshipOpportunity": 0.55,
                "ContractOpportunity": 0.45,
                "Opportunity": 0.30,
            }.get(label, 0.20)

            ranked.append({
                "opportunity": opp["uri"],
                "score": score,
                "explanation": f"{label} signal",
            })

        ranked.sort(
            key=lambda x: x["score"],
            reverse=True,
        )

        self.results = ranked

        return ranked

    def validate(self, payload):
        return isinstance(payload, list)

    def expose(self):
        return self.results

    def execute(self, instances):

        self.load(instances)

        payload = self.discover()

        if not self.validate(payload):
            raise RuntimeError("Opportunity validation failed")

        return payload
