"""Orchestration Engine coordinating DAG execution and verification."""

from typing import Dict, List, Any, Callable
from .task import Task, TaskStatus, TaskResult
from .queue import TaskQueue

class OrchestrationEngine:
    """Executes multi-step agent workflows with dependency resolution."""

    def __init__(self, max_workers: int = 4):
        self.queue = TaskQueue(max_workers=max_workers)

    def execute_dag(self, tasks: List[Task], runner: Callable[[Task], TaskResult]) -> Dict[str, TaskResult]:
        """Resolves dependencies and runs tasks in correct topological order."""
        completed: Dict[str, TaskResult] = {}
        remaining = {t.task_id: t for t in tasks}

        while remaining:
            # Find tasks whose dependencies are satisfied
            runnable = [
                t for t in remaining.values()
                if all(dep in completed and completed[dep].success for dep in t.depends_on)
            ]

            if not runnable:
                # Deadlock or unsatisfied dependency
                for t in remaining.values():
                    t.status = TaskStatus.FAILED
                    completed[t.task_id] = TaskResult(
                        success=False,
                        error=f"Unsatisfied dependencies: {t.depends_on}"
                    )
                break

            for t in runnable:
                self.queue.submit(t)

            batch_results = self.queue.run_worker_pool(runner)
            for tid, res in batch_results.items():
                completed[tid] = res
                if tid in remaining:
                    del remaining[tid]

        return completed
