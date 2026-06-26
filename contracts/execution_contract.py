from dataclasses import dataclass, field
from typing import List, Dict


@dataclass
class ExecutionContract:

    # defines dependency order between managers
    dependencies: Dict[str, List[str]] = field(default_factory=dict)


def default_execution_contract():

    return ExecutionContract(
        dependencies={
            "OntologyManager": [],
            "TaxonomyManager": ["OntologyManager"],
            "ShapesManager": ["OntologyManager"],
            "QueryManager": ["OntologyManager", "TaxonomyManager"],
            "FieldMemoryManager": [],
        }
    )
