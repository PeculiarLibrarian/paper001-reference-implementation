from flask import Flask, jsonify
from pathlib import Path

from kernel.rdf_graph import RDFGraphClient
from kernel.query_executor import QueryExecutor
from kernel.manifest_registry import ManifestRegistry
from kernel.semantic.query_10_engine import Query10SemanticEngine

app = Flask(__name__)


def build_graph():
    ttl_files = sorted(
        str(p)
        for p in Path("schemas").rglob("*.ttl")
    )
    return RDFGraphClient(ttl_files)


graph = build_graph()
executor = QueryExecutor(graph)


@app.get("/")
def index():
    return jsonify({
        "status": "ok",
        "service": "peculiarlibrarian-finance-api",
        "queries": ManifestRegistry.discover()
    })


@app.get("/api/query/10")
def query10():

    manifest = ManifestRegistry.load(
        "finance",
        "query_10"
    )

    sparql = (
        ManifestRegistry
        .manifest("finance", "query_10")
        .parent
        / manifest["entrypoint"]
    )

    raw = executor.run(sparql)

    result = Query10SemanticEngine(raw).execute()

    return jsonify(result)


if __name__ == "__main__":
    app.run(
        host="127.0.0.1",
        port=8000,
        debug=True,
    )
