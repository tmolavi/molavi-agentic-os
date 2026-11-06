---
name: Technical SEO & Core Web Vitals Audit
description: Diagnose crawlability, response headers, canonicalization, schema markup, and performance metrics for websites.
category: seo
version: 1.0.0
author: Taqi Molavi
license: MIT
---

# Technical SEO & Core Web Vitals Audit

Diagnose crawlability, response headers, canonicalization, schema markup, and performance metrics for websites.

## Trigger Conditions
- Activated when task requires capability: `seo-audit`
- Invoked by specialist agents in category `seo`

## Required Inputs
```json
{
  "url": "Target URL to inspect",
  "check_cwv": "boolean"
}
```

## Execution Instructions
Inspect HTTP headers (status, content-type, cache-control). Extract meta title, description, robots tags, OpenGraph tags, and JSON-LD scripts.

## Expected Outputs
```json
{
  "status_code": "integer",
  "meta_tags": "object",
  "schema_valid": "boolean",
  "recommendations": "list"
}
```

## Limitations & Security
- **Limitation:** Does not alter remote server settings
- **Security:** Rate limit requests to avoid triggering web application firewalls
