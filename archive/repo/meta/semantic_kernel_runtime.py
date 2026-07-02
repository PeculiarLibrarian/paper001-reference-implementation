from transaction_engine import TransactionEngine
from kernel_closure import GraphClosureValidator
from enforcement_runtime import SemanticEnforcementRuntimeV11
from rdf_graph_compiler import SafaricomProductionCompiler
import os

class SemanticKernelRuntime:

    def __init__(self, root="repo/"):
        self.root = root
        self.tx = TransactionEngine(root)
        self.closure = GraphClosureValidator(root)
        self.enforcer = SemanticEnforcementRuntimeV11(root)
        self.compiler = SafaricomProductionCompiler()

    def execute_transaction(self, fy, seed_rows):
        print("\n🧠 KERNEL START FY", fy)

        temp_file = self.tx.stage(fy, seed_rows)

        if not self.closure.execute_global_gate(temp_file):
            raise RuntimeError("Closure validation failed")

        final_path = os.path.join(
            self.root,
            f"instances/safaricom/fy{fy}_committed.ttl"
        )

        if not self.enforcer.commit_to_immutable_graph(
            temp_file,
            final_path,
            manifest={"fy": fy}
        ):
            raise RuntimeError("SHACL enforcement failed")

        print("🟢 COMMIT SUCCESS FY", fy)
        return True
