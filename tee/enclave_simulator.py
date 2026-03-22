import json
import hashlib
import base64
import os


def run():
    """
    Simulated enclave execution.
    Designed to run inside dstack task environment.
    """

    input_data = os.getenv("INPUT_DATA", "This is a safe document.")
    policy_json = os.getenv(
        "POLICY",
        json.dumps({"allowed_actions": ["summarize"], "no_data_leakage": True}),
    )

    policy = json.loads(policy_json)

    # --- AGENT LOGIC INSIDE "TEE" ---
    if "summarize" in policy.get("allowed_actions", []):
        output = "Summary generated successfully."
        blocked = False
        reason = None
    else:
        output = ""
        blocked = True
        reason = "Action not allowed"

    # --- HASHES ---
    input_hash = hashlib.sha256(input_data.encode()).hexdigest()
    output_hash = hashlib.sha256(output.encode()).hexdigest()

    # --- TEE QUOTE (attestation payload) ---
    quote_payload = {
        "enclave_id": "attest42-dstack-real",
        "input_hash": input_hash,
        "output_hash": output_hash,
    }

    quote = base64.b64encode(json.dumps(quote_payload).encode()).decode()

    # --- FINAL RESULT ---
    result = {
        "output": output,
        "input_hash": input_hash,
        "output_hash": output_hash,
        "quote": quote,
        "blocked": blocked,
        "reason": reason,
    }

    print(json.dumps(result))


if __name__ == "__main__":
    run()