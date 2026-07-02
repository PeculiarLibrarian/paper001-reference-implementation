from pathlib import Path

from peculiarlibrarian.engine.repository import load_repository
from peculiarlibrarian.engine.execution_plan import build_execution_plan

repo = load_repository(Path("peculiarlibrary"))
plan = build_execution_plan(repo)

print(f"Artifacts: {len(plan.artifacts)}")
print()

for i, artifact in enumerate(plan.artifacts, start=1):
    print(
        f"{i:02d}. "
        f"{artifact.library_id:15} "
        f"{artifact.artifact_type:10} "
        f"{artifact.path.name}"
    )
