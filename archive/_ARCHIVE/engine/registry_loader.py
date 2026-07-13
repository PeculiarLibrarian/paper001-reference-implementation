import yaml
from pathlib import Path


def load_registry():
    """
    Loads operator registry YAML into runtime dict.
    No transformations. No enrichment. Deterministic only.
    """

    path = Path("peculiarlibrary/registry/operators.yaml")

    if not path.exists():
        raise FileNotFoundError(f"Registry not found: {path}")

    with path.open("r", encoding="utf-8") as f:
        raw = yaml.safe_load(f)

    # YAML structure is already {registry: {..., operators: {...}}}
    registry = raw.get("registry", raw)

    return registry
