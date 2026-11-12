---
name: Web Intelligence & Deterministic Extraction
description: Zero-token headless crawling, DOM extraction, and web content parsing with local sanitization.
category: research
version: 1.0.0
author: Taqi Molavi
license: MIT
---

# Web Intelligence & Deterministic Extraction

Zero-token headless crawling, DOM extraction, and web content parsing with local sanitization.

## Trigger Conditions
- Activated when an agent requires real-time web context, competitive intelligence, or documentation crawls.
- Invoked by research agents and marketing analysts.

## Required Inputs
```json
{
  "target_urls": "list",
  "selectors": "list",
  "sanitize_html": "boolean"
}
```

## Execution Instructions
1. Retrieve target web content using HTTP client or headless browser.
2. Extract main article text, meta tags, OpenGraph data, and schema definitions.
3. Sanitize HTML, remove tracking scripts, and normalize text to Markdown.
4. Output structured JSON with cryptographic content hashes for verifiable citation.

## Expected Outputs
```json
{
  "extracted_pages": "list",
  "total_urls_processed": "integer",
  "status": "string"
}
```

## Limitations & Security
- **Limitation:** Respects robots.txt policies and rate limits.
- **Security:** Strips executable javascript and restricts crawling to public endpoints.
