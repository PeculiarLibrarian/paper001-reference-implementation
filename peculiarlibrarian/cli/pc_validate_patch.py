from peculiarlibrary.engine.validation.compile_validation import CompileValidation


def validate_result(result):
    validator = CompileValidation()
    report = validator.validate(result)

    print("\n======================")
    print("SYSTEM VALIDATION")
    print("======================")

    if report["valid"]:
        print("STATUS: ✅ VALID")
    else:
        print("STATUS: ❌ INVALID")
        for e in report["errors"]:
            print("ERROR:", e)

    print("\nGRAPH SIZE:", report["graph_size"])
    print("FACT TRIPLES:", report["fact_triples"])
    print("SEMANTIC TRIPLES:", report["semantic_triples"])

    return report["valid"]
