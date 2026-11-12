---
name: Systematic Debugging & Error Isolation
description: Root-cause debugging, trace analysis, and non-destructive reproduction for complex systems.
category: development
version: 1.0.0
author: Taqi Molavi
license: MIT
---

# Systematic Debugging & Error Isolation

Root-cause debugging, trace analysis, and non-destructive reproduction for complex systems.

## Trigger Conditions
- Activated when unit tests fail, runtime exceptions are thrown, or unintended behavior is detected.
- Invoked by developer agents and code reviewers.

## Required Inputs
```json
{
  "error_trace": "string",
  "reproduction_command": "string",
  "affected_files": "list"
}
```

## Execution Instructions
1. Parse stack trace to isolate exact failure origin and line numbers.
2. Build minimal, non-destructive reproduction script or test double.
3. Formulate falsifiable hypothesis regarding the failure mechanism.
4. Apply targeted, surgical fix preserving surrounding code patterns.
5. Re-run verification suite to confirm error resolution without regression.

## Expected Outputs
```json
{
  "root_cause": "string",
  "fix_summary": "string",
  "regression_test_status": "string"
}
```

## Limitations & Security
- **Limitation:** Does not auto-apply breaking schema changes without human review.
- **Security:** Masks passwords, keys, and tokens from error stack traces.
