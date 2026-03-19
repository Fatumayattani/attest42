import hashlib
import json
from typing import Dict, Any


class AttestationService:
    """
    Generates and verifies attestations for TEE executions.
    """

    def _hash(self, data: str) -> str:
        return hashlib.sha256(data.encode()).hexdigest()

    def generate_attestation(
        self,
        agent_id: str,
        input_hash: str,
        output_hash: str,
        policy: Dict[str, Any],
        tee_quote: str,
        blocked: bool,
        reason: str | None,
    ) -> Dict[str, Any]:
        """
        Create deterministic attestation record.
        """

        attestation = {
            "agent_id": agent_id,
            "input_hash": input_hash,
            "output_hash": output_hash,
            "policy": policy,
            "tee_quote": tee_quote,
            "blocked": blocked,
            "reason": reason,
        }

        # Deterministic signature
        signature = self._hash(json.dumps(attestation, sort_keys=True))
        attestation["signature"] = signature

        return attestation

    def verify_attestation(self, attestation: Dict[str, Any]) -> Dict[str, Any]:
        """
        Verify integrity and structure.
        """

        # Extract signature
        signature = attestation.get("signature")

        if not signature:
            return {
                "valid": False,
                "error": "Missing signature",
            }

        # Recompute expected signature
        reconstructed = attestation.copy()
        reconstructed.pop("signature", None)

        expected_signature = self._hash(json.dumps(reconstructed, sort_keys=True))

        is_valid = signature == expected_signature

        return {
            "valid": is_valid,
            "checks": {
                "signature": is_valid,
                "has_quote": bool(attestation.get("tee_quote")),
                "has_hashes": bool(attestation.get("input_hash") and attestation.get("output_hash")),
            },
        }