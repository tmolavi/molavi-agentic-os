"""Canonical Workflow Specification for Molavi Agentic OS."""

from dataclasses import dataclass, field, asdict
from typing import Dict, List, Any, Optional
import json

@dataclass
class WorkflowStep:
    step_id: str
    name: str
    agent_id: str
    action: str
    inputs: Dict[str, Any] = field(default_factory=dict)
    depends_on: List[str] = field(default_factory=list)
    requires_approval: bool = False
    timeout_seconds: int = 300
    retry_count: int = 2

@dataclass
class WorkflowDefinition:
    id: str
    name: str
    description: str
    steps: List[WorkflowStep] = field(default_factory=list)
    on_failure: str = "halt_and_notify"
    final_output_key: str = "report"

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "WorkflowDefinition":
        steps = [
            WorkflowStep(
                step_id=s.get("step_id", ""),
                name=s.get("name", ""),
                agent_id=s.get("agent_id", ""),
                action=s.get("action", ""),
                inputs=s.get("inputs", {}),
                depends_on=s.get("depends_on", []),
                requires_approval=s.get("requires_approval", False),
                timeout_seconds=s.get("timeout_seconds", 300),
                retry_count=s.get("retry_count", 2),
            )
            for s in data.get("steps", [])
        ]
        return cls(
            id=data.get("id", ""),
            name=data.get("name", ""),
            description=data.get("description", ""),
            steps=steps,
            on_failure=data.get("on_failure", "halt_and_notify"),
            final_output_key=data.get("final_output_key", "report"),
        )

    def to_json(self, indent: int = 2) -> str:
        return json.dumps(self.to_dict(), indent=indent, ensure_ascii=False)
