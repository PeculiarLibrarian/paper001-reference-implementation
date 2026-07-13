"""
Trace Guard
Ensures execution trace integrity.
"""

from peculiarlibrarian.engine.runtime.execution_invariants import ExecutionInvariants


class TraceGuard:

    @staticmethod
    def validate(trace):
        return ExecutionInvariants.is_valid_pipeline(trace)
