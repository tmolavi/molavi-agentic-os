---
name: Unslop Writing Humanizer
description: Strip repetitive AI clichés ('delve', 'testament', 'tapestry', 'game-changer') and produce clean, natural human prose.
category: writing
version: 1.0.0
author: Taqi Molavi
license: MIT
---

# Unslop Writing Humanizer

Strip repetitive AI clichés ('delve', 'testament', 'tapestry', 'game-changer') and produce clean, natural human prose.

## Trigger Conditions
- Activated when task requires capability: `unslop-humanizer`
- Invoked by specialist agents in category `writing`

## Required Inputs
```json
{
  "draft_text": "AI generated or draft text"
}
```

## Execution Instructions
Scan text against known AI cliché dictionaries. Replace inflated academic phrases with direct, crisp, natural conversational language.

## Expected Outputs
```json
{
  "humanized_text": "Cleaned prose",
  "slop_patterns_removed": "list"
}
```

## Limitations & Security
- **Limitation:** Preserves core technical meaning without distortion
- **Security:** Does not alter factual claims or verified citations
