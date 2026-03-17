from typing import Dict


class AgentResponse:
    def __init__(self, output: str, blocked: bool = False, reason: str = None):
        self.output = output
        self.blocked = blocked
        self.reason = reason


class SimpleAgent:
    """
    Minimal deterministic agent for hackathon demo.

    Rules:
    - Enforces pre-execution policy
    - Executes allowed action
    - Enforces post-execution leakage rule (strict, exact match)
    """

    def __init__(self, agent_id: str = "agent-001"):
        self.agent_id = agent_id

    def run(self, input_data: str, policy: Dict) -> AgentResponse:
        # Step 1: Pre-check
        violation = self._check_pre_execution_policy(input_data, policy)
        if violation:
            return AgentResponse(
                output="Request blocked by policy.",
                blocked=True,
                reason=violation,
            )

        # Step 2: Process
        output = self._process(input_data, policy)

        # Step 3: Post-check
        if not self._check_post_execution_policy(input_data, output, policy):
            return AgentResponse(
                output="⚠️ Output blocked due to policy violation.",
                blocked=True,
                reason="Data leakage detected",
            )

        return AgentResponse(output=output)

    # -----------------------------
    # Core logic
    # -----------------------------

    def _process(self, input_data: str, policy: Dict) -> str:
        allowed_actions = policy.get("allowed_actions", [])

        if "summarize" in allowed_actions:
            # IMPORTANT: must NOT include original input
            return "Summary generated successfully."

        if "transform" in allowed_actions:
            return input_data.upper()

        return "Action not allowed by policy."

    def _check_pre_execution_policy(self, input_data: str, policy: Dict) -> str | None:
        if policy.get("block_secrets", False):
            if "secret" in input_data.lower():
                return "Sensitive input detected"
        return None

    def _check_post_execution_policy(
        self, input_data: str, output_data: str, policy: Dict
    ) -> bool:
        """
        Strict rule:
        If output contains full input → leakage
        """

        if policy.get("no_data_leakage", False):
            if input_data.lower() in output_data.lower():
             return False

        return True