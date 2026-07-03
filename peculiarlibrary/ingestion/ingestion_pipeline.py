"""
PADI Semantic Compiler
Version: 0.9.3

Locked pipeline with runtime version and structure enforcement.
"""

import hashlib
import json
from pathlib import Path

from rdflib import Graph

from peculiarlibrary.factory.core_factory import FactoryRegistry
from peculiarlibrary.ledger.hash_policy import HashPolicy
from peculiarlibrary.ledger.materialization_ledger import (
    SemanticMaterializationLedger,
)
from peculiarlibrary.ontology.schema_validator import (
    OntologySchemaValidator,
)

from peculiarlibrary.ingestion.pipeline_lock import (
    PIPELINE_VERSION,
    PIPELINE_STAGES,
    expected_signature,
)


class SemanticCompiler:

    VERSION = "0.9.3"

    def __init__(
        self,
        mapper,
        doctrine_enforcer,
        shacl_validator,
        ontology_validator=None,
    ):

        # -------------------------------------------------
        # PIPELINE IMMUTABILITY GUARDS
        # -------------------------------------------------

        assert (
            self.VERSION == PIPELINE_VERSION
        ), "Pipeline version mismatch"

        signature = hashlib.sha256(
            "|".join(PIPELINE_STAGES).encode("utf-8")
        ).hexdigest()

        assert (
            signature == expected_signature()
        ), "Pipeline structure mismatch"

        # -------------------------------------------------
        # Compiler Components
        # -------------------------------------------------

        self.graph = Graph()

        self.registry = FactoryRegistry(self.graph)

        self.mapper = mapper
        self.doctrine = doctrine_enforcer
        self.validator = shacl_validator

        self.ontology_validator = (
            ontology_validator
            or OntologySchemaValidator(Graph())
        )

        self.ledger = SemanticMaterializationLedger()

    # -------------------------------------------------
    # Dataset Loading
    # -------------------------------------------------

    def load_dataset(self, dataset_path: str):

        path = Path(dataset_path)

        if not path.exists():
            raise FileNotFoundError(
                f"Dataset not found: {dataset_path}"
            )

        with path.open(
            "r",
            encoding="utf-8",
        ) as f:
            return json.load(f)

    # -------------------------------------------------
    # Validation Normalization
    # -------------------------------------------------

    def _normalize_validation(self, validation_result):

        if hasattr(validation_result, "conforms"):
            return {
                "conforms": validation_result.conforms,
                "triples": getattr(
                    validation_result,
                    "triples",
                    None,
                ),
            }

        if isinstance(validation_result, tuple):
            return {
                "conforms": validation_result[0],
                "graph": str(validation_result[1]),
                "raw": validation_result[2],
            }

        return {
            "value": str(validation_result),
        }

    # -------------------------------------------------
    # Compiler
    # -------------------------------------------------

    def compile(self, dataset_path: str):

        dataset = self.load_dataset(dataset_path)

        commands = self.mapper.map(dataset)

        commands = self.doctrine.validate(commands)

        commands = self.ontology_validator.validate(commands)

        for command in commands:
            self.registry.execute(command)

        validation_result = self.validator.validate(
            self.graph
        )

        materialization_id = HashPolicy.materialization_id(
            compiler_version=self.VERSION,
            mapper=self.mapper.__class__.__name__,
            dataset=dataset_path,
            commands=commands,
        )

        self.ledger.record(
            materialization_id=materialization_id,
            compiler_version=self.VERSION,
            mapper=self.mapper.__class__.__name__,
            dataset=dataset_path,
            triple_count=len(self.graph),
            validation=self._normalize_validation(
                validation_result
            ),
            provenance={
                "compiler": self.__class__.__name__,
            },
        )

        ledger_path = Path(
            "runtime/materialization_ledger.jsonld"
        )

        ledger_path.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        self.ledger.serialize(str(ledger_path))

        return self.graph

    # -------------------------------------------------
    # RDF Serialization
    # -------------------------------------------------

    def serialize(
        self,
        destination: str,
        format: str = "turtle",
    ):

        path = Path(destination)

        path.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        self.graph.serialize(
            destination=str(path),
            format=format,
        )

        return str(path)
