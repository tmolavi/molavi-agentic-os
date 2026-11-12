"""Workflow Failure Recovery and Model Fallback.

Demonstrates:
1. Simulated primary network or provider failure
2. Automated retry policy with exponential backoff
3. Dynamic fallback to Free-First local provider (e.g., Ollama / Llama 3.2 via ModelRouter)
4. Graceful recovery and completion
"""

import sys
import os
import time

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from molavi_agentic_os.providers.router import ModelRouter, ModelTier
from molavi_agentic_os.providers.mock_provider import MockProvider


class ResilientExecutionEngine:
    """Manages task retries and provider fallbacks."""

    def __init__(self, max_retries: int = 2, initial_delay_ms: float = 20.0):
        self.max_retries = max_retries
        self.initial_delay_ms = initial_delay_ms

    def execute_with_fallback(self, task_name: str, primary_provider_fail_times: int = 2) -> dict:
        attempts = 0
        current_delay = self.initial_delay_ms / 1000.0

        print(f"\n[EXECUTION] Initiating task: '{task_name}'")

        while attempts < self.max_retries:
            attempts += 1
            print(f"  Attempt {attempts}/{self.max_retries}: Calling primary endpoint...")

            if attempts <= primary_provider_fail_times:
                print(f"  -> [FAILED] Primary provider timeout (504 Gateway Timeout).")
                print(f"  -> Backing off for {current_delay * 1000:.0f}ms...")
                time.sleep(current_delay)
                current_delay *= 2
            else:
                print(f"  -> [SUCCESS] Connection established on attempt {attempts}.")
                return {
                    "task": task_name,
                    "status": "success",
                    "provider": "PrimaryCloudProvider",
                    "attempts": attempts,
                    "cost": "$0.02"
                }

        # If primary failed all attempts, trigger fallback model router
        print("\n[FALLBACK TRIGGERED] Primary provider exhausted retries.")
        print("[ROUTER] Escalating to Free-First Router (Local Ollama Llama-3.2 3B)...")
        router = ModelRouter()
        local_mock = MockProvider(fixed_response="System security architecture verified offline.")
        router.register_provider("ollama-local", local_mock, ModelTier.FREE_LOCAL)

        resp = router.route_and_generate(
            prompt="Summarize technical architecture",
            preferred_tier=ModelTier.FREE_LOCAL
        )
        print(f"  -> [RECOVERED] Fallback execution succeeded with zero marginal API cost ($0.00).")
        print(f"  Model: {resp.model_name} | Content: '{resp.content}'")

        return {
            "task": task_name,
            "status": "recovered",
            "provider": resp.model_name,
            "cost": "$0.00",
            "output": resp.content
        }


def main():
    print("=" * 75)
    print("TM MOLAVI AGENTIC OS — FAILURE RECOVERY & FALLBACK ROUTING")
    print("=" * 75)

    engine = ResilientExecutionEngine(max_retries=2, initial_delay_ms=20.0)
    result = engine.execute_with_fallback(
        task_name="Generate System Security Overview",
        primary_provider_fail_times=2
    )

    print("\n[SUMMARY] Final Execution Result:")
    print(f"  Status:   {result['status']}")
    print(f"  Provider: {result['provider']}")
    print(f"  Cost:     {result['cost']}")
    print("Resilience cycle completed successfully without workflow termination.\n")


if __name__ == "__main__":
    main()
