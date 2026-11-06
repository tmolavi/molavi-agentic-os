"""Tests for queue, task status, and execution engine."""

import pytest
from molavi_agentic_os.orchestration.task import Task, TaskStatus, TaskResult
from molavi_agentic_os.orchestration.queue import TaskQueue
from molavi_agentic_os.orchestration.engine import OrchestrationEngine

def test_task_queue_parallel():
    q = TaskQueue(max_workers=2)
    t1 = Task(name="Task 1", action="action1", agent_id="agent1")
    t2 = Task(name="Task 2", action="action2", agent_id="agent2")

    q.submit(t1, priority=1)
    q.submit(t2, priority=2)

    def dummy_runner(t: Task) -> TaskResult:
        return TaskResult(success=True, output={"status": f"done_{t.name}"})

    results = q.run_worker_pool(dummy_runner)
    assert len(results) == 2
    assert results[t1.task_id].success is True
    assert t1.status == TaskStatus.COMPLETED

def test_orchestration_dag():
    engine = OrchestrationEngine(max_workers=2)
    t1 = Task(task_id="t1", name="Step 1", action="step1", agent_id="agent1")
    t2 = Task(task_id="t2", name="Step 2", action="step2", agent_id="agent2", depends_on=["t1"])

    def dummy_runner(t: Task) -> TaskResult:
        return TaskResult(success=True, output={"done": t.task_id})

    results = engine.execute_dag([t2, t1], dummy_runner)
    assert results["t1"].success is True
    assert results["t2"].success is True
