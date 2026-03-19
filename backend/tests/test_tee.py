from app.services.tee import MockTEE


def test_tee_execution_success():
    tee = MockTEE()

    policy = {
        "allowed_actions": ["summarize"],
        "no_data_leakage": True,
    }

    input_data = "This is a safe document."

    result = tee.execute(input_data, policy)

    assert result.blocked is False
    assert result.output.startswith("Summary")
    assert isinstance(result.input_hash, str)
    assert isinstance(result.output_hash, str)
    assert isinstance(result.quote, str)


def test_tee_blocks_leakage():
    tee = MockTEE()

    policy = {
        "allowed_actions": ["transform"],
        "no_data_leakage": True,
    }

    input_data = "sensitive data"

    result = tee.execute(input_data, policy)

    assert result.blocked is True
    assert result.reason == "Data leakage detected"


def test_quote_is_deterministic():
    tee = MockTEE()

    policy = {
        "allowed_actions": ["summarize"],
    }

    input_data = "Deterministic test"

    result1 = tee.execute(input_data, policy)
    result2 = tee.execute(input_data, policy)

    assert result1.quote == result2.quote