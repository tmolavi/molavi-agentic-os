"""Zero-cost local persistent SQLite memory store."""

import sqlite3
import json
import time
from typing import Dict, List, Any, Optional
from .base import MemoryInterface

class SQLiteMemoryStore(MemoryInterface):
    def __init__(self, db_path: str = ":memory:"):
        self.db_path = db_path
        self._conn = sqlite3.connect(self.db_path, check_same_thread=False)
        self._conn.row_factory = sqlite3.Row
        self._init_db()

    def _get_conn(self) -> sqlite3.Connection:
        return self._conn

    def _init_db(self):
        with self._get_conn() as conn:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS episodes (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    session_id TEXT NOT NULL,
                    agent_id TEXT NOT NULL,
                    entry_json TEXT NOT NULL,
                    created_at REAL NOT NULL
                )
            """)
            conn.execute("""
                CREATE TABLE IF NOT EXISTS kv_store (
                    namespace TEXT NOT NULL,
                    key TEXT NOT NULL,
                    value_json TEXT NOT NULL,
                    updated_at REAL NOT NULL,
                    PRIMARY KEY (namespace, key)
                )
            """)
            conn.commit()

    def store_episode(self, session_id: str, agent_id: str, entry: Dict[str, Any]) -> None:
        with self._get_conn() as conn:
            conn.execute(
                "INSERT INTO episodes (session_id, agent_id, entry_json, created_at) VALUES (?, ?, ?, ?)",
                (session_id, agent_id, json.dumps(entry), time.time())
            )
            conn.commit()

    def get_episodes(self, session_id: str, limit: int = 20) -> List[Dict[str, Any]]:
        with self._get_conn() as conn:
            cur = conn.cursor()
            cur.execute(
                "SELECT agent_id, entry_json, created_at FROM episodes WHERE session_id = ? ORDER BY id DESC LIMIT ?",
                (session_id, limit)
            )
            rows = cur.fetchall()
            return [
                {"agent_id": r["agent_id"], "entry": json.loads(r["entry_json"]), "created_at": r["created_at"]}
                for r in reversed(rows)
            ]

    def set_key(self, namespace: str, key: str, value: Any) -> None:
        with self._get_conn() as conn:
            conn.execute(
                "INSERT OR REPLACE INTO kv_store (namespace, key, value_json, updated_at) VALUES (?, ?, ?, ?)",
                (namespace, key, json.dumps(value), time.time())
            )
            conn.commit()

    def get_key(self, namespace: str, key: str) -> Optional[Any]:
        with self._get_conn() as conn:
            cur = conn.cursor()
            cur.execute("SELECT value_json FROM kv_store WHERE namespace = ? AND key = ?", (namespace, key))
            row = cur.fetchone()
            if row:
                return json.loads(row["value_json"])
            return None
