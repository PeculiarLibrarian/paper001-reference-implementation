"""
PADI Control Plane Manifest

This module defines the immutable contract for the control plane.

Any modification to these values constitutes a control-plane
revision and requires a version increment.
"""

CONTROL_PLANE_VERSION = "1.0.0"

PIPELINE_VERSION = "0.9.3"

CONTROL_PLANE_MODULES = (
    "audits",
    "ontology",
    "taxonomy",
    "shapes",
    "queries",
    "factory",
    "mappings",
    "ingestion",
    "ledger",
    "reasoning",
)

LOCKED_AUDITS = (
    "StructureAudit",
    "DependencyAudit",
    "ImportAudit",
    "RDFAudit",
    "SHACLAudit",
    "JenaAudit",
    "CompilerAudit",
    "MappingAudit",
    "DomainAudit",
    "ReasonerAudit",
)

IMMUTABLE_CONTRACTS = (
    "SemanticCompiler",
    "CanonicalMapper",
    "FactoryRegistry",
    "OntologyRegistry",
    "SemanticMaterializationLedger",
)

