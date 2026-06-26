from typing import Dict, Any


class RuntimeBootstrapContract:
    """
    Defines system bootstrap state.

    This resolves DAG ambiguity by ensuring a shared root context exists.
    """

    BOOTSTRAP_STATE: Dict[str, Any] = {
        "graph": "available",
        "instances": "available",
        "core": "available",
    }
