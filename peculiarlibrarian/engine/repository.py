from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List

import yaml

from .core import Library


@dataclass(frozen=True)
class Constitution:
    ontology: List[Path]
    taxonomy: List[Path]
    shapes: List[Path]
    queries: List[Path]
    context: List[Path]


@dataclass(frozen=True)
class Repository:
    id: str
    version: str
    root: Path
    constitution: Constitution
    libraries: List[Library]


def load_repository(root: Path) -> Repository:
    manifest = root / "peculiarlibrarian.yaml"

    with open(manifest, "r", encoding="utf-8") as f:
        spec = yaml.safe_load(f)

    constitution = spec["constitution"]

    def resolve(section):
        return [
            (root / p).resolve()
            for p in constitution.get(section, [])
        ]

    const = Constitution(
        ontology=resolve("ontology"),
        taxonomy=resolve("taxonomy"),
        shapes=resolve("shapes"),
        queries=resolve("queries"),
        context=resolve("context"),
    )

    libraries = []

    for library_manifest in root.glob("domains/**/library.yaml"):
        with open(library_manifest, "r", encoding="utf-8") as f:
            data = yaml.safe_load(f)

        library_root = library_manifest.parent

        artifacts = {
            k: library_root / v
            for k, v in data["artifacts"].items()
        }

        libraries.append(
            Library(
                id=data["id"],
                version=data["version"],
                path=library_root,
                artifacts=artifacts,
                imports=[],
            )
        )

    libraries.sort(key=lambda l: l.id)

    return Repository(
        id=spec["id"],
        version=spec["version"],
        root=root.resolve(),
        constitution=const,
        libraries=libraries,
    )
