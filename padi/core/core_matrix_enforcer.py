from padi.core.core_matrix import CORE_MATRIX


class CoreMatrixViolation(Exception):
    pass


class CoreMatrixEnforcer:
    """
    Enforces strict layer boundaries defined in PADI Core Matrix.
    """

    def __init__(self):
        self.matrix = CORE_MATRIX

    def validate_layer_access(self, source_layer: str, target_class: str):
        for layer, allowed in self.matrix.items():
            if target_class in allowed:
                # if source is LOWER layer trying to access HIGHER layer → violation
                if self._is_illegal_access(source_layer, layer):
                    raise CoreMatrixViolation(
                        f"{source_layer} cannot access {target_class} in {layer}"
                    )

    def _is_illegal_access(self, source, target):
        order = list(self.matrix.keys())
        return order.index(source) < order.index(target)
