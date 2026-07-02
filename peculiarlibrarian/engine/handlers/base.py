from abc import ABC, abstractmethod
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class Artifact:
    artifact_type: str
    path: Path
    library_id: str
    version: str


class ArtifactHandler(ABC):

    @abstractmethod
    def handle(self, artifact: Artifact):
        raise NotImplementedError
