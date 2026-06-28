from kernel.query_registry import QueryRegistry
from kernel.query_executor import QueryExecutor
from kernel.rdf_graph import RDFGraphClient

graph = RDFGraphClient([
    "schemas/finance/knowledge/safaricom_revenue_observations.ttl",
    "schemas/finance/knowledge/safaricom_net_profit_observations.ttl",
    "schemas/finance/knowledge/safaricom_eps_observations.ttl",
    "schemas/finance/knowledge/safaricom_free_cash_flow_observations.ttl"
])

executor = QueryExecutor(graph)

query_path = QueryRegistry.core("query_10")

result = executor.run(query_path)

print("\n=== OFFLINE QUERY 10 TEST ===\n")

for r in result:
    print(r)
