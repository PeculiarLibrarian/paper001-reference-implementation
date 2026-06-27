from pathlib import Path


class ArtifactRegistry:

    @staticmethod
    def artifacts():

        return {

            "manager": Path("managers"),

            "contract": Path("contracts"),

            "kernel": Path("kernel"),

            "orchestrator": Path("orchestrator"),

            "schema": Path("schema"),

            "ontology": Path("ontology"),

        }
