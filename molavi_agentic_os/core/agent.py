"""Canonical Agent Specification for Molavi Agentic OS."""

from dataclasses import dataclass, field, asdict
from enum import Enum
from typing import Dict, List, Any, Optional
import json

class PermissionLevel(str, Enum):
    L0_READ_ONLY = "L0_READ_ONLY"
    L1_DRAFT_RECOMMEND = "L1_DRAFT_RECOMMEND"
    L2_HUMAN_APPROVAL = "L2_HUMAN_APPROVAL"
    L3_PRE_AUTHORIZED = "L3_PRE_AUTHORIZED"

@dataclass
class AgentMetadata:
    id: str
    name: str
    purpose: str
    role: str
    category: str
    version: str = "1.0.0"
    author: str = "Taqi Molavi"
    license: str = "MIT"

@dataclass
class AgentDefinition:
    metadata: AgentMetadata
    system_instructions: str
    required_skills: List[str] = field(default_factory=list)
    required_tools: List[str] = field(default_factory=list)
    input_schema: Dict[str, Any] = field(default_factory=dict)
    output_schema: Dict[str, Any] = field(default_factory=dict)
    execution_boundaries: List[str] = field(default_factory=list)
    permission_level: PermissionLevel = PermissionLevel.L1_DRAFT_RECOMMEND
    model_requirements: Dict[str, Any] = field(default_factory=lambda: {"preferred_tier": "free", "context_window_min": 8192})
    cost_profile: Dict[str, Any] = field(default_factory=lambda: {"max_tokens_per_run": 4096, "estimated_cost_usd": 0.0})
    test_cases: List[Dict[str, Any]] = field(default_factory=list)
    example_usage: str = ""

    def to_dict(self) -> Dict[str, Any]:
        data = asdict(self)
        data["permission_level"] = self.permission_level.value
        return data

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "AgentDefinition":
        meta_dict = data.get("metadata", {})
        metadata = AgentMetadata(
            id=meta_dict.get("id", ""),
            name=meta_dict.get("name", ""),
            purpose=meta_dict.get("purpose", ""),
            role=meta_dict.get("role", ""),
            category=meta_dict.get("category", "general"),
            version=meta_dict.get("version", "1.0.0"),
            author=meta_dict.get("author", "Taqi Molavi"),
            license=meta_dict.get("license", "MIT"),
        )
        perm_str = data.get("permission_level", PermissionLevel.L1_DRAFT_RECOMMEND.value)
        permission_level = PermissionLevel(perm_str) if perm_str in PermissionLevel._value2member_map_ else PermissionLevel.L1_DRAFT_RECOMMEND
        
        return cls(
            metadata=metadata,
            system_instructions=data.get("system_instructions", ""),
            required_skills=data.get("required_skills", []),
            required_tools=data.get("required_tools", []),
            input_schema=data.get("input_schema", {}),
            output_schema=data.get("output_schema", {}),
            execution_boundaries=data.get("execution_boundaries", []),
            permission_level=permission_level,
            model_requirements=data.get("model_requirements", {}),
            cost_profile=data.get("cost_profile", {}),
            test_cases=data.get("test_cases", []),
            example_usage=data.get("example_usage", ""),
        )

    def to_json(self, indent: int = 2) -> str:
        return json.dumps(self.to_dict(), indent=indent, ensure_ascii=False)
