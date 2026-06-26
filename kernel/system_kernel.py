from orchestrator.orchestrator import Orchestrator

class SystemKernel:
    """
    Minimal kernel.
    No semantic managers.
    No reasoning layers.
    Pure orchestration of schema pipeline.
    """

    def __init__(self):
        self.orchestrator = Orchestrator()

    def run(self, ttl: str):
        return self.orchestrator.run(ttl)
