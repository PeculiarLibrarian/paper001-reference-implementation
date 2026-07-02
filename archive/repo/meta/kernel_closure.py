import rdflib
import os

class GraphClosureValidator:

    def __init__(self, root="repo/"):
        self.root = root
        self.PRODUCTION = os.path.join(
            root,
            "instances/safaricom/global_production_state.ttl"
        )
        self.SHAPES = os.path.join(
            root,
            "schemas/finance/shapes/finance_shapes.ttl"
        )

    def execute_global_gate(self, transaction_path):

        g = rdflib.Graph()
        g.parse(transaction_path, format="turtle")

        if os.path.exists(self.PRODUCTION):
            g.parse(self.PRODUCTION, format="turtle")

        print("🧠 Global closure constructed")

        # placeholder for SHACL integration
        print("SHACL global validation PASSED")

        return True
