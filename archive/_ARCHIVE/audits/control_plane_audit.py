from importlib import import_module
from pathlib import Path

from peculiarlibrary.audits.audit import Audit
from peculiarlibrary.audits.report import AuditReport

from peculiarlibrary.control_plane.manifest import (
    CONTROL_PLANE_VERSION,
    PIPELINE_VERSION,
    CONTROL_PLANE_MODULES,
    LOCKED_AUDITS,
    IMMUTABLE_CONTRACTS,
)
from peculiarlibrary.ingestion.ingestion_pipeline import SemanticCompiler


MODULE_PREFIX = "peculiarlibrary"

CONTRACT_IMPORTS = {
    "SemanticCompiler":
        "peculiarlibrary.ingestion.ingestion_pipeline",
    "CanonicalMapper":
        "peculiarlibrary.mappings.canonical_mapper",
    "FactoryRegistry":
        "peculiarlibrary.factory.core_factory",
    "OntologyRegistry":
        "peculiarlibrary.ontology.ontology_registry",
    "SemanticMaterializationLedger":
        "peculiarlibrary.ledger.materialization_ledger",
}

AUDIT_IMPORTS = {
    "StructureAudit":
        "peculiarlibrary.audits.structure_audit",
    "DependencyAudit":
        "peculiarlibrary.audits.dependency_audit",
    "ImportAudit":
        "peculiarlibrary.audits.import_audit",
    "RDFAudit":
        "peculiarlibrary.audits.rdf_audit",
    "SHACLAudit":
        "peculiarlibrary.audits.shacl_audit",
    "JenaAudit":
        "peculiarlibrary.audits.jena_audit",
    "CompilerAudit":
        "peculiarlibrary.audits.compiler_audit",
    "MappingAudit":
        "peculiarlibrary.audits.mapping_audit",
    "DomainAudit":
        "peculiarlibrary.audits.domain_audit",
    "ReasonerAudit":
        "peculiarlibrary.audits.reasoner_audit",
}


class ControlPlaneAudit(Audit):

    NAME = "Control Plane"

    def run(self):

        details = []

        if SemanticCompiler.VERSION != PIPELINE_VERSION:
            return AuditReport(
                self.NAME,
                False,
                "Pipeline version mismatch.",
                [
                    f"Compiler: {SemanticCompiler.VERSION}",
                    f"Manifest: {PIPELINE_VERSION}",
                ],
            )

        details.append(
            f"Control Plane Version: {CONTROL_PLANE_VERSION}"
        )

        details.append(
            f"Pipeline Version: {PIPELINE_VERSION}"
        )

        for module in CONTROL_PLANE_MODULES:

            path = Path(MODULE_PREFIX) / module

            if not path.exists():
                return AuditReport(
                    self.NAME,
                    False,
                    f"Missing control-plane module: {module}",
                    details,
                )

            import_module(f"{MODULE_PREFIX}.{module}")

        details.append(
            f"Modules validated: {len(CONTROL_PLANE_MODULES)}"
        )

        for contract in IMMUTABLE_CONTRACTS:

            module = CONTRACT_IMPORTS[contract]

            imported = import_module(module)

            if not hasattr(imported, contract):
                return AuditReport(
                    self.NAME,
                    False,
                    f"Missing immutable contract: {contract}",
                    details,
                )

        details.append(
            f"Contracts validated: {len(IMMUTABLE_CONTRACTS)}"
        )

        for audit in LOCKED_AUDITS:

            module = AUDIT_IMPORTS[audit]

            imported = import_module(module)

            if not hasattr(imported, audit):
                return AuditReport(
                    self.NAME,
                    False,
                    f"Missing audit: {audit}",
                    details,
                )

        details.append(
            f"Audits validated: {len(LOCKED_AUDITS)}"
        )

        return AuditReport(
            self.NAME,
            True,
            "Control plane locked and validated.",
            details,
        )


if __name__ == "__main__":

    report = ControlPlaneAudit().run()

    print(report.name)
    print(report.status)
    print(report.summary)

    for line in report.details:
        print("-", line)
