from pathlib import Path
import yaml

ROOT = Path("peculiarlibrary")

repo = yaml.safe_load((ROOT / "peculiarlibrary.yaml").read_text())

print("=== CONSTITUTION ===")
for section, files in repo["constitution"].items():
    for rel in files:
        p = ROOT / rel
        status = "OK" if p.exists() else "MISSING"
        print(f"{section:10} {status:8} {p}")

print("\n=== DISCOVERY ===")

for discovery_dir in repo["discovery"]:
    base = ROOT / discovery_dir
    for library in sorted(base.glob("*/library.yaml")):
        spec = yaml.safe_load(library.read_text())
        print(f"\nLibrary: {spec['id']}")

        imports = spec.get("imports", [])
        if imports:
            print("  imports:")
            for imp in imports:
                resolved = (library.parent / imp).resolve()
                print(f"    {resolved}")
        else:
            print("  imports: none")
