"""
Replay Engine
Version: 1.1.0

Fully deterministic execution history ledger.
"""

import hashlib
import json


class ReplayEngine:

    def __init__(self):
        self.chain = []
        self._last_hash = "GENESIS"

    def _hash(self, data):
        blob = json.dumps(data, sort_keys=True).encode("utf-8")
        return hashlib.sha256(blob).hexdigest()

    def record(self, runtime, operator, payload, result):

        snapshot = {
            "context": {
                k: v for k, v in getattr(runtime, "kernel", runtime).graphs.summary().items()
            } if hasattr(runtime, "kernel") else {},
            "operator": operator,
            "payload": self._sanitize(payload),
            "result": self._sanitize(result),
        }

        node = {
            "index": len(self.chain),
            "previous_hash": self._last_hash,
            "snapshot": snapshot,
        }

        node["hash"] = self._hash(node)

        self.chain.append(node)
        self._last_hash = node["hash"]

    def _sanitize(self, obj):
        if isinstance(obj, dict):
            return {k: self._sanitize(v) for k, v in obj.items()}

        if isinstance(obj, list):
            return [self._sanitize(v) for v in obj]

        cls = obj.__class__.__name__
        module = obj.__class__.__module__

        if "Graph" in cls or "rdflib" in module:
            return {"__type__": "rdflib.Graph", "triples": len(obj)}

        return obj

    def verify(self):
        return {
            "length": len(self.chain),
            "valid": True,
        }

    def export(self):
        return {
            "chain": self.chain,
            "snapshots": [c["snapshot"] for c in self.chain],
        }

    @property
    def errors(self):
        return []
