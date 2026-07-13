from padi.core.core_matrix import dump_matrix, validate_core_matrix
from padi_guard import validate_import


class PadiBootKernel:
    """
    Boot-time enforcement of PADI architecture.
    """

    def __init__(self):
        self.matrix = dump_matrix()

    def validate_structure(self):
        print("[BOOT] Loading PADI Core Matrix...")

        validation = validate_core_matrix()

        if not validation["valid"]:
            raise SystemError(
                f"[BOOT FAILURE] Missing layers: {validation['missing_layers']}"
            )

        print("✔ Core Matrix Valid")

        # enforce minimal guard sanity
        validate_import("RDF", "DATA")
        print("✔ Layer Guard OK")

        print("[BOOT] PADI Kernel VALID")
        return True


def boot():
    kernel = PadiBootKernel()
    return kernel.validate_structure()
