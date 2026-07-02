from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List
import yaml


@dataclass(frozen=True)
class Library:
    id: str
    version: str
    path: Path
    artifacts: Dict[str, Path]
    imports: List[Path]


class SemanticEngine:
    def __init__(self, repository: Path):
        self.repository = repository

    def discover(self) -> List[Library]:
        libraries = []

        for manifest in self.repository.glob("domains/**/library.yaml"):
            with open(manifest, "r", encoding="utf-8") as f:
                data = yaml.safe_load(f)

            root = manifest.parent

            artifacts = {
                key: root / value
                for key, value in data.get("artifacts", {}).items()
            }

            imports = [
                (root / item).resolve()
                for item in data.get("imports", [])
            ]

            libraries.append(
                Library(
                    id=data["id"],
                    version=data["version"],
                    path=root,
                    artifacts=artifacts,
                    imports=imports,
                )
            )

        return libraries
