import subprocess
import json
import os


class TEEExecutionResult:
    def __init__(self, output, input_hash, output_hash, quote, blocked, reason):
        self.output = output
        self.input_hash = input_hash
        self.output_hash = output_hash
        self.quote = quote
        self.blocked = blocked
        self.reason = reason


class TEE:
    """
    TEE abstraction using isolated subprocess execution.
    """

    def execute(self, input_data: str, policy: dict) -> TEEExecutionResult:
        payload = {
            "input": input_data,
            "policy": policy,
        }

        # Absolute path to avoid path issues
        import pathlib

        project_root = pathlib.Path(__file__).resolve().parents[3]
        enclave_path = project_root / "tee" / "enclave_simulator.py"

        result = subprocess.run(
            ["python", str(enclave_path)],
            input=json.dumps(payload),
            text=True,
            capture_output=True,
        )

        if result.returncode != 0:
            raise Exception(f"TEE execution failed: {result.stderr}")

        data = json.loads(result.stdout)

        return TEEExecutionResult(
            output=data["output"],
            input_hash=data["input_hash"],
            output_hash=data["output_hash"],
            quote=data["quote"],
            blocked=data["blocked"],
            reason=data["reason"],
        )