"""TM Second Brain Memory Adapter — Local-first Markdown & Obsidian memory bridge.

Integrates with `tm-second-brain` (https://github.com/tmolavi/tm-second-brain)
for persistent, model-agnostic cross-session memory with immutable provenance.
"""

import os
import json
import time
import hashlib
from typing import Dict, List, Any, Optional
from .base import MemoryInterface


class TMSecondBrainMemoryAdapter(MemoryInterface):
    """Adapter bridging Molavi Agentic OS to a local Obsidian/Markdown Second Brain vault."""

    def __init__(self, vault_path: str = ".tm-brain", namespace: str = "default"):
        self.vault_path = os.path.expanduser(vault_path)
        self.namespace = namespace
        self.notes_dir = os.path.join(self.vault_path, "memory", self.namespace)
        self.audit_log_path = os.path.join(self.vault_path, ".audit_log.jsonl")
        os.makedirs(self.notes_dir, exist_ok=True)
        self._kv_cache: Dict[str, Any] = {}

    def store_episode(self, session_id: str, agent_id: str, entry: Dict[str, Any]) -> None:
        """Stores an episodic memory entry as a persistent Markdown note with YAML metadata."""
        now = time.strftime("%Y%m%d_%H%M%S")
        content_str = json.dumps(entry, sort_keys=True)
        entry_hash = hashlib.sha256(content_str.encode("utf-8")).hexdigest()[:8]
        filename = f"mem_{now}_{entry_hash}.md"
        filepath = os.path.join(self.notes_dir, filename)

        frontmatter = (
            f"---\n"
            f"id: mem_{now}_{entry_hash}\n"
            f"session_id: {session_id}\n"
            f"agent_id: {agent_id}\n"
            f"namespace: {self.namespace}\n"
            f"timestamp: {time.time()}\n"
            f"status: active\n"
            f"---\n\n"
        )
        body = f"# Episodic Memory Entry\n\n```json\n{json.dumps(entry, indent=2)}\n```\n"

        with open(filepath, "w", encoding="utf-8") as f:
            f.write(frontmatter + body)

        # Append to audit log
        audit_record = {
            "action": "store_episode",
            "file": filename,
            "session_id": session_id,
            "agent_id": agent_id,
            "hash": entry_hash,
            "time": time.time()
        }
        with open(self.audit_log_path, "a", encoding="utf-8") as f:
            f.write(json.dumps(audit_record) + "\n")

    def get_episodes(self, session_id: str, limit: int = 20) -> List[Dict[str, Any]]:
        """Retrieves past episodic memory entries for a given session."""
        episodes = []
        if not os.path.exists(self.notes_dir):
            return episodes

        files = sorted(os.listdir(self.notes_dir), reverse=True)
        for fname in files:
            if not fname.endswith(".md"):
                continue
            fpath = os.path.join(self.notes_dir, fname)
            try:
                with open(fpath, "r", encoding="utf-8") as f:
                    content = f.read()
                if f"session_id: {session_id}" in content:
                    # Extract json block
                    if "```json" in content:
                        raw_json = content.split("```json")[1].split("```")[0].strip()
                        data = json.loads(raw_json)
                        episodes.append({
                            "file": fname,
                            "session_id": session_id,
                            "entry": data
                        })
                        if len(episodes) >= limit:
                            break
            except Exception:
                continue

        return episodes

    def set_key(self, namespace: str, key: str, value: Any) -> None:
        """Stores key-value state in persistent namespace file."""
        self._kv_cache[f"{namespace}:{key}"] = value
        kv_file = os.path.join(self.vault_path, f"kv_{namespace}.json")
        try:
            current = {}
            if os.path.exists(kv_file):
                with open(kv_file, "r", encoding="utf-8") as f:
                    current = json.load(f)
            current[key] = {
                "value": value,
                "updated_at": time.time()
            }
            with open(kv_file, "w", encoding="utf-8") as f:
                json.dump(current, f, indent=2)
        except Exception:
            pass

    def get_key(self, namespace: str, key: str) -> Optional[Any]:
        """Retrieves a persistent key-value entry."""
        cache_key = f"{namespace}:{key}"
        if cache_key in self._kv_cache:
            return self._kv_cache[cache_key]

        kv_file = os.path.join(self.vault_path, f"kv_{namespace}.json")
        if os.path.exists(kv_file):
            try:
                with open(kv_file, "r", encoding="utf-8") as f:
                    data = json.load(f)
                    if key in data:
                        val = data[key]["value"]
                        self._kv_cache[cache_key] = val
                        return val
            except Exception:
                pass
        return None
