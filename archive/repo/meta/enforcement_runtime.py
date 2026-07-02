import os
import rdflib
from pyshacl import validate

class SemanticEnforcementRuntimeV11:

    def __init__(self, root="repo/"):
        self.root = root
        self.SHAPES = os.path.join(
            root,
            "schemas/finance/shapes/finance_shapes.ttl"
        )

    def commit_to_immutable_graph(self, temp_file, final_path, manifest):

        conforms, _, text = validate(
            temp_file,
            shacl_graph=self.SHAPES,
            inference='rdfs'
        )

        if not conforms:
            print("❌ SHACL FAILED")
            print(text)
            return False

        os.makedirs(os.path.dirname(final_path), exist_ok=True)
        os.rename(temp_file, final_path)

        self._write_manifest(manifest)

        return True

    def _write_manifest(self, manifest):
        print("📦 Commit manifest recorded:", manifest)
