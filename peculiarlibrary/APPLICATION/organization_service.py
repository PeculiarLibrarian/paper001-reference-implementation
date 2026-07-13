"""
PADI Technical Standard

Organization Service

Purpose
-------
Application boundary for validated organizational
knowledge supplied by the KOM runtime.
"""

from peculiarlibrary.RUNTIME.runtime_executor import (
    run_finalized_runtime,
)


class OrganizationService:
    """
    Canonical organization service.

    Delegates knowledge acquisition to KOM Runtime.
    """

    def get_validated_knowledge(self) -> dict:
        """
        Execute KOM runtime and return sealed result.
        """

        runtime_result = run_finalized_runtime()

        return runtime_result
