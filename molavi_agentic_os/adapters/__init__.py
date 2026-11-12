"""TM Platform Adapters."""

from .base import PlatformAdapter
from .antigravity import AntigravityAdapter
from .codex import CodexAdapter
from .claude_code import ClaudeCodeAdapter
from .hermes import HermesAdapter
from .hermes_desktop import HermesDesktopAdapter
from .generic import GenericAdapter

__all__ = [
    "PlatformAdapter",
    "AntigravityAdapter",
    "CodexAdapter",
    "ClaudeCodeAdapter",
    "HermesAdapter",
    "HermesDesktopAdapter",
    "GenericAdapter"
]
