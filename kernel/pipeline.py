from orchestrator.orchestrator import Orchestrator

class SemanticPipeline:
    """
    Thin entrypoint only.
    No intelligence here.
    """

    def __init__(self, kernel):
        self.kernel = kernel
        self.orchestrator = kernel.orchestrator

    def run(self, ttl: str):
        return self.orchestrator.run(ttl)
