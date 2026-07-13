import json
from pathlib import Path


def load_facts():

    path = Path(__file__).with_name("canonical_facts.json")

    with open(path, "r") as f:
        return json.load(f)
