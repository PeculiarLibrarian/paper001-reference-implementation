from peculiarlibrary.core.padi_core_matrix import validate


class CoreMatrixEnforcer:
    """
    PADI Core Matrix enforcement layer.
    Delegates ALL truth to padi_core_matrix.py
    """

    def validate_layer_access(self, layer: str, component: str):
        return validate(layer, component)
