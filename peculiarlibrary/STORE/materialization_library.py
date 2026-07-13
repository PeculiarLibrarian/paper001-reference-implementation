from rdflib import Graph
from pathlib import Path
from datetime import datetime
import hashlib
import json


class MaterializationLedger:
    """
    Generic persistence layer.

    Responsibilities
    ----------------
    - Persist an RDF graph exactly as received.
    - Compute deterministic hash.
    - Write ledger entry.

    Non-responsibilities
    --------------------
    - No normalization.
    - No ontology rewriting.
    - No graph mutation.
    """

    def __init__(self):

        self.graphstore = Path("peculiarlibrary/LIBRARIES/graphstore")
        self.entries = Path("peculiarlibrary/LIBRARIES/entries")

        self.graphstore.mkdir(parents=True, exist_ok=True)
        self.entries.mkdir(parents=True, exist_ok=True)

    def persist(self, graph: Graph):

        if not isinstance(graph, Graph):
            raise TypeError("persist() expects rdflib.Graph")

        ttl = graph.serialize(format="turtle")

        if isinstance(ttl, bytes):
            ttl = ttl.decode()

        digest = hashlib.sha256(ttl.encode()).hexdigest()

        graph_file = self.graphstore / f"{digest}.ttl"
        graph_file.write_text(ttl)

        entry = {
            "hash": digest,
            "timestamp": datetime.utcnow().isoformat(),
            "graph": str(graph_file)
        }

        entry_file = self.entries / f"{digest}.json"
        entry_file.write_text(json.dumps(entry, indent=2))

        return entry
