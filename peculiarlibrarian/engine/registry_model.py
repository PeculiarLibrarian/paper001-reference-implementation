import yaml
from pathlib import Path

REGISTRY_PATH = Path(__file__).parent.parent / "registry" / "operators.yaml"

with open(REGISTRY_PATH, "r") as f:
    RAW = yaml.safe_load(f)

REGISTRY = RAW

def get_operator(name: str):
    return REGISTRY["operators"][name]

def get_handler_spec(name: str):
    op = get_operator(name)
    return {
        "module": op["module"],
        "class": op["class"],
        "stage": op["stage"]
    }
