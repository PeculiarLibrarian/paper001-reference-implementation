from dataclasses import dataclass
from typing import List


@dataclass
class ManagerContract:

    REQUIRED_METHODS: List[str] = (
        "discover",
        "load",
        "parse",
        "bind",
        "validate",
        "expose"
    )
