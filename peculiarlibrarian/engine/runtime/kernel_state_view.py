"""
Kernel State View (Canonical Runtime Contract)
Version: 1.0.0

Single deterministic external representation of runtime state.
"""

class KernelStateView:

    def __init__(self, kernel, replay):
        self.kernel = kernel
        self.replay = replay

    def graphs(self):
        return self.kernel.graphs.summary()

    def dag(self):
        return self.kernel.dag.snapshot()

    def ledger_size(self):
        return len(self.kernel.ledger.graph)

    def replay_state(self):
        return {
            "chain": self.replay.export().get("chain", []),
            "snapshots": self.replay.export().get("snapshots", []),
        }

    def integrity(self):
        return self.replay.verify()

    def trace(self):
        return self.kernel.dag.snapshot().get("nodes", {})

    def materialized(self):
        return {
            "graphs": self.graphs(),
            "dag": self.dag(),
            "ledger_triples": self.ledger_size(),
        }

    def export(self):
        return {
            "graphs": self.graphs(),
            "dag": self.dag(),
            "ledger_triples": self.ledger_size(),
            "replay": self.replay_state(),
            "integrity": self.integrity(),
            "trace": list(self.trace().keys()),
        }
