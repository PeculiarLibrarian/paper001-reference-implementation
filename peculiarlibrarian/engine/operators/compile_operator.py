from peculiarlibrary.ingestion.ingestion_pipeline import SemanticCompiler
from peculiarlibrary.mappings.canonical_mapper import CanonicalMapper
from peculiarlibrary.ingestion.doctrine_enforcer import DoctrineEnforcer
from peculiarlibrary.validation.shacl_validator import SHACLValidator


class CompileOperator:

    VERSION = "1.0.0"

    def execute(self, payload: dict):

        dataset = payload.get("dataset")

        compiler = SemanticCompiler()
        mapper = CanonicalMapper()
        enforcer = DoctrineEnforcer()
        validator = SHACLValidator()

        graph = compiler.compile(dataset)
        graph = mapper.map(graph)
        graph = enforcer.enforce(graph)

        report = validator.validate(graph)

        return {
            "status": "compiled",
            "graph": graph,
            "triples": len(graph),
            "dataset": dataset,
            "validation": str(report),
        }
