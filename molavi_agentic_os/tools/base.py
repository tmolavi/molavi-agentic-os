"""TM Tool & MCP Gateway — Base Tool Definition & Execution Interface."""

from dataclasses import dataclass, field
from typing import Dict, Any, List, Optional, Callable
import time
import inspect
import json


@dataclass
class ToolParameter:
    """Schema definition for a tool input parameter."""
    name: str
    type_name: str  # string, integer, float, boolean, object, array
    description: str
    required: bool = True
    default: Optional[Any] = None


@dataclass
class ToolDefinition:
    """Standardized tool specification with JSON Schema contracts and security boundaries."""
    name: str
    description: str
    parameters: List[ToolParameter] = field(default_factory=list)
    required_permission: str = "L0_SAFE_READONLY"  # L0_SAFE_READONLY, L1_WORKSPACE_MUTATION, L2_HUMAN_APPROVAL, L3_CRITICAL_SYSTEM
    timeout_seconds: float = 30.0
    handler: Optional[Callable[..., Any]] = None

    def to_json_schema(self) -> Dict[str, Any]:
        """Converts tool parameters to standard JSON Schema format for LLMs & MCP."""
        properties = {}
        required_fields = []
        for p in self.parameters:
            properties[p.name] = {
                "type": p.type_name,
                "description": p.description
            }
            if p.required:
                required_fields.append(p.name)

        return {
            "type": "object",
            "properties": properties,
            "required": required_fields
        }

    def validate_inputs(self, arguments: Dict[str, Any]) -> List[str]:
        """Validates input arguments against schema constraints."""
        errors = []
        for p in self.parameters:
            if p.required and p.name not in arguments:
                errors.append(f"Missing required parameter: '{p.name}'")
            elif p.name in arguments:
                val = arguments[p.name]
                expected = p.type_name.lower()
                if expected == "string" and not isinstance(val, str):
                    errors.append(f"Parameter '{p.name}' expected string, got {type(val).__name__}")
                elif expected in ["integer", "int"] and (not isinstance(val, int) or isinstance(val, bool)):
                    errors.append(f"Parameter '{p.name}' expected integer, got {type(val).__name__}")
                elif expected in ["float", "number"] and not isinstance(val, (int, float)):
                    errors.append(f"Parameter '{p.name}' expected number, got {type(val).__name__}")
                elif expected in ["boolean", "bool"] and not isinstance(val, bool):
                    errors.append(f"Parameter '{p.name}' expected boolean, got {type(val).__name__}")
        return errors


@dataclass
class ToolResult:
    """Encapsulates tool execution output, telemetry, and status."""
    tool_name: str
    success: bool
    output: Any
    error: Optional[str] = None
    execution_time_ms: float = 0.0
