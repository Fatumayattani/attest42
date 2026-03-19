from app.services.pipeline import Attest42Pipeline
from app.services.attestation import AttestationService


def test_pipeline_success():
    pipeline = Attest42Pipeline()
    verifier = AttestationService()

    policy = {
        "allowed_actions": ["summarize"],
        "no_data_leakage": True,
    }

    input_data = "This is safe."

    result = pipeline.run(input_data, policy)

    assert result["blocked"] is False
    assert "attestation" in result

    verification = verifier.verify_attestation(result["attestation"])
    assert verification["valid"] is True


def test_pipeline_blocks():
    pipeline = Attest42Pipeline()
    verifier = AttestationService()

    policy = {
        "allowed_actions": ["transform"],
        "no_data_leakage": True,
    }

    input_data = "sensitive data"

    result = pipeline.run(input_data, policy)

    assert result["blocked"] is True

    verification = verifier.verify_attestation(result["attestation"])
    assert verification["valid"] is True