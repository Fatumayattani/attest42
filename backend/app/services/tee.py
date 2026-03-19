import hashlib
import json
import base64
from typing import Dict

from app.services.agent import SimpleAgent, AgentResponse


class TEEExecutionResult:
    def __init__(
        self,
        output: str,
        input_hash: str,
        output_hash: str,
        quote: str,
        blocked: bool,
        reason: str | None,
    ):
        self.output = output
        self.input_hash = input_hash
        self.output_hash = output_hash
        self.quote = quote
        self.blocked = blocked
        self.reason = reason


class MockTEE:
    """
    Deterministic TEE simulation for testing and demo.
    """

    def __init__(self, enclave_id: str = "attest42-enclave"):
        self.enclave_id = enclave_id
        self.agent = SimpleAgent()

    def execute(self, input_data: str, policy: Dict) -> TEEExecutionResult:
        agent_response: AgentResponse = self.agent.run(input_data, policy)

        input_hash = self._hash(input_data)
        output_hash = self._hash(agent_response.output)

        quote = self._generate_quote(input_hash, output_hash)

        return TEEExecutionResult(
            output=agent_response.output,
            input_hash=input_hash,
            output_hash=output_hash,
            quote=quote,
            blocked=agent_response.blocked,
            reason=agent_response.reason,
        )

    def _hash(self, data: str) -> str:
        return hashlib.sha256(data.encode()).hexdigest()

    def _generate_quote(self, input_hash: str, output_hash: str) -> str:
        payload = {
            "enclave_id": self.enclave_id,
            "input_hash": input_hash,
            "output_hash": output_hash,
        }

        serialized = json.dumps(payload, sort_keys=True)
        return base64.b64encode(serialized.encode()).decode()