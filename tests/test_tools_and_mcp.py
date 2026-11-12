"""Tests for TM Tool Registry, MCP Gateway, and Bumblebee Security Auditor."""

import pytest
from molavi_agentic_os.tools import ToolDefinition, ToolParameter, ToolRegistry
from molavi_agentic_os.mcp import MCPGateway, BumblebeeMCPSecurityAuditor


def test_tool_registration_and_execution():
    registry = ToolRegistry()

    def add(a: int, b: int) -> int:
        return a + b

    tool = ToolDefinition(
        name="add_numbers",
        description="Adds two integers.",
        parameters=[
            ToolParameter("a", "integer", "First number", required=True),
            ToolParameter("b", "integer", "Second number", required=True)
        ],
        handler=add
    )
    registry.register(tool)

    assert registry.get("add_numbers") is not None
    assert len(registry.list_tools()) == 1

    # Valid execution
    res = registry.execute("add_numbers", {"a": 10, "b": 25})
    assert res.success is True
    assert res.output == 35
    assert res.error is None
    assert res.execution_time_ms >= 0.0

    # Validation failure: missing parameter
    res_missing = registry.execute("add_numbers", {"a": 10})
    assert res_missing.success is False
    assert "Missing required parameter" in res_missing.error

    # Validation failure: wrong type
    res_type = registry.execute("add_numbers", {"a": "invalid", "b": 5})
    assert res_type.success is False
    assert "expected integer" in res_type.error


def test_mcp_gateway_manifest_and_invocation():
    registry = ToolRegistry()
    tool = ToolDefinition(
        name="echo_text",
        description="Echoes input text",
        parameters=[ToolParameter("text", "string", "Text to echo")],
        handler=lambda text: f"echo: {text}"
    )
    registry.register(tool)

    gateway = MCPGateway(registry=registry, enforce_bumblebee_security=True)
    manifest = gateway.export_tools_manifest()

    assert manifest["protocol_version"] == "2024-11-05"
    assert len(manifest["tools"]) == 1
    assert manifest["tools"][0]["name"] == "echo_text"

    # Call tool via gateway
    call_res = gateway.handle_call_tool("echo_text", {"text": "hello mcp"})
    assert call_res["isError"] is False
    assert call_res["content"][0]["text"] == "echo: hello mcp"


def test_bumblebee_mcp_security_auditor():
    # 1. Test injection block
    dangerous_args = {"command": "rm -rf / --no-preserve-root"}
    audit = BumblebeeMCPSecurityAuditor.audit_invocation_arguments(dangerous_args)
    assert audit.is_safe is False
    assert any("Dangerous system command" in issue for issue in audit.issues)

    # 2. Test path traversal block
    traversal_args = {"file_path": "../../etc/shadow"}
    audit_traversal = BumblebeeMCPSecurityAuditor.audit_invocation_arguments(traversal_args)
    assert audit_traversal.is_safe is False
    assert any("path traversal" in issue for issue in audit_traversal.issues)

    # 3. Test safe arguments
    safe_args = {"query": "deep learning architectures", "limit": 10}
    audit_safe = BumblebeeMCPSecurityAuditor.audit_invocation_arguments(safe_args)
    assert audit_safe.is_safe is True
