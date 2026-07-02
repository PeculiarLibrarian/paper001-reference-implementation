"""
PADI Semantic Compiler
Version: 0.9.0

Single compiler entry point.

Pipeline

Dataset
    ↓
Doctrine Enforcement
    ↓
Mapping Grammar
    ↓
Factory Dispatch
    ↓
SHACL Validation
    ↓
Hash Policy
    ↓
Semantic Materialization Ledger
    ↓
Compiled Knowledge Graph
"""

import json
from pathlib import Path

from rdflib import Graph

from peculiarlibrary.factory.core_factory import FactoryRegistry
from peculiarlibrary.ledger.hash_policy import HashPolicy
from peculiarlibrary.ledger.materialization_ledger import (
    SemanticMaterializationLedger,
)


class SemanticCompiler:

    VERSION = "0.9.0"

    def __init__(
        self,
        mapper,
        doctrine_enforcer,
        shacl_validator,
    ):

        self.graph = Graph()

        self.registry = FactoryRegistry(self.graph)

        self.mapper = mapper
        self.doctrine = doctrine_enforcer
        self.validator = shacl_validator

        self.ledger = SemanticMaterializationLedger()

    def load_dataset(self, dataset_path):

        with open(dataset_path, "r", encoding="utf-8") as f:
            return json.load(f)

    def compile(self, dataset_path):

        dataset = self.load_dataset(dataset_path)

        commands = self.mapper.map(dataset)

        commands = self.doctrine.validate(commands)

        for command in commands:
            self.registry.execute(command)

        self.validator.validate(self.graph)

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
            validation=True,
            provenance={
                "compiler": self.__class__.__name__,
            },
        )

        self.ledger.serialize(
            "runtime/materialization_ledger.jsonld"
        )

        return self.graph

    def serialize(self, destination, format="turtle"):

        Path(destination).parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        self.graph.serialize(
            destination=destination,
            format=format,
        )

        return destination
