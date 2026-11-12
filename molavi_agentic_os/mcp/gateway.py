"""TM MCP Gateway — Standardized Model Context Protocol client & server adapter."""

import json
from typing import Dict, Any, List, Optional
from ..tools.registry import ToolRegistry
from ..tools.base import ToolDefinition, ToolResult
from .security_auditor import BumblebeeMCPSecurityAuditor


class MCPGateway:
    """Manages Model Context Protocol tool discovery, invocation, and security isolation."""

    def __init__(self, registry: Optional[ToolRegistry] = None, enforce_bumblebee_security: bool = True):
        self.registry = registry or ToolRegistry()
        self.enforce_bumblebee_security = enforce_bumblebee_security

    def export_tools_manifest(self) -> Dict[str, Any]:
        """Generates standard MCP tools listing schema for MCP clients."""
        tools_list = []
        for tool in self.registry.list_tools():
            schema = tool.to_json_schema()
            tools_list.append({
                "name": tool.name,
                "description": tool.description,
                "inputSchema": schema,
                "permission": tool.required_permission
            })
        return {
            "protocol_version": "2024-11-05",
            "tools": tools_list
        }

    def handle_call_tool(self, tool_name: str, arguments: Dict[str, Any]) -> Dict[str, Any]:
        """Handles an incoming MCP `tools/call` JSON-RPC request with security audit."""
        # 1. Bumblebee security check
        if self.enforce_bumblebee_security:
            sec_res = BumblebeeMCPSecurityAuditor.audit_invocation_arguments(arguments)
            if not sec_res.is_safe:
                return {
                    "isError": True,
                    "content": [
                        {
                            "type": "text",
                            "text": f"BUMBLEBEE SECURITY BLOCK: Potential malicious argument detected: {'; '.join(sec_res.issues)}"
                        }
                    ]
                }

        # 2. Execute via registry
        res: ToolResult = self.registry.execute(tool_name, arguments)
        if not res.success:
            return {
                "isError": True,
                "content": [
                    {
                        "type": "text",
                        "text": f"Error executing tool '{tool_name}': {res.error}"
                    }
                ]
            }

        return {
            "isError": False,
            "content": [
                {
                    "type": "text",
                    "text": json.dumps(res.output) if isinstance(res.output, (dict, list)) else str(res.output)
                }
            ],
            "execution_time_ms": res.execution_time_ms
        }
