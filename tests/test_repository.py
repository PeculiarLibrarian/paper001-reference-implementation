from pathlib import Path

from peculiarlibrarian.engine.repository import load_repository

repo = load_repository(Path("peculiarlibrary"))

print(f"Repository : {repo.id}")
print(f"Version    : {repo.version}")

print("\nConstitution")

for section in (
    "ontology",
    "taxonomy",
    "shapes",
    "queries",
    "context",
):
    print(f"\n{section}")

    for item in getattr(repo.constitution, section):
        print(" ", item)

print("\nLibraries")

for lib in repo.libraries:
    print(" ", lib.id)
