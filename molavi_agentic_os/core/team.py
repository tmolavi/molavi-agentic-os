"""Canonical Multi-Agent Team Specification for Molavi Agentic OS."""

from dataclasses import dataclass, field, asdict
from typing import Dict, List, Any, Optional
import json

@dataclass
class TeamRole:
    role_id: str
    agent_id: str
    title: str
    responsibilities: List[str]
    can_delegate_to: List[str] = field(default_factory=list)
    must_report_to: Optional[str] = None

@dataclass
class TeamDefinition:
    id: str
    name: str
    purpose: str
    coordinator_role_id: str
    roles: List[TeamRole] = field(default_factory=list)
    delegation_rules: List[str] = field(default_factory=list)
    execution_sequence: List[str] = field(default_factory=list)
    dependencies: List[str] = field(default_factory=list)
    review_process: str = ""
    failure_handling: str = "retry_with_backoff_then_escalate"
    approval_requirements: List[str] = field(default_factory=list)
    final_deliverable: str = ""

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "TeamDefinition":
        raw_roles = data.get("roles", [])
        roles = []
        for r in raw_roles:
            roles.append(TeamRole(
                role_id=r.get("role_id", ""),
                agent_id=r.get("agent_id", ""),
                title=r.get("title", ""),
                responsibilities=r.get("responsibilities", []),
                can_delegate_to=r.get("can_delegate_to", []),
                must_report_to=r.get("must_report_to"),
            ))
        return cls(
            id=data.get("id", ""),
            name=data.get("name", ""),
            purpose=data.get("purpose", ""),
            coordinator_role_id=data.get("coordinator_role_id", ""),
            roles=roles,
            delegation_rules=data.get("delegation_rules", []),
            execution_sequence=data.get("execution_sequence", []),
            dependencies=data.get("dependencies", []),
            review_process=data.get("review_process", ""),
            failure_handling=data.get("failure_handling", "escalate_to_human"),
            approval_requirements=data.get("approval_requirements", []),
            final_deliverable=data.get("final_deliverable", ""),
        )

    def to_json(self, indent: int = 2) -> str:
        return json.dumps(self.to_dict(), indent=indent, ensure_ascii=False)
