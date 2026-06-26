from contracts.contract_binding_map import CONTRACT_MAP


def enforce_contract(manager_instance):

    name = manager_instance.__class__.__name__

    expected = CONTRACT_MAP.get(name, None)

    if expected is None:
        raise Exception(f"Unbound manager: {name}")

    manager_instance._contract = expected

    return manager_instance
