FORBIDDEN_IMPORTS = {
    "peculiarlibrarian.engine.runtime.operator_runtime": [
        "peculiarlibrarian.engine.runtime.system_validator"
    ],
    "peculiarlibrarian.engine.runtime.system_validator": [
        "peculiarlibrarian.engine.runtime.operator_runtime"
    ]
}

def check(module: str, target: str):
    return target in FORBIDDEN_IMPORTS.get(module, [])
