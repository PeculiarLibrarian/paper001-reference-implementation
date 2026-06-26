import inspect
import importlib
import pkgutil

from managers.contract_enforcer import enforce_contract
from contracts.validation_contract import validate_manager


def discover_managers(package_name="managers"):

    discovered = []

    package = importlib.import_module(package_name)

    for _, module_name, _ in pkgutil.iter_modules(package.__path__):

        module = importlib.import_module(f"{package_name}.{module_name}")

        for _, obj in inspect.getmembers(module, inspect.isclass):

            if not obj.__module__.startswith(package_name):
                continue

            try:
                instance = obj()

                instance = enforce_contract(instance)

                validate_manager(instance)

                discovered.append(instance)

            except Exception:
                continue

    return discovered
