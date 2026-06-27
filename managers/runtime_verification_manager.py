from managers.artifact_discovery_manager import ArtifactDiscoveryManager
from managers.artifact_provenance_manager import ArtifactProvenanceManager
from managers.artifact_relationship_manager import ArtifactRelationshipManager
from managers.relationship_integrity_manager import RelationshipIntegrityManager


class RuntimeVerificationManager:

    @staticmethod
    def handshake():

        return {

            "manager": "RuntimeVerificationManager",
            "version": "1.0",
            "contract": "manager_contract",
            "capabilities": [

                "verify_runtime",
                "execute",

            ],

        }

    def execute(self, context=None):

        inventory = ArtifactDiscoveryManager().execute()

        provenance = ArtifactProvenanceManager().execute(inventory)

        relationships = ArtifactRelationshipManager().execute()

        integrity = RelationshipIntegrityManager().execute()

        artifacts_ok = all(
            record["contract_valid"]
            for record in provenance["artifact_provenance"]
        )

        relationships_ok = all(
            record["contract_valid"]
            for record in relationships["relationships"]
        )

        integrity_ok = all(
            record["verified"]
            for record in integrity["relationship_integrity"]
        )

        verified = (
            artifacts_ok
            and relationships_ok
            and integrity_ok
        )

        return {

            "verified": verified,

            "artifact_count":
                len(provenance["artifact_provenance"]),

            "relationship_count":
                len(relationships["relationships"]),

            "integrity_count":
                len(integrity["relationship_integrity"]),

            "artifacts_ok":
                artifacts_ok,

            "relationships_ok":
                relationships_ok,

            "integrity_ok":
                integrity_ok,

        }
