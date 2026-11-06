"""Deterministic mock provider for reproducible offline unit testing."""

from .base import ModelProvider, ModelResponse

class MockProvider(ModelProvider):
    def __init__(self, fixed_response: str = '{"status": "ok", "summary": "Deterministic verification pass"}'):
        self.fixed_response = fixed_response

    def generate(self, prompt: str, system_prompt: str = "", max_tokens: int = 2048) -> ModelResponse:
        return ModelResponse(
            content=self.fixed_response,
            model_name="mock-deterministic-v1",
            prompt_tokens=len(prompt) // 4,
            completion_tokens=len(self.fixed_response) // 4,
            total_tokens=(len(prompt) + len(self.fixed_response)) // 4,
            estimated_cost_usd=0.0,
            latency_seconds=0.01
        )
