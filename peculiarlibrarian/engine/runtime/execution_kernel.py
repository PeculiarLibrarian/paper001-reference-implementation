class ExecutionKernel:
    def __init__(self, replay=None):
        self.replay = replay
        self.dag = None
        self.graphs = {}
        self.ledger = None
