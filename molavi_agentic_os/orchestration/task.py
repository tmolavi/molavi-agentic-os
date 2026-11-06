"""Task data structures for Molavi Agentic OS."""

from dataclasses import dataclass, field
from enum import Enum
from typing import Dict, Any, Optional, List
import time
import uuid

class TaskStatus(str, Enum):
    PENDING = "PENDING"
    QUEUED = "QUEUED"
    RUNNING = "RUNNING"
    BLOCKED_ON_APPROVAL = "BLOCKED_ON_APPROVAL"
    VERIFYING = "VERIFYING"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"
    TIMED_OUT = "TIMED_OUT"

@dataclass
class TaskResult:
    success: bool
    output: Dict[str, Any] = field(default_factory=dict)
    evidence: List[str] = field(default_factory=list)
    error: Optional[str] = None
    execution_time_seconds: float = 0.0
    tokens_used: int = 0
    estimated_cost_usd: float = 0.0

@dataclass
class Task:
    name: str
    action: str
    agent_id: str
    inputs: Dict[str, Any] = field(default_factory=dict)
    task_id: str = field(default_factory=lambda: str(uuid.uuid4())[:8])
    status: TaskStatus = TaskStatus.PENDING
    depends_on: List[str] = field(default_factory=list)
    requires_approval: bool = False
    approval_ticket_id: Optional[str] = None
    max_retries: int = 3
    retry_count: int = 0
    timeout_seconds: float = 60.0
    created_at: float = field(default_factory=time.time)
    completed_at: Optional[float] = None
    result: Optional[TaskResult] = None
