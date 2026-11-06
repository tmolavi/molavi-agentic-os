"""In-memory scratchpad and fast working memory."""

from typing import Dict, Any, List

class WorkingMemory:
    """Manages ephemeral working state, scratchpads, and immediate context."""

    def __init__(self):
        self._scratchpad: Dict[str, Any] = {}
        self._history: List[str] = []

    def set(self, key: str, value: Any) -> None:
        self._scratchpad[key] = value

    def get(self, key: str, default: Any = None) -> Any:
        return self._scratchpad.get(key, default)

    def log(self, entry: str) -> None:
        self._history.append(entry)

    def get_history(self) -> List[str]:
        return list(self._history)

    def clear(self) -> None:
        self._scratchpad.clear()
        self._history.clear()
