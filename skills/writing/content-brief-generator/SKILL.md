---
name: Content Brief & Topic Cluster Generator
description: Generate comprehensive editorial briefs with search intent, heading hierarchy, target entities, and FAQ blocks.
category: writing
version: 1.0.0
author: Taqi Molavi
license: MIT
---

# Content Brief & Topic Cluster Generator

Generate comprehensive editorial briefs with search intent, heading hierarchy, target entities, and FAQ blocks.

## Trigger Conditions
- Activated when task requires capability: `content-brief-generator`
- Invoked by specialist agents in category `writing`

## Required Inputs
```json
{
  "topic": "Target keyword or theme",
  "target_audience": "Audience persona"
}
```

## Execution Instructions
Analyze intent. Construct structured H1/H2/H3 outline. Include high-value semantic entities, target keywords, and recommended word counts.

## Expected Outputs
```json
{
  "h1": "string",
  "h2_sections": "list",
  "target_entities": "list",
  "faq_questions": "list"
}
```

## Limitations & Security
- **Limitation:** Requires clear topic definition
- **Security:** Ensure copyright originality in brief outlines
