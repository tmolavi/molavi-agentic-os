#!/usr/bin/env python3
"""Example: Running a combined SEO & GEO audit workflow."""

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from molavi_agentic_os.orchestration import OrchestrationEngine, Task, TaskResult
from molavi_agentic_os.evaluation import ForemanVerificationGate

def run_audit():
    print("Initializing Molavi SEO & GEO Audit Workflow...")
    engine = OrchestrationEngine(max_workers=2)

    tasks = [
        Task(
            task_id="t1-seo",
            name="Technical SEO Audit",
            action="seo-audit",
            agent_id="seo-auditor",
            inputs={"url": "https://example.com"}
        ),
        Task(
            task_id="t2-geo",
            name="Generative Engine Visibility",
            action="geo-visibility-audit",
            agent_id="geo-auditor",
            inputs={"brand": "Example Brand", "queries": ["best AI agency", "top SEO tools"]}
        ),
        Task(
            task_id="t3-report",
            name="Compile Executive Dossier",
            action="draft_report",
            agent_id="content-writer",
            depends_on=["t1-seo", "t2-geo"]
        )
    ]

    def runner(task: Task) -> TaskResult:
        print(f"  [RUNNING] {task.name} ({task.agent_id})...")
        return TaskResult(
            success=True,
            output={"status": "completed", "task": task.name},
            evidence=[f"https://example.com/audit/{task.task_id}"]
        )

    results = engine.execute_dag(tasks, runner)
    print("\nAudit Complete! Task Results:")
    for tid, res in results.items():
        print(f"  Task {tid}: success={res.success}, evidence={res.evidence}")

if __name__ == "__main__":
    run_audit()
