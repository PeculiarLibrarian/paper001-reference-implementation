"""
PADI Semantic Materialization Hash Policy
Version: 0.1.0

Purpose
-------
Generate deterministic semantic materialization identifiers.

The hash represents WHAT was materialized,
not WHEN it was materialized.
"""

import hashlib
import json


class HashPolicy:

    VERSION = "0.1.0"

    @staticmethod
    def materialization_id(
        *,
        compiler_version,
        mapper,
        dataset,
        commands,
    ):
        """
        Deterministic materialization hash.
        """

        payload = {
            "compiler_version": compiler_version,
            "mapper": mapper,
            "dataset": dataset,
            "commands": commands,
        }

        canonical = json.dumps(
            payload,
            sort_keys=True,
            separators=(",", ":"),
            default=str,
        )

        return hashlib.sha256(
            canonical.encode("utf-8")
        ).hexdigest()
