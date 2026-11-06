"""Prompt Injection defense, secret scrubbing, and tool allowlisting."""

import re
from typing import Dict, Any, List

SUSPICIOUS_PROMPT_PATTERNS = [
    r"ignore previous instructions",
    r"disregard all previous prompts",
    r"system override",
    r"reveal your secret key",
    r"dump environmental variables",
    r"rm -rf",
    r"drop database",
]

SECRET_PATTERNS = [
    (r"(?i)api[_-]?key\s*[:=]\s*['\"]?([A-Za-z0-9_\-]{16,})['\"]?", "api_key=***REDACTED***"),
    (r"(?i)bearer\s+[A-Za-z0-9_\-\.]{16,}", "Bearer ***REDACTED***"),
    (r"(?i)ghp_[A-Za-z0-9]{36}", "ghp_***REDACTED***"),
]

class GuardrailFilter:
    """Security filter protecting agent runtime against injection and leakage."""

    @classmethod
    def sanitize_input(cls, text: str) -> str:
        """Flags or cleans prompt injection indicators."""
        for pattern in SUSPICIOUS_PROMPT_PATTERNS:
            if re.search(pattern, text, re.IGNORECASE):
                # Neutralize dangerous override prefix
                text = re.sub(pattern, "[FLAGGED_INJECTION_ATTEMPT]", text, flags=re.IGNORECASE)
        return text

    @classmethod
    def redact_secrets(cls, text: str) -> str:
        """Strips secret tokens and API keys from logged messages."""
        for pattern, replacement in SECRET_PATTERNS:
            text = re.sub(pattern, replacement, text)
        return text
