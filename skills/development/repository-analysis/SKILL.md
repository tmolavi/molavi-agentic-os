---
name: Repository Analysis & Codebase Discovery
description: Deep codebase inspection, dependency mapping, runtime profiling, and architectural discovery.
category: development
version: 1.0.0
author: Taqi Molavi
license: MIT
---

# Repository Analysis & Codebase Discovery

Deep codebase inspection, dependency mapping, runtime profiling, and architectural discovery.

## Trigger Conditions
- Activated when onboarding an agent to a new repository or workspace.
- Invoked before proposing code modifications or system refactoring.

## Required Inputs
```json
{
  "repository_path": "string",
  "inspection_depth": "string"
}
```

## Execution Instructions
1. Discover project layout, lockfiles, configuration manifests, and CI/CD workflows.
2. Map internal dependency graph and identify external package versions.
3. Verify git history, active branches, and unstaged modifications.
4. Locate test suites and identify non-destructive verification commands.

## Expected Outputs
```json
{
  "tech_stack": "object",
  "entry_points": "list",
  "test_commands": "list",
  "governance_status": "string"
}
```

## Limitations & Security
- **Limitation:** Read-only inspection; does not alter repository code.
- **Security:** Secret scanning is executed automatically to prevent logging sensitive environment files.
