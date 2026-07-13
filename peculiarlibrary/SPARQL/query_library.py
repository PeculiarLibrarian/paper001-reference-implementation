from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class QueryIR:
    """
    Immutable representation of a SPARQL query.
    """
    name: str
    text: str
    category: str = "GENERAL"
    query_type: str = "STATIC"


def parse_query_names(query_text: str):
    names = []
    for line in query_text.splitlines():
        line = line.strip()
        if line.startswith("# QUERY:"):
            names.append(line.removeprefix("# QUERY:").strip())
    return names


def build_ir_registry(library_path: Path):
    """
    Build immutable query registry from a SPARQL library.
    Supports metadata directives:

        # CATEGORY: ...
        # TYPE: ...
        # QUERY: ...

    Metadata applies to the query that immediately follows.
    """

    text = library_path.read_text(encoding="utf-8")

    registry = {}

    current_name = None
    current_category = "GENERAL"
    current_type = "STATIC"
    body = []

    def commit():
        nonlocal current_name, current_category, current_type, body

        if current_name is None:
            return

        registry[current_name] = QueryIR(
            name=current_name,
            text="\n".join(body).strip(),
            category=current_category,
            query_type=current_type,
        )

    for raw_line in text.splitlines():
        line = raw_line.strip()

        if line.startswith("# CATEGORY:"):
            current_category = line.removeprefix("# CATEGORY:").strip()
            continue

        if line.startswith("# TYPE:"):
            current_type = line.removeprefix("# TYPE:").strip()
            continue

        if line.startswith("# QUERY:"):
            commit()

            current_name = line.removeprefix("# QUERY:").strip()
            body = []
            continue

        if current_name is not None:
            body.append(raw_line)

    commit()

    return registry
