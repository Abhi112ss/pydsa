METADATA = {
    "id": 2636,
    "name": "Promise Pool",
    "slug": "promise_pool",
    "category": "Design",
    "aliases": [],
    "tags": ["concurrency", "design", "asyncio"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(k)",
    "description": "Implement a promise pool that limits the number of concurrent tasks to a maximum of k.",
}

import asyncio

class PromisePool:
    """
    A class to manage a pool of concurrent tasks with a limit on concurrency.
    """

    def __init__(self, k: int):
        """
        Initializes the PromisePool with a maximum concurrency limit.

        Args:
            k (int): The maximum number of concurrent tasks allowed.
        """
        self.k = k
        self.semaphore = asyncio.Semaphore(k)

    async def run(self, tasks: list[callable]) -> list[any]:
        """
        Executes a list of tasks with a maximum of k tasks running concurrently.

        Args:
            tasks (list[callable]): A list of asynchronous functions (tasks) to execute.

        Returns:
            list[any]: A list of results from the tasks in the same order as the input.

        Examples:
            >>> async def task(i):
            ...     await asyncio.sleep(0.1)
            ...     return i
            >>> pool = PromisePool(2)
            >>> await pool.run([lambda: task(i) for i in range(5)])
            [0, 1, 2, 3, 4]
        """
        
        async def worker(task_func: callable) -> any:
            """
            A wrapper to ensure each task respects the semaphore limit.
            """
            # Acquire a slot in the semaphore before starting the task
            async with self.semaphore:
                # Execute the provided task function
                return await task_func()

        # Create a list of coroutine objects by wrapping each task in the worker
        # We use a list comprehension to prepare all tasks, but they won't 
        # all run at once because of the semaphore inside the worker.
        wrapped_tasks = [worker(t) for t in tasks]

        # asyncio.gather schedules the coroutines and waits for all to complete,
        # preserving the original order of the results.
        return await asyncio.gather(*wrapped_tasks)

async def solve():
    """
    Example usage of the PromisePool class.
    """
    async def mock_task(task_id: int, delay: float) -> int:
        await asyncio.sleep(delay)
        return task_id

    # Create a list of lambda functions to simulate tasks
    tasks = [
        lambda i=i: mock_task(i, 0.1) for i in range(5)
    ]

    pool = PromisePool(k=2)
    results = await pool.run(tasks)
    print(f"Results: {results}")
