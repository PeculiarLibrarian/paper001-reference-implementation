class SystemValidator:

    def __init__(self, rt_factory):
        self.rt_factory = rt_factory

    def validate_pipeline(self, dataset_path: str):

        rt = self.rt_factory()

        compile_out = rt.execute("compile", {"dataset": dataset_path})
        reason_out = rt.execute("reason", {"dataset": dataset_path})
        validate_out = rt.execute("validate", {"dataset": dataset_path})

        return {
            "compile": compile_out["result"]["status"],
            "reason": reason_out["result"]["status"],
            "validate": validate_out["result"]["status"]
        }
