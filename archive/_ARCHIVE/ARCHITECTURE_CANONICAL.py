from pathlib import Path

CANONICAL = {
    "data",
    "rdf/owl",
    "skos",
    "shacl",
    "ledger",
    "sparql",
    "runtime",
    "kpi_engine"
}

def validate(root="peculiarlibrary"):
    root = Path(root)

    actual = {p.relative_to(root).as_posix() for p in root.rglob("*") if p.is_dir()}

    top = {p.name.lower() for p in root.iterdir() if p.is_dir()}

    print("EXPECTED:", CANONICAL)
    print("ACTUAL TOP:", top)

    missing = CANONICAL - top
    extra = top - CANONICAL

    print("\nMISSING:", missing)
    print("EXTRA:", extra)

    return not missing and not extra


if __name__ == "__main__":
    ok = validate()
    print("\nVALIDATION:", "PASS" if ok else "FAIL")
