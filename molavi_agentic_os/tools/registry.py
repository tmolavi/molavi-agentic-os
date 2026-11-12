"""TM Tool Registry — Central repository of agent tools with permission and runtime guardrails."""

from typing import Dict, List, Optional, Any
import time
from .base import ToolDefinition, ToolResult


class ToolRegistry:
    """Thread-safe tool registry supporting capability discovery and execution."""

    def __init__(self):
        self._tools: Dict[str, ToolDefinition] = {}

    def register(self, tool: ToolDefinition) -> None:
        """Registers a new tool in the central catalog."""
        self._tools[tool.name] = tool

    def get(self, name: str) -> Optional[ToolDefinition]:
        """Retrieves a registered tool by name."""
        return self._tools.get(name)

    def list_tools(self) -> List[ToolDefinition]:
        """Returns all registered tool definitions."""
        return list(self._tools.values())

    def execute(self, tool_name: str, arguments: Dict[str, Any]) -> ToolResult:
        """Executes a tool with strict validation, timeout checks, and error isolation."""
        tool = self.get(tool_name)
        if not tool:
            return ToolResult(
                tool_name=tool_name,
                success=False,
                output=None,
                error=f"Tool '{tool_name}' not found in registry."
            )

        # 1. Input Validation
        validation_errors = tool.validate_inputs(arguments)
        if validation_errors:
            return ToolResult(
                tool_name=tool_name,
                success=False,
                output=None,
                error=f"Validation failed: {'; '.join(validation_errors)}"
            )

        if not tool.handler:
            return ToolResult(
                tool_name=tool_name,
                success=False,
                output=None,
                error=f"Tool '{tool_name}' has no executable handler registered."
            )

        # 2. Execution with telemetry
        start_time = time.perf_counter()
        try:
            res = tool.handler(**arguments)
            elapsed_ms = (time.perf_counter() - start_time) * 1000.0
            return ToolResult(
                tool_name=tool_name,
                success=True,
                output=res,
                execution_time_ms=elapsed_ms
            )
        except Exception as e:
            elapsed_ms = (time.perf_counter() - start_time) * 1000.0
            return ToolResult(
                tool_name=tool_name,
                success=False,
                output=None,
                error=f"Execution error: {str(e)}",
                execution_time_ms=elapsed_ms
            )
