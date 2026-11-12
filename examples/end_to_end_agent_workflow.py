"""End-to-End Autonomous Agent Execution Flow.

Demonstrates the complete canonical TM Agentic OS pipeline:
1. User Request Received
2. Agent Selection from Registry
3. Skill Discovery & Parameter Matching
4. Tool Execution (via ToolRegistry & MCP Gateway)
5. Structured Output Generation
6. Independent Foreman Verification ("No Guessing")
7. Final Verified Delivery
"""

import sys
import os
import json
import time

# Ensure package is on sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from molavi_agentic_os.tools import ToolDefinition, ToolParameter, ToolRegistry
from molavi_agentic_os.mcp import MCPGateway
from molavi_agentic_os.evaluation import ForemanVerificationGate, VerificationArtifact, AgentOutputEvaluator


def mock_crawl_page(url: str, extract_headings: bool = True) -> dict:
    """Mock handler for deterministic web inspection."""
    return {
        "url": url,
        "title": "Molavi AI Systems Architecture — Production Agentic OS",
        "headings": ["Overview", "Core Architecture", "Foreman Verification", "Benchmarks"],
        "word_count": 1420,
        "status_code": 200
    }


def main():
    print("=" * 70)
    print("TM MOLAVI AGENTIC OS — END-TO-END AGENT WORKFLOW EXAMPLE")
    print("=" * 70)

    # 1. User Request
    user_prompt = "Perform a technical audit on 'https://molavi.pro/research' and verify headings."
    print(f"\n[STEP 1] User Request Received:\n  '{user_prompt}'")

    # 2. Agent Selection
    selected_agent_id = "seo-auditor"
    agent_role = "Senior Technical SEO & Citability Auditor"
    print(f"\n[STEP 2] Agent Selection:\n  Target Agent: {selected_agent_id} ({agent_role})")

    # 3. Skill & Tool Discovery
    print("\n[STEP 3] Skill Discovery & Tool Registration:")
    crawl_tool = ToolDefinition(
        name="web_crawl",
        description="Extracts page headings, DOM metadata, and word count from target URL.",
        parameters=[
            ToolParameter("url", "string", "Target URL to inspect", required=True),
            ToolParameter("extract_headings", "boolean", "Whether to extract H1-H3 headings", required=False, default=True)
        ],
        handler=mock_crawl_page
    )
    registry = ToolRegistry()
    registry.register(crawl_tool)
    mcp_gateway = MCPGateway(registry=registry)
    print(f"  Discovered Tool: '{crawl_tool.name}' | Schema properties: {list(crawl_tool.to_json_schema()['properties'].keys())}")

    # 4. Tool Execution via MCP Gateway
    print("\n[STEP 4] Executing Tool via MCP Gateway:")
    tool_args = {"url": "https://molavi.pro/research", "extract_headings": True}
    mcp_call_result = mcp_gateway.handle_call_tool("web_crawl", tool_args)
    print(f"  MCP Execution Success: {not mcp_call_result['isError']}")
    parsed_output = json.loads(mcp_call_result["content"][0]["text"])
    print(f"  Extracted Title: {parsed_output['title']}")
    print(f"  Headings Found: {parsed_output['headings']}")

    # 5. Structured Output Generation
    print("\n[STEP 5] Agent Structured Output Generation:")
    agent_result = {
        "status": "completed",
        "agent": selected_agent_id,
        "target_url": parsed_output["url"],
        "audit_summary": f"Audit passed with {len(parsed_output['headings'])} primary sections identified.",
        "evidence": [
            f"HTTP 200 verified on {parsed_output['url']}",
            f"Title matched: '{parsed_output['title']}'",
            f"Headings parsed: {', '.join(parsed_output['headings'])}"
        ]
    }
    print(json.dumps(agent_result, indent=2))

    # 6. Independent Foreman Verification Gate ("No Guessing")
    print("\n[STEP 6] Foreman Anti-Hallucination Verification Gate:")
    artifacts = [
        VerificationArtifact("url_crawled", "string", parsed_output["url"], True),
        VerificationArtifact("headings_extracted", "list", parsed_output["headings"], True),
    ]
    gate_decision = ForemanVerificationGate.verify(agent_result, artifacts)
    print(f"  Foreman Decision: {'PASS (Verified)' if gate_decision.is_verified else 'REJECTED'}")
    print(f"  Verified Artifacts: {gate_decision.verified_artifacts}")

    # 7. Independent Quality Evaluation Score
    expected_schema = {"status": str, "agent": str, "target_url": str, "evidence": list}
    score = AgentOutputEvaluator.evaluate(agent_result, expected_schema)
    print(f"\n[STEP 7] Final Independent Evaluation Score: {score.total_score:.1f}/100.0 (Passed: {score.is_passed})")
    print("\nWorkflow successfully completed with full mathematical provenance.\n")


if __name__ == "__main__":
    main()
