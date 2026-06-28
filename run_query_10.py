from kernel.query_registry import QueryRegistry
from kernel.query_executor import QueryExecutor
from kernel.rdf_graph import RDFGraphClient

# ----------------------------
# RDF GRAPH LOADING
# ----------------------------
graph = RDFGraphClient([
    "schemas/finance/knowledge/safaricom_revenue_observations.ttl",
    "schemas/finance/knowledge/safaricom_net_profit_observations.ttl",
    "schemas/finance/knowledge/safaricom_eps_observations.ttl",
    "schemas/finance/knowledge/safaricom_free_cash_flow_observations.ttl"
])

executor = QueryExecutor(graph)

# ----------------------------
# LOAD QUERY 10
# ----------------------------
query_path = QueryRegistry.finance("query_10")

# ----------------------------
# EXECUTE
# ----------------------------
result = executor.run(query_path)

print("\n=== QUERY 10: FINANCIAL SYNTHESIS OUTPUT ===\n")

for row in result:
    print({
        "year": str(row["year"]),
        "revenue": float(row["revenue"]),
        "net_profit": float(row["netProfit"]),
        "eps": float(row["eps"]),
        "fcf": float(row["fcf"]),
        "net_margin": float(row["netMargin"]),
        "fcf_conversion": float(row["fcfConversion"])
    })
