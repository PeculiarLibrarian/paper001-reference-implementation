import os
import json
import hashlib

class TransactionEngine:

    def __init__(self, root="repo/"):
        self.root = root
        self.staging = os.path.join(root, "staging/")
        os.makedirs(self.staging, exist_ok=True)

    def stage(self, fy, rows):
        batch_hash = hashlib.sha256(
            json.dumps(rows, sort_keys=True).encode()
        ).hexdigest()[:12]

        temp_file = os.path.join(
            self.staging,
            f"fy{fy}_{batch_hash}.ttl"
        )

        with open(temp_file, "w") as f:
            f.write(self._serialize(rows))

        return temp_file

    def _serialize(self, rows):
        return "\n".join([str(r) for r in rows])
