"""Base interface for model providers in Molavi Agentic OS."""

from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import Dict, Any, Optional

@dataclass
class ModelResponse:
    content: str
    model_name: str
    prompt_tokens: int = 0
    completion_tokens: int = 0
    total_tokens: int = 0
    estimated_cost_usd: float = 0.0
    latency_seconds: float = 0.0
    raw: Optional[Dict[str, Any]] = None

class ModelProvider(ABC):
    @abstractmethod
    def generate(self, prompt: str, system_prompt: str = "", max_tokens: int = 2048) -> ModelResponse:
        pass
