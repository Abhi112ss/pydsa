METADATA = {
    "id": 2071,
    "name": "Maximum Number of Tasks You Can Assign",
    "slug": "maximum-number-of-tasks-you-can-assign",
    "category": "Greedy",
    "aliases": [],
    "tags": ["greedy", "sorting", "two_pointer", "binary_search"],
    "difficulty": "hard",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Find the maximum number of tasks that can be completed given task requirements and worker capabilities.",
}

def solve(tasks: list[int], workers: list[int]) -> int:
    """
    Calculates the maximum number of tasks that can be assigned to workers.

    Each task requires a minimum worker capability, and each worker can 
    perform at most one task.

    Args:
        tasks: A list of integers representing the minimum capability required for each task.
        workers: A list of integers representing the capability of each worker.

    Returns:
        The maximum number of tasks that can be completed.

    Examples:
        >>> solve([1, 2, 3], [1, 1])
        2
        >>> solve([1, 2, 3], [3, 3, 3])
        3
        >>> solve([10, 20, 30], [5, 15, 25])
        2
    """
    # Sort both to allow for a greedy approach during validation
    tasks.sort()
    workers.sort()

    def can_assign(k: int) -> bool:
        """
        Checks if it is possible to complete k tasks.
        
        To maximize the chance of success, we pick the k smallest tasks 
        and the k largest workers. We then match the smallest task 
        with the smallest capable worker among the selected subset.
        """
        if k == 0:
            return True
        
        # We take the k smallest tasks
        selected_tasks = tasks[:k]
        # We take the k largest workers to give us the best chance
        selected_workers = workers[-k:]
        
        # Greedy matching: smallest task with smallest available worker
        # Since both are sorted, we can use two pointers or a simple loop
        for i in range(k):
            if selected_tasks[i] > selected_workers[i]:
                return False
        return True

    # Binary search on the number of tasks (range [0, min(len(tasks), len(workers))])
    low = 0
    high = min(len(tasks), len(workers))
    result = 0

    while low <= high:
        mid = (low + high) // 2
        if can_assign(mid):
            result = mid
            low = mid + 1
        else:
            high = mid - 1

    return result
