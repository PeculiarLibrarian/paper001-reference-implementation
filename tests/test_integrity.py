from pathlib import Path
import subprocess
import yaml
import sys

ROOT = Path("peculiarlibrary")

errors = []

def check_file(path):
    if not path.exists():
        errors.append(f"Missing: {path}")
        return False
    return True

print("=" * 60)
print("PECULIAR LIBRARY INTEGRITY REPORT")
print("=" * 60)

repo = yaml.safe_load((ROOT / "peculiarlibrary.yaml").read_text())

print("\nCONSTITUTION")

constitution = repo.get("constitution", {})

for section, files in constitution.items():
    for rel in files:
        p = ROOT / rel
        if check_file(p):
            print(f"PASS  {section:<10} {p}")
        else:
            print(f"FAIL  {section:<10} {p}")

print("\nLIBRARIES")

libraries = sorted(ROOT.glob("domains/*/library.yaml"))

for lib in libraries:
    data = yaml.safe_load(lib.read_text())

    print(f"\n{data['id']}")

    artifacts = data.get("artifacts", {})

    for name, filename in artifacts.items():
        artifact = lib.parent / filename

        if check_file(artifact):
            print(f"PASS  {name:<10} {artifact.name}")
        else:
            print(f"FAIL  {name:<10} {artifact.name}")

        if artifact.exists() and artifact.suffix == ".ttl":
            result = subprocess.run(
                ["riot", "--validate", str(artifact)],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
            )

            if result.returncode != 0:
                errors.append(f"Invalid Turtle: {artifact}")
                print("      riot: FAIL")
            else:
                print("      riot: PASS")

print("\nSUMMARY")
print("-" * 60)

if errors:
    print("STATUS : FAIL")
    print()
    for e in errors:
        print(e)
    sys.exit(1)
else:
    print("STATUS : PASS")
    print("Repository integrity verified.")
