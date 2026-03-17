from app.services.agent import SimpleAgent


def test_summary_allowed():
    agent = SimpleAgent()

    policy = {
        "allowed_actions": ["summarize"],
        "no_data_leakage": True,
    }

    input_data = "This is a public document."

    response = agent.run(input_data, policy)

    assert response.blocked is False
    assert response.output.startswith("Summary")


def test_secret_blocked():
    agent = SimpleAgent()

    policy = {
        "block_secrets": True,
    }

    input_data = "This is a secret key: 12345"

    response = agent.run(input_data, policy)

    assert response.blocked is True
    assert response.reason == "Sensitive input detected"


def test_leakage_prevented():
    agent = SimpleAgent()

    policy = {
        "allowed_actions": ["transform"],
        "no_data_leakage": True,
    }

    input_data = "sensitive data"

    response = agent.run(input_data, policy)

    assert response.blocked is True