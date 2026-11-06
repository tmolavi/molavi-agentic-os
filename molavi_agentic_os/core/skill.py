"""Canonical Skill Specification for Molavi Agentic OS."""

from dataclasses import dataclass, field, asdict
from typing import Dict, List, Any, Optional
import json

@dataclass
class SkillMetadata:
    id: str
    name: str
    description: str
    category: str
    version: str = "1.0.0"
    author: str = "Taqi Molavi"
    license: str = "MIT"

@dataclass
class SkillDefinition:
    metadata: SkillMetadata
    trigger_conditions: List[str] = field(default_factory=list)
    required_inputs: Dict[str, Any] = field(default_factory=dict)
    execution_instructions: str = ""
    expected_outputs: Dict[str, Any] = field(default_factory=dict)
    examples: List[Dict[str, Any]] = field(default_factory=list)
    limitations: List[str] = field(default_factory=list)
    security_considerations: List[str] = field(default_factory=list)
    validation_tests: List[Dict[str, Any]] = field(default_factory=list)

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "SkillDefinition":
        meta_dict = data.get("metadata", {})
        metadata = SkillMetadata(
            id=meta_dict.get("id", ""),
            name=meta_dict.get("name", ""),
            description=meta_dict.get("description", ""),
            category=meta_dict.get("category", "general"),
            version=meta_dict.get("version", "1.0.0"),
            author=meta_dict.get("author", "Taqi Molavi"),
            license=meta_dict.get("license", "MIT"),
        )
        return cls(
            metadata=metadata,
            trigger_conditions=data.get("trigger_conditions", []),
            required_inputs=data.get("required_inputs", {}),
            execution_instructions=data.get("execution_instructions", ""),
            expected_outputs=data.get("expected_outputs", {}),
            examples=data.get("examples", []),
            limitations=data.get("limitations", []),
            security_considerations=data.get("security_considerations", []),
            validation_tests=data.get("validation_tests", []),
        )

    def to_markdown(self) -> str:
        """Serialize to open Agent Skills SKILL.md format."""
        lines = [
            "---",
            f"name: {self.metadata.name}",
            f"description: {self.metadata.description}",
            f"category: {self.metadata.category}",
            f"version: {self.metadata.version}",
            "---",
            "",
            f"# {self.metadata.name}",
            "",
            f"{self.metadata.description}",
            "",
            "## Trigger Conditions",
        ]
        for trig in self.trigger_conditions:
            lines.append(f"- {trig}")
        lines.extend([
            "",
            "## Required Inputs",
            "```json",
            json.dumps(self.required_inputs, indent=2),
            "```",
            "",
            "## Execution Instructions",
            self.execution_instructions,
            "",
            "## Expected Outputs",
            "```json",
            json.dumps(self.expected_outputs, indent=2),
            "```",
            "",
            "## Limitations & Security",
        ])
        for lim in self.limitations:
            lines.append(f"- **Limitation:** {lim}")
        for sec in self.security_considerations:
            lines.append(f"- **Security:** {sec}")
        return "\n".join(lines)
