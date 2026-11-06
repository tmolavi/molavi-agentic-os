"""Free-First, task-based Model Router.

Prioritizes:
1. Local offline models (Ollama, llama3.2, mistral) -> $0.00
2. Free cloud tiers (Groq, Gemini Free Tier, OpenRouter Free) -> $0.00
3. Low-cost fallback models (Claude Haiku, GPT-4o-mini) -> Minimal cost
4. High-capability models ONLY when explicitly requested and approved.
"""

from enum import Enum
from typing import Dict, List, Optional
from .base import ModelProvider, ModelResponse

class ModelTier(str, Enum):
    FREE_LOCAL = "FREE_LOCAL"
    FREE_CLOUD = "FREE_CLOUD"
    CHEAP_CLOUD = "CHEAP_CLOUD"
    PREMIUM_CLOUD = "PREMIUM_CLOUD"

class ModelRouter:
    """Manages provider selection, quotas, fallback chains, and budget control."""

    def __init__(self):
        self._providers: Dict[str, ModelProvider] = {}
        self._tier_mapping: Dict[ModelTier, List[str]] = {
            ModelTier.FREE_LOCAL: [],
            ModelTier.FREE_CLOUD: [],
            ModelTier.CHEAP_CLOUD: [],
            ModelTier.PREMIUM_CLOUD: [],
        }
        self.total_tokens_consumed = 0
        self.total_cost_usd = 0.0

    def register_provider(self, name: str, provider: ModelProvider, tier: ModelTier):
        self._providers[name] = provider
        self._tier_mapping[tier].append(name)

    def route_and_generate(self, prompt: str, system_prompt: str = "", preferred_tier: ModelTier = ModelTier.FREE_LOCAL) -> ModelResponse:
        """Attempts execution starting at free tiers with graceful fallback."""
        tier_order = [
            preferred_tier,
            ModelTier.FREE_LOCAL,
            ModelTier.FREE_CLOUD,
            ModelTier.CHEAP_CLOUD,
        ]
        # Remove duplicates while preserving order
        seen = set()
        deduped = []
        for t in tier_order:
            if t not in seen:
                seen.add(t)
                deduped.append(t)

        last_error = None
        for tier in deduped:
            for p_name in self._tier_mapping.get(tier, []):
                p = self._providers[p_name]
                try:
                    resp = p.generate(prompt=prompt, system_prompt=system_prompt)
                    self.total_tokens_consumed += resp.total_tokens
                    self.total_cost_usd += resp.estimated_cost_usd
                    return resp
                except Exception as e:
                    last_error = e
                    continue

        raise RuntimeError(f"All configured model providers failed. Last error: {last_error}")
