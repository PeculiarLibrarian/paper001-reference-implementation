from contracts.manager_dependency_contract import ManagerDependencyContract


class RelationshipIntegrityManager:

    @staticmethod
    def handshake():

        return {

            "manager": "RelationshipIntegrityManager",
            "version": "1.0",
            "contract": "manager_contract",
            "capabilities": [

                "verify_relationships",
                "resolve_producers",
                "execute",

            ],

        }

    def execute(self, context=None):

        dependencies = ManagerDependencyContract.DEPENDENCIES

        providers = {}

        for manager, spec in dependencies.items():

            for artifact in spec.get("produces", []):

                providers[artifact] = manager

        integrity = []

        for manager, spec in dependencies.items():

            for artifact in spec.get("depends_on", []):

                provider = providers.get(artifact)

                integrity.append({

                    "source": manager,
                    "depends_on": artifact,
                    "provider": provider,
                    "verified": provider is not None,

                })

        return {

            "relationship_integrity": integrity

        }
