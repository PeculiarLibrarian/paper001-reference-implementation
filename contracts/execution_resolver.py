from contracts.execution_contract import default_execution_contract


def resolve_execution_order(managers):

    contract = default_execution_contract().dependencies

    name_to_manager = {
        m.__class__.__name__: m for m in managers
    }

    visited = set()
    order = []

    def visit(name):

        if name in visited:
            return

        deps = contract.get(name, [])

        for d in deps:
            if d in name_to_manager:
                visit(d)

        visited.add(name)
        order.append(name_to_manager[name])

    for name in name_to_manager:
        visit(name)

    return order
