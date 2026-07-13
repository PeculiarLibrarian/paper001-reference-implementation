"""
PADI Runtime Executor

Version: 3.0.0

Deterministic execution boundary over the Canonical Semantic Runtime.

Responsibilities
----------------
- Consume immutable SemanticDataset.
- Delegate analytical operations.
- Expose query services to OperatorRuntime.
- Keep execution separate from governance.

Non-responsibilities
--------------------
- No disk loading.
- No graph rebuilding.
- No SHACL execution.
- No constitution execution.
- No finality sealing.
"""

from peculiarlibrary.RUNTIME.query_runtime import QueryRuntime


class RuntimeExecutor:
    """
    Runtime service façade.

    Input:
        SemanticDataset

    Output:
        Deterministic runtime operations.
    """

    VERSION = "3.0.0"

    def __init__(self, dataset):
        self.dataset = dataset
        self.query_runtime = QueryRuntime(dataset)

    @property
    def records(self):
        return self.query_runtime.records

    def compare(self, metric):
        return self.query_runtime.compare(metric)

    def rank(self, metric):
        return self.query_runtime.rank(metric)

    def time_series(self, entity, metric):
        return self.query_runtime.time_series(
            entity,
            metric,
        )

    def growth_strength(self, entity, metric):
        return self.query_runtime.growth_strength(
            entity,
            metric,
        )

    def health_score(self, entity, metric):
        return self.query_runtime.health_score(
            entity,
            metric,
        )
