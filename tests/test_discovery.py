from pathlib import Path
from peculiarlibrarian.engine.core import SemanticEngine

engine = SemanticEngine(Path("peculiarlibrary"))

libraries = engine.discover()

print(f"Discovered {len(libraries)} libraries")

for lib in libraries:
    print(f"\nLibrary: {lib.id}")
    print(f"Version: {lib.version}")
    print("Artifacts:")

    for name, path in lib.artifacts.items():
        print(f"  {name}: {path}")

    print("Imports:")

    for item in lib.imports:
        print(f"  {item}")
