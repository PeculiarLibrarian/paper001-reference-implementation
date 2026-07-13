from __future__ import annotations

import hashlib
import json
import platform
import uuid

from copy import deepcopy
from datetime import UTC, datetime
from pathlib import Path

from rdflib import Graph


class MaterializationLedger:
    """
    Persistent system memory.

    Runtime Graph  ---> GraphStore
                          |
                          v
                 MaterializationLedger
                          |
                          +--> graphstore/<sha>.ttl
                          +--> ledger/<timestamp>.json
    """

    VERSION = "4.0.0"

    def __init__(
        self,
        ledger_dir="peculiarlibrary/ledger/entries",
        graph_dir="peculiarlibrary/graphstore",
    ):
        self.ledger_dir = Path(ledger_dir)
        self.graph_dir = Path(graph_dir)

        self.ledger_dir.mkdir(parents=True, exist_ok=True)
        self.graph_dir.mkdir(parents=True, exist_ok=True)

    def materialize(
        self,
        *,
        state,
        graph: Graph,
        integrity,
    ):

        if not isinstance(graph, Graph):
            raise TypeError("materialize() expects an rdflib.Graph")

        timestamp = (
            datetime.now(UTC)
            .replace(microsecond=0)
            .isoformat()
            .replace("+00:00", "Z")
        )

        ttl = graph.serialize(format="turtle")

        graph_hash = hashlib.sha256(
            ttl.encode("utf-8")
        ).hexdigest()

        graph_path = self.graph_dir / f"{graph_hash}.ttl"

        if not graph_path.exists():
            graph_path.write_text(ttl, encoding="utf-8")

        compile_state = deepcopy(state.get("compile", {}))
        reason_state = deepcopy(state.get("reason", {}))

        reason_state.pop("graph", None)
        reason_state.pop("graph_hash", None)

        fingerprint_payload = {
            "compile": compile_state,
            "reason": reason_state,
            "integrity": integrity,
            "graph_sha256": graph_hash,
            "runtime_version": self.VERSION,
        }

        fingerprint = hashlib.sha256(
            json.dumps(
                fingerprint_payload,
                sort_keys=True,
                default=str,
            ).encode("utf-8")
        ).hexdigest()

        entry = {
            "ledger_id": str(uuid.uuid4()),
            "timestamp": timestamp,
            "dataset": compile_state.get("dataset"),
            "compile": compile_state,
            "reason": reason_state,
            "integrity": deepcopy(integrity),
            "artifacts": {
                "graph": {
                    "sha256": graph_hash,
                    "format": "turtle",
                    "location": str(graph_path),
                    "triples": len(graph),
                }
            },
            "runtime": {
                "version": self.VERSION,
                "python": platform.python_version(),
            },
            "execution": {
                "fingerprint": fingerprint,
                "operator_count": len(state),
            },
        }

        filename = timestamp.replace(":", "-") + ".json"

        with (self.ledger_dir / filename).open(
            "w",
            encoding="utf-8",
        ) as f:
            json.dump(entry, f, indent=2)

        return entry

    def load_graph(self, graph_hash):

        path = self.graph_dir / f"{graph_hash}.ttl"

        if not path.exists():
            raise FileNotFoundError(graph_hash)

        g = Graph()
        g.parse(path, format="turtle")

        return g

    def latest(self):

        files = sorted(self.ledger_dir.glob("*.json"))

        if not files:
            return None

        with files[-1].open(encoding="utf-8") as f:
            return json.load(f)

    def history(self):
        return sorted(
            p.name
            for p in self.ledger_dir.glob("*.json")
        )

    def snapshot(self):
        return {
            "entries": len(self.history()),
            "latest": self.latest(),
        }

    def stats(self):

        history = self.history()

        valid = 0

        for name in history:
            with (self.ledger_dir / name).open(
                encoding="utf-8"
            ) as f:
                if json.load(f)["integrity"]["valid"]:
                    valid += 1

        return {
            "entries": len(history),
            "valid": valid,
            "invalid": len(history) - valid,
        }
