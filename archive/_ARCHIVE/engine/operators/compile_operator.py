from peculiarlibrary.ingestion.ingestion_pipeline import IngestionPipeline
from peculiarlibrary.compiler.canonical_compiler import CanonicalCompiler
from peculiarlibrary.runtime.semantic_dataset import SemanticDataset
from peculiarlibrary.reasoning.kpi_engine import KPIEngine
from peculiarlibrary.reasoning.cross_entity_reasoner import CrossEntityReasoner
from peculiarlibrary.validation.semantic_validator import SemanticValidator


class CompileOperator:
    """
    SINGLE PIPELINE ORCHESTRATOR

    Flow:
    Dataset → IngestionPipeline → CanonicalCompiler → RDF Graph → Runtime
    """

    def __init__(self):
        self.ingestion = IngestionPipeline()
        self.compiler = CanonicalCompiler()

    def execute(self, payload):
        dataset_path = payload["dataset"]

        # 1. LOAD KNOWLEDGE (PECULIARLIBRARY)
        package = self.ingestion.compile(dataset_path)

        # 2. COMPILE (PADI CONTROL PLANE - SINGLE ROUTE)
        graph = self.compiler.compile(package["data"]["facts"])

        # 3. VALIDATION
        validator = SemanticValidator(graph)

        # 4. RUNTIME LAYER
        runtime = {
            "multi_entity": SemanticDataset(graph),
            "cross_entity": CrossEntityReasoner(graph),
            "reasoning": KPIEngine(graph)
        }

        # 5. RETURN CANONICAL OUTPUT
        return {
            "integrity": {
                "fact_triples": len(list(graph)),
                "duplicates": validator.detect_duplicates(),
                "value_conflicts": validator.check_value_stability(),
                "multi_entity_enabled": True
            },
            "graph": graph,
            "runtime": runtime
        }
