import subprocess
from pathlib import Path


class JenaSHACLRunner:
    """
    Executes SHACL validation using Apache Jena CLI (shacl).
    """

    def __init__(self, jena_bin="shacl"):
        self.jena_bin = jena_bin

    def validate(self, data_path, shapes_path):
        """
        Runs Jena SHACL validation.

        Returns:
            dict with conforms + raw output
        """

        if not Path(data_path).exists():
            raise FileNotFoundError(data_path)

        if not Path(shapes_path).exists():
            raise FileNotFoundError(shapes_path)

        cmd = [
            self.jena_bin,
            "validate",
            "--data", str(data_path),
            "--shapes", str(shapes_path),
        ]

        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True
        )

        output = result.stdout + "\n" + result.stderr

        conforms = "Conforms: true" in output or "conforms: true" in output.lower()

        return {
            "conforms": conforms,
            "raw_output": output.strip(),
            "return_code": result.returncode,
        }
