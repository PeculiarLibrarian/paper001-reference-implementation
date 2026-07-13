"""
PADI Execution Plane Manifest
=============================

Version: 1.0.0
Status : LOCKED

Defines the immutable execution layer of the PADI Kernel.
"""

EXECUTION_PLANE_VERSION = "1.0.0"

PIPELINE_VERSION = "0.9.3"

LOCKED_MODULES = (
    "execution_plan",
    "execution_context",
    "planner",
    "runtime",
    "orchestrator",
)

IMMUTABLE_CONTRACTS = (
    "ExecutionPlan",
    "ExecutionStep",
    "ExecutionResult",
    "ExecutionContext",
    "ExecutionRuntime",
)

LOCKED_STAGES = (
    "compile",
    "reason",
)

EXECUTION_SEQUENCE = (
    "compile",
    "reason",
)

FORBIDDEN_BYPASSES = (
    "SemanticCompiler",
    "InferenceEngine",
)

RUNTIME_INVARIANTS = (
    "Deterministic execution",
    "Immutable execution plan",
    "Single execution context",
    "Ordered stage execution",
    "Execution result provenance",
)

__all__ = [
    "EXECUTION_PLANE_VERSION",
    "PIPELINE_VERSION",
    "LOCKED_MODULES",
    "IMMUTABLE_CONTRACTS",
    "LOCKED_STAGES",
    "EXECUTION_SEQUENCE",
    "FORBIDDEN_BYPASSES",
    "RUNTIME_INVARIANTS",
]
