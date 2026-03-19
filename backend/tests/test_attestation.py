from app.services.attestation import AttestationService


def test_generate_attestation():
    service = AttestationService()

    attestation = service.generate_attestation(
        agent_id="agent-001",
        input_hash="input123",
        output_hash="output456",
        policy={"allowed_actions": ["summarize"]},
        tee_quote="quote123",
        blocked=False,
        reason=None,
    )

    assert "signature" in attestation
    assert attestation["agent_id"] == "agent-001"


def test_verify_valid_attestation():
    service = AttestationService()

    attestation = service.generate_attestation(
        agent_id="agent-001",
        input_hash="input123",
        output_hash="output456",
        policy={"allowed_actions": ["summarize"]},
        tee_quote="quote123",
        blocked=False,
        reason=None,
    )

    result = service.verify_attestation(attestation)

    assert result["valid"] is True


def test_detect_tampering():
    service = AttestationService()

    attestation = service.generate_attestation(
        agent_id="agent-001",
        input_hash="input123",
        output_hash="output456",
        policy={"allowed_actions": ["summarize"]},
        tee_quote="quote123",
        blocked=False,
        reason=None,
    )

    # Tamper with data
    attestation["output_hash"] = "tampered"

    result = service.verify_attestation(attestation)

    assert result["valid"] is False