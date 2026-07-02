from peculiarlibrary.ingestion.ingestion_pipeline import SemanticCompiler
from peculiarlibrary.mappings.safaricom_mapper import SafaricomMapper
from peculiarlibrary.validation.shacl_validator import SHACLValidator
from peculiarlibrary.reasoning.inference_engine import InferenceEngine


def run(name):
    compiler = SemanticCompiler(
        mapper=SafaricomMapper(),
        doctrine_enforcer=None,
        shacl_validator=SHACLValidator(),
    )

    graph = compiler.compile(name)

    # inference is post-process, not constructor dependency
    engine = InferenceEngine(graph)
    engine.run()

    print("\n✔ RDF GRAPH GENERATED")
    return graph


if __name__ == "__main__":
    import sys
    run(sys.argv[1])
