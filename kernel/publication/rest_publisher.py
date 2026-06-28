import os
from flask import Flask, jsonify

from kernel.query_registry import QueryRegistry
from kernel.query_executor import QueryExecutor
from kernel.rdf_graph import RDFGraphClient

app = Flask(__name__)

graph = RDFGraphClient([
    "schemas/finance/knowledge/safaricom_revenue_observations.ttl",
    "schemas/finance/knowledge/safaricom_net_profit_observations.ttl",
    "schemas/finance/knowledge/safaricom_eps_observations.ttl",
    "schemas/finance/knowledge/safaricom_free_cash_flow_observations.ttl"
])

executor = QueryExecutor(graph)

@app.route("/", methods=["GET"])
def health():
    return jsonify({
        "service": "peculiarlibrarian-finance-api",
        "status": "ok",
        "endpoints": ["/api/query/10"]
    })

@app.route("/api/query/10", methods=["GET"])
def query_10():

    q = QueryRegistry.core("query_10")
    result = executor.run(q)

    # IMPORTANT: DO NOT CAST TYPES HERE
    return jsonify(result)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    app.run(host="127.0.0.1", port=port, debug=True, use_reloader=True)
