import json
from pathlib import Path


def load_canonical_facts(dataset_path: Path):
    """
    Generic canonical dataset loader.

    Loads authored facts without:
    - transformation
    - normalization
    - filtering
    """

    if not dataset_path.exists():
        raise FileNotFoundError(
            f"Missing dataset: {dataset_path}"
        )

    with open(dataset_path, "r") as f:
        data = json.load(f)

    if "facts" not in data:
        raise ValueError(
            "Invalid dataset: missing 'facts' key"
        )

    return data
