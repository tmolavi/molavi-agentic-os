---
name: Bumblebee MCP & Supply Chain Security Audit
description: Audits Model Context Protocol tools, configuration manifests, and package dependencies for supply chain risks.
category: security
version: 1.0.0
author: Taqi Molavi
license: MIT
---

# Bumblebee MCP & Supply Chain Security Audit

Audits Model Context Protocol tools, configuration manifests, and package dependencies for supply chain risks.

Inspired by Perplexity Bumblebee architecture.

## Trigger Conditions
- Activated before installing third-party MCP servers or tools.
- Invoked during security reviews of agent capabilities and tool manifests.

## Required Inputs
```json
{
  "mcp_server_config": "object",
  "tool_definitions": "list",
  "dependencies": "list"
}
```

## Execution Instructions
1. Inspect tool handlers for unsafe shell invocations (`rm -rf`, `sudo`, `curl | bash`).
2. Verify path parameters are jailed within workspace boundaries to prevent traversal attacks.
3. Check dependencies against known vulnerabilities and typosquatting vectors.
4. Flag missing HMAC approval gates on high-privilege tools (level L2/L3).

## Expected Outputs
```json
{
  "is_safe": "boolean",
  "security_issues": "list",
  "recommended_mitigations": "list",
  "audit_timestamp": "number"
}
```

## Limitations & Security
- **Limitation:** Static pattern analysis; does not execute binary dynamic analysis.
- **Security:** Blocks tool registration if critical security violations are discovered.
