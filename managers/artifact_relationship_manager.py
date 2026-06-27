from contracts.manager_dependency_contract import ManagerDependencyContract
from contracts.artifact_relationship_contract import ArtifactRelationshipContract


class ArtifactRelationshipManager:

    @staticmethod
    def handshake():

        return {

            "manager": "ArtifactRelationshipManager",
            "version": "1.0",
            "contract": "manager_contract",
            "capabilities": [

                "relationships",
                "dependency_validation",
                "execute",

            ],

        }

    def execute(self, context=None):

        relationships = []

        for manager, spec in ManagerDependencyContract.DEPENDENCIES.items():

            for dependency in spec.get("depends_on", []):

                record = {

                    "source": manager,
                    "relationship": "depends_on",
                    "target": dependency,
                    "verified": True,

                }

                validation = ArtifactRelationshipContract.validate(record)

                record["contract_valid"] = validation["valid"]
                record["missing_fields"] = validation["missing"]

                relationships.append(record)

        return {

            "relationships": relationships

        }
