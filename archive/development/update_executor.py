from pathlib import Path

path = Path("peculiarlibrary/INFERENCE/inference_pipeline_executor.py")

text = path.read_text()

text = text.replace(
"""    def __init__(self):

        self.evidence_runtime = EvidenceRuntime()
        self.registry = build_rule_registry()
        self.assertion_builder = AssertionBuilder()
""",
"""    def __init__(self, registry=None):

        self.evidence_runtime = EvidenceRuntime()

        self.registry = (
            registry
            if registry is not None
            else build_rule_registry()
        )

        self.assertion_builder = AssertionBuilder()
"""
)

path.write_text(text)
