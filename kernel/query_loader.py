from kernel.query_registry import QueryRegistry

class QueryLoader:

    @staticmethod
    def run(query_id: str):
        """
        Executes a registered financial query from the query registry.
        """

        query = QueryRegistry.get(query_id)

        if query is None:
            raise ValueError(f"Query not found: {query_id}")

        # For now we return structured metadata
        # (execution engine will be plugged in next stage)

        return {
            "query_id": query_id,
            "description": getattr(query, "description", None),
            "metrics": getattr(query, "usesMetric", None),
            "status": "REGISTERED_BUT_NOT_EXECUTED",
            "note": "Execution engine not yet attached"
        }
