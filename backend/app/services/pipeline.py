from typing import Dict, Any

from app.services.tee import MockTEE
from app.services.attestation import AttestationService


class Attest42Pipeline:
    """
    Orchestrates full execution flow:
    input → TEE → attestation
    """

    def __init__(self):
        self.tee = MockTEE()
        self.attestor = AttestationService()

    def run(self, input_data: str, policy: Dict[str, Any]) -> Dict[str, Any]:
        tee_result = self.tee.execute(input_data, policy)

        attestation = self.attestor.generate_attestation(
            agent_id="agent-001",
            input_hash=tee_result.input_hash,
            output_hash=tee_result.output_hash,
            policy=policy,
            tee_quote=tee_result.quote,
            blocked=tee_result.blocked,
            reason=tee_result.reason,
        )

        return {
            "output": tee_result.output,
            "blocked": tee_result.blocked,
            "reason": tee_result.reason,
            "attestation": attestation,
        }