"""
Execution Ledger
Tamper-evident, hash-chained execution record system.
"""

import hashlib
import json
from copy import deepcopy


class ExecutionLedger:

    def __init__(self):
        self.chain = []
        self.previous_hash = "GENESIS"

    def _hash(self, data: dict) -> str:
        encoded = json.dumps(data, sort_keys=True).encode()
        return hashlib.sha256(encoded).hexdigest()

    def record(self, snapshot: dict):

        clean_snapshot = deepcopy(snapshot)

        block = {
            "index": len(self.chain),
            "snapshot": clean_snapshot,
            "previous_hash": self.previous_hash,
        }

        block_hash = self._hash(block)
        block["hash"] = block_hash

        self.chain.append(block)
        self.previous_hash = block_hash

        return block_hash

    def verify(self):

        prev_hash = "GENESIS"

        for i, block in enumerate(self.chain):

            expected = {
                "index": i,
                "snapshot": block["snapshot"],
                "previous_hash": prev_hash,
            }

            if self._hash(expected) != block["hash"]:
                return {
                    "valid": False,
                    "failed_at": i
                }

            prev_hash = block["hash"]

        return {"valid": True, "length": len(self.chain)}

    def export(self):
        return deepcopy(self.chain)
