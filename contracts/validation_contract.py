from contracts.behavior_contract import ManagerContract


def validate_manager(manager):

    missing = []

    for method in ManagerContract.REQUIRED_METHODS:

        if not hasattr(manager, method):

            missing.append(method)

    if missing:

        raise TypeError(
            f"Manager {manager.__class__.__name__} "
            f"missing contract methods: {missing}"
        )

    return True
