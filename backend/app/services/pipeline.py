from typing import Dict, Any

from app.services.attestation import AttestationService
from app.services.tee import TEE


class Attest42Pipeline:
    """
    Orchestrates execution:
    input → TEE (isolated) → attestation
    """

    def __init__(self):
        self.tee = TEE()
        self.attestor = AttestationService()

    def run(self, input_data: str, policy: Dict[str, Any]) -> Dict[str, Any]:
        # 🔥 TEE now handles execution
        tee_result = self.tee.execute(input_data, policy)

        attestation = self.attestor.generate_attestation(
            agent_id="attest42",
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