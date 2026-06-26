import importlib
import inspect


def discover_managers():
    """
    Contract enforcement:
    MUST return Dict[str, ManagerInstance]
    NOT list, NOT tuple.
    """

    package_name = "managers"

    registry = {}

    # You likely already have module list logic — keep simple & deterministic
    manager_modules = [
        "ontology_manager",
        "opportunity_engine",
        "taxonomy_manager",
        "shapes_manager",
        "query_manager",
        "reasoning_manager",
        "schema_manager",
        "field_memory_manager",
        "semantic_core_manager",
        "ingestion_manager",
        "orchestration_manager"
    ]

    for module_name in manager_modules:
        module = importlib.import_module(f"{package_name}.{module_name}")

        # find manager class inside module
        for name, obj in inspect.getmembers(module, inspect.isclass):
            if name.endswith("Manager") or name.endswith("Engine"):
                registry[name] = obj()

    return registry
