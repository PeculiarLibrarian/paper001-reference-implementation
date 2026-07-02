import json
import os
from typing import Dict, Any

class RegistryLoadError(Exception):
    pass

class RegistryLoader:
    """
    Loads and validates kernel registry artifacts from schemas/core/registry.
    Designed for Peculiar Librarian v3.5.0 protocol compliance.
    """

    def __init__(self, base_path: str = "schemas/core/registry"):
        self.base_path = base_path

    def _load_json(self, filename: str) -> Dict[str, Any]:
        path = os.path.join(self.base_path, filename)

        if not os.path.exists(path):
            raise RegistryLoadError(f"Missing registry file: {filename}")

        try:
            with open(path, "r", encoding="utf-8") as f:
                return json.load(f)
        except json.JSONDecodeError as e:
            raise RegistryLoadError(f"Invalid JSON in {filename}: {str(e)}")

    def load_all(self) -> Dict[str, Dict[str, Any]]:
        """
        Loads full registry bundle.
        Expected structure:
            aggregates.json
            opcodes.json
            kernel.json
            namespaces.json
            projections.json
            manifest.json
        """

        registry = {
            "aggregates": self._load_json("aggregates.json"),
            "opcodes": self._load_json("opcodes.json"),
            "kernel": self._load_json("kernel.json"),
            "namespaces": self._load_json("namespaces.json"),
            "projections": self._load_json("projections.json"),
            "manifest": self._load_json("manifest.json"),
        }

        self._validate_bundle(registry)
        return registry

    def _validate_bundle(self, registry: Dict[str, Any]) -> None:
        """
        Lightweight structural validation for v3.5.0 compliance.
        """

        required_keys = [
            "aggregates",
            "opcodes",
            "kernel",
            "namespaces",
            "projections",
            "manifest"
        ]

        for key in required_keys:
            if key not in registry:
                raise RegistryLoadError(f"Missing registry section: {key}")

        # Kernel version lock check
        kernel = registry["kernel"]
        if "version" not in kernel:
            raise RegistryLoadError("Kernel missing version field")

        if kernel["version"] != "3.5.0":
            raise RegistryLoadError(
                f"Kernel version mismatch: expected 3.5.0, got {kernel['version']}"
            )

        # Basic opcode integrity check
        opcodes = registry["opcodes"]
        if not isinstance(opcodes, dict):
            raise RegistryLoadError("Opcodes registry must be a JSON object")

        # Ensure no empty registries
        if not registry["aggregates"]:
            raise RegistryLoadError("Aggregates registry is empty")

        if not registry["namespaces"]:
            raise RegistryLoadError("Namespaces registry is empty")

    def get_section(self, registry: Dict[str, Any], section: str) -> Any:
        return registry.get(section)
