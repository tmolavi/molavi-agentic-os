"""Pure Python, zero-external-dependency Thread-Safe Task Queue."""

import queue
import threading
import time
import concurrent.futures
from typing import Dict, List, Optional, Callable
from .task import Task, TaskStatus, TaskResult

class TaskQueue:
    """In-memory thread-safe task queue with retry and timeout mechanisms."""

    def __init__(self, max_workers: int = 4):
        self._q: queue.PriorityQueue = queue.PriorityQueue()
        self._tasks: Dict[str, Task] = {}
        self._lock = threading.Lock()
        self.max_workers = max_workers
        self._counter = 0

    def submit(self, task: Task, priority: int = 10) -> str:
        with self._lock:
            self._counter += 1
            task.status = TaskStatus.QUEUED
            self._tasks[task.task_id] = task
            # Priority queue stores (priority, sequence_counter, task_id)
            self._q.put((priority, self._counter, task.task_id))
            return task.task_id

    def get_task(self, task_id: str) -> Optional[Task]:
        with self._lock:
            return self._tasks.get(task_id)

    def list_tasks(self) -> List[Task]:
        with self._lock:
            return list(self._tasks.values())

    def run_worker_pool(self, executor_fn: Callable[[Task], TaskResult]) -> Dict[str, TaskResult]:
        """Executes queued tasks using a thread pool until empty."""
        results = {}
        with concurrent.futures.ThreadPoolExecutor(max_workers=self.max_workers) as pool:
            futures = {}
            while not self._q.empty():
                _, _, task_id = self._q.get()
                task = self._tasks[task_id]
                task.status = TaskStatus.RUNNING
                fut = pool.submit(self._execute_with_safety, task, executor_fn)
                futures[fut] = task

            for fut in concurrent.futures.as_completed(futures):
                task = futures[fut]
                try:
                    res = fut.result()
                    task.result = res
                    task.status = TaskStatus.COMPLETED if res.success else TaskStatus.FAILED
                    task.completed_at = time.time()
                    results[task.task_id] = res
                except Exception as e:
                    task.status = TaskStatus.FAILED
                    task.result = TaskResult(success=False, error=str(e))
                    results[task.task_id] = task.result

        return results

    def _execute_with_safety(self, task: Task, fn: Callable[[Task], TaskResult]) -> TaskResult:
        start = time.time()
        try:
            res = fn(task)
            res.execution_time_seconds = time.time() - start
            return res
        except Exception as e:
            return TaskResult(
                success=False,
                error=str(e),
                execution_time_seconds=time.time() - start
            )
