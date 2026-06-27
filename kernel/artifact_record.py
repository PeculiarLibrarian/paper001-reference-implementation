from dataclasses import dataclass
from kernel.artifact_descriptor import ArtifactDescriptor


@dataclass(frozen=True)
class ArtifactRecord:

    descriptor: ArtifactDescriptor
    hash: str | None
    version: str
    implements_contract: str
    verified: bool
    contract_valid: bool
    missing_fields: list[str]
    layer: str
    produces: list[str]

    def identity(self):

        return self.descriptor.identity()

    def provenance(self):

        return {
            **self.identity(),
            "hash": self.hash,
            "version": self.version,
            "implements_contract": self.implements_contract,
            "verified": self.verified,
            "contract_valid": self.contract_valid,
            "missing_fields": self.missing_fields,
        }
