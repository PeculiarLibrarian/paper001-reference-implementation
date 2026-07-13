import json

def _serialize(obj):
    from rdflib import Graph

    if isinstance(obj, Graph):
        return {
            "__type__": "rdflib.Graph",
            "triples": len(obj)
        }

    return obj


class ExecutionNode:

    def __init__(self, data):
        self.data = data

    def hash(self):
        canonical = _serialize(self.data)
        return json.dumps(canonical, sort_keys=True).encode("utf-8")
