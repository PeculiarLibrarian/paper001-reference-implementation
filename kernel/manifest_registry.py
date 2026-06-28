from pathlib import Path
import yaml


class ManifestRegistry:
    ROOT = Path("schemas/queries")

    @classmethod
    def manifest(cls, domain, query_id):
        return cls.ROOT / domain / query_id / "manifest.yaml"

    @classmethod
    def load(cls, domain, query_id):
        path = cls.manifest(domain, query_id)

        if not path.exists():
            raise FileNotFoundError(path)

        with open(path, "r") as f:
            return yaml.safe_load(f)

    @classmethod
    def discover(cls):
        manifests = []

        if not cls.ROOT.exists():
            return manifests

        for path in cls.ROOT.rglob("manifest.yaml"):
            with open(path) as f:
                manifests.append(yaml.safe_load(f))

        return manifests
