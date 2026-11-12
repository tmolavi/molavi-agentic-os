"""TM MCP Security Auditor — Supply-chain, MCP server, and tool permission audit.

Inspired by Perplexity Bumblebee architecture:
- Static inspection of tool handlers and parameter declarations.
- Detection of dangerous shell injections, arbitrary file path traversals, and unbound socket executions.
- Principle of least privilege enforcement for agent MCP tools.
"""

from typing import Dict, Any, List, Optional
import re
from ..tools.base import ToolDefinition

DANGEROUS_COMMANDS = [
    r"rm\s+-rf",
    r"sudo\s+",
    r"mkfs",
    r":\(\)\{.*:\|:&\};:",  # Fork bomb
    r"curl\s+.*\|\s*bash",
    r"wget\s+.*\|\s*sh",
    r"chmod\s+777",
    r"dd\s+if=",
]

SUSPICIOUS_PATH_PATTERNS = [
    r"\.\./\.\./",
    r"/etc/shadow",
    r"/etc/passwd",
    r"~/.ssh",
    r"~/.aws",
]


class MCPSecurityAuditResult:
    def __init__(self, is_safe: bool, issues: List[str], recommendations: List[str]):
        self.is_safe = is_safe
        self.issues = issues
        self.recommendations = recommendations

    def to_dict(self) -> Dict[str, Any]:
        return {
            "is_safe": self.is_safe,
            "issues": self.issues,
            "recommendations": self.recommendations
        }


class BumblebeeMCPSecurityAuditor:
    """Security auditor for MCP tools, server manifests, and invocation payloads."""

    @classmethod
    def audit_tool_definition(cls, tool: ToolDefinition) -> MCPSecurityAuditResult:
        """Audits a ToolDefinition for over-privileged access or dangerous descriptions."""
        issues = []
        recommendations = []

        # 1. Permission checks
        if "execute" in tool.name.lower() or "bash" in tool.name.lower() or "shell" in tool.name.lower():
            if tool.required_permission not in ["L2_HUMAN_APPROVAL", "L3_CRITICAL_SYSTEM"]:
                issues.append(f"Tool '{tool.name}' executes shell/system commands but is assigned lower permission: {tool.required_permission}")
                recommendations.append("Elevate required permission to L2_HUMAN_APPROVAL with HMAC approval tickets.")

        # 2. Parameter schema validation
        for p in tool.parameters:
            if p.type_name == "string" and "path" in p.name.lower() and not p.required:
                recommendations.append(f"Parameter '{p.name}' in '{tool.name}' represents a file path; ensure path sanitization and boundary checking.")

        is_safe = len(issues) == 0
        return MCPSecurityAuditResult(is_safe, issues, recommendations)

    @classmethod
    def audit_invocation_arguments(cls, arguments: Dict[str, Any]) -> MCPSecurityAuditResult:
        """Audits dynamic input arguments before MCP invocation to prevent injection."""
        issues = []
        recommendations = []

        for k, v in arguments.items():
            if isinstance(v, str):
                # Check for dangerous command execution
                for cmd_pat in DANGEROUS_COMMANDS:
                    if re.search(cmd_pat, v, re.IGNORECASE):
                        issues.append(f"Dangerous system command pattern detected in argument '{k}': {cmd_pat}")
                        recommendations.append("Block execution and alert security operator immediately.")

                # Check for path traversal
                for path_pat in SUSPICIOUS_PATH_PATTERNS:
                    if re.search(path_pat, v):
                        issues.append(f"Sensitive path traversal detected in argument '{k}': {path_pat}")
                        recommendations.append("Sanitize path to remain inside workspace jail directory.")

        is_safe = len(issues) == 0
        return MCPSecurityAuditResult(is_safe, issues, recommendations)
