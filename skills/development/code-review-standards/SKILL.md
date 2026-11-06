---
name: Code Review & Clean Code Standards
description: Audit git diffs for architectural patterns, security vulnerabilities, test coverage, and code smell.
category: development
version: 1.0.0
author: Taqi Molavi
license: MIT
---

# Code Review & Clean Code Standards

Audit git diffs for architectural patterns, security vulnerabilities, test coverage, and code smell.

## Trigger Conditions
- Activated when task requires capability: `code-review-standards`
- Invoked by specialist agents in category `development`

## Required Inputs
```json
{
  "code_diff": "Unified git diff string",
  "language": "python | typescript | go"
}
```

## Execution Instructions
Check for: 1. Resource leaks; 2. Unhandled nulls/exceptions; 3. Security vulnerabilities (eval, injection); 4. Test coverage; 5. Idiomatic style.

## Expected Outputs
```json
{
  "passed": "boolean",
  "severity_issues": "list",
  "suggested_patch": "string"
}
```

## Limitations & Security
- **Limitation:** Static inspection; does not execute untrusted binaries directly
- **Security:** Never execute untrusted code in local root context
