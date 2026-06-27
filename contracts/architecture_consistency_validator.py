import os
from typing import Dict, Set


def to_snake(name: str) -> str:

    # convert PascalCase → snake_case

    import re

    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)

    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()


class ArchitectureConsistencyValidator:

    def __init__(self):

        self.base_path = "managers"

    def discover_managers(self) -> Set[str]:

        return {

            f.replace(".py", "")

            for f in os.listdir(self.base_path)

            if f.endswith(".py")

            and not f.startswith("__")

        }

    def manifest_managers(self, manifest: Dict) -> Set[str]:

        return {

            to_snake(k)

            for k in manifest.keys()

        }

    def dependency_managers(self, deps: Dict) -> Set[str]:

        return {

            to_snake(k)

            for k in deps.keys()

        }

    def validate(self, manifest: Dict, dependencies: Dict) -> Dict:

        filesystem = self.discover_managers()

        manifest_set = self.manifest_managers(manifest)

        dependency_set = self.dependency_managers(dependencies)

        return {

            "valid":
                filesystem == manifest_set == dependency_set,

            "filesystem": sorted(filesystem),

            "missing_in_manifest": sorted(filesystem - manifest_set),

            "missing_in_dependencies": sorted(filesystem - dependency_set),

            "orphan_manifest": sorted(manifest_set - filesystem),

            "orphan_dependencies": sorted(dependency_set - filesystem),

        }
