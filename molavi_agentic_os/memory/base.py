"""Base interface for Molavi Agentic OS memory backends."""

from abc import ABC, abstractmethod
from typing import Dict, List, Any, Optional

class MemoryInterface(ABC):
    @abstractmethod
    def store_episode(self, session_id: str, agent_id: str, entry: Dict[str, Any]) -> None:
        pass

    @abstractmethod
    def get_episodes(self, session_id: str, limit: int = 20) -> List[Dict[str, Any]]:
        pass

    @abstractmethod
    def set_key(self, namespace: str, key: str, value: Any) -> None:
        pass

    @abstractmethod
    def get_key(self, namespace: str, key: str) -> Optional[Any]:
        pass
