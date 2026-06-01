METADATA = {
    "id": 2895,
    "name": "Minimum Processing Time",
    "slug": "minimum-processing-time",
    "category": "Greedy",
    "aliases": [],
    "tags": ["greedy", "sorting"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(1)",
    "description": "Find the minimum total processing time by pairing tasks and workers optimally.",
}

def solve(tasks: list[int], workers: list[int]) -> int:
    """
    Calculates the minimum total processing time for a set of tasks and workers.
    
    To minimize the sum of max(task, worker), we should pair the largest tasks 
    with the largest workers. This is a greedy approach where sorting both 
    arrays allows us to align the magnitudes.

    Args:
        tasks: A list of integers representing the time required for each task.
        workers: A list of integers representing the processing capacity of each worker.

    Returns:
        The minimum possible total processing time.

    Examples:
        >>> solve([3, 5], [2, 4])
        9
        >>> solve([1, 2, 3], [1, 2, 3])
        6
    """
    # Sort both lists to pair the largest tasks with the largest workers.
    # This minimizes the 'waste' or the impact of the max() function.
    tasks.sort()
    workers.sort()
    
    total_processing_time = 0
    
    # Iterate through both lists simultaneously.
    # Since both are sorted, tasks[i] and workers[i] are paired optimally.
    for task_time, worker_capacity in zip(tasks, workers):
        total_processing_time += max(task_time, worker_capacity)
        
    return total_processing_time
