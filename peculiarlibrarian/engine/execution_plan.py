from dataclasses import dataclass
from pathlib import Path
from typing import List

from .handlers.base import Artifact
from .repository import Repository


@dataclass(frozen=True)
class ExecutionPlan:
    artifacts: List[Artifact]


def build_execution_plan(repository: Repository) -> ExecutionPlan:
    """
    Build a deterministic execution plan.

    Order:
      1. Constitutional artifacts
      2. Domain library artifacts (alphabetical by library id)
    """

    artifacts = []

    #
    # Constitution first
    #

    for path in repository.constitution.ontology:
        artifacts.append(
            Artifact("ontology", path, "constitution", repository.version)
        )

    for path in repository.constitution.taxonomy:
        artifacts.append(
            Artifact("taxonomy", path, "constitution", repository.version)
        )

    for path in repository.constitution.shapes:
        artifacts.append(
            Artifact("shapes", path, "constitution", repository.version)
        )

    for path in repository.constitution.queries:
        artifacts.append(
            Artifact("queries", path, "constitution", repository.version)
        )

    for path in repository.constitution.context:
        artifacts.append(
            Artifact("context", path, "constitution", repository.version)
        )

    #
    # Libraries
    #

    order = (
        "ontology",
        "taxonomy",
        "shapes",
        "queries",
        "context",
    )

    for library in repository.libraries:
        for artifact_type in order:
            path = library.artifacts.get(artifact_type)

            if path is not None:
                artifacts.append(
                    Artifact(
                        artifact_type,
                        path.resolve(),
                        library.id,
                        library.version,
                    )
                )

    return ExecutionPlan(artifacts)
