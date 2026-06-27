from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class ArtifactDescriptor:

    artifact_type: str
    name: str
    path: Path

    @property
    def exists(self):
        return self.path.exists()

    @property
    def extension(self):
        return self.path.suffix

    def identity(self):
        return {
            "artifact_id": self.name,
            "display_name": self.name,
            "artifact_kind": "python_module",
            "runtime_role": self.artifact_type,
            "path": str(self.path),
            "exists": self.exists,
            "extension": self.extension,
        }
