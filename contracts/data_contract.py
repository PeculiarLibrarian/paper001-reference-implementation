from dataclasses import dataclass
from typing import Any, Dict, List


# ----------------------------
# ONTOLOGY CONTRACT
# ----------------------------

@dataclass
class OntologyBundle:
    graph: Any
    assets: List[str]
    metrics: Dict[str, Any]


# ----------------------------
# TAXONOMY CONTRACT
# ----------------------------

@dataclass
class TaxonomyBundle:
    registry: Dict[str, Any]
    index: Dict[str, Any]
    concepts: int


# ----------------------------
# SHAPES CONTRACT
# ----------------------------

@dataclass
class ShapesBundle:
    registry: Dict[str, Any]
    shapes: int
    triples: int


# ----------------------------
# QUERY CONTRACT
# ----------------------------

@dataclass
class QueryBundle:
    catalog: Dict[str, Any]
    registry: Dict[str, Any]
    queries: int


# ----------------------------
# FIELD MEMORY CONTRACT
# ----------------------------

@dataclass
class FieldMemoryBundle:
    field: Dict[str, Any]
    run: int
    snapshot: Dict[str, Any]
