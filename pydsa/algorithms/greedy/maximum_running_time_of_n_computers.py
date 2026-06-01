METADATA = {
    "id": 2141,
    "name": "Maximum Running Time of N Computers",
    "slug": "maximum-running-time-of-n-computers",
    "category": "Math",
    "aliases": [],
    "tags": ["greedy", "math", "sorting"],
    "difficulty": "hard",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(1)",
    "description": "Calculate the maximum total running time of n computers given a list of task durations, where each task must be completed by exactly one computer.",
}

def solve(n: int, tasks: list[int]) -> int:
    """
    Calculates the maximum total running time of n computers.
    
    The problem is a variation of the partition problem. To maximize the total time,
    we want to distribute tasks such that no single computer is idle while others 
    are working, unless a single task is so large that it dominates the schedule.
    
    The maximum time is constrained by two factors:
    1. The total sum of all tasks.
    2. The capacity of the n-1 computers to 'buffer' the largest task. 
       If the largest task is greater than the sum of all other tasks, 
       the maximum time is limited to 2 * (sum of all other tasks).
       More generally, the maximum time is min(sum(tasks), 2 * (sum(tasks) - max(tasks))).

    Args:
        n: The number of computers available.
        tasks: A list of integers representing the duration of each task.

    Returns:
        The maximum total running time possible.

    Examples:
        >>> solve(3, [1, 2, 3, 4, 5])
        15
        >>> solve(2, [1, 10])
        2
        >>> solve(3, [1, 1, 10])
        2
    """
    if not tasks:
        return 0
    
    total_sum = sum(tasks)
    max_task = max(tasks)
    sum_of_others = total_sum - max_task
    
    # If the largest task is larger than the sum of all other tasks,
    # the maximum time we can achieve is limited by the ability to 
    # pair the 'other' tasks with the large task.
    # Specifically, the largest task can only be 'covered' by the 
    # sum of others. The total time would be 2 * sum_of_others.
    # However, if n > 2, we can distribute the 'others' to maximize 
    # the overlap. But the constraint is actually simpler:
    # The maximum time is limited by 2 * (sum of all tasks except the largest)
    # if the largest task is very large.
    
    if max_task > sum_of_others:
        # The largest task is the bottleneck.
        # We can use the other tasks to 'sandwich' the large task.
        # The maximum time is 2 * sum_of_others.
        return 2 * sum_of_others
    else:
        # The tasks are balanced enough that we can utilize the full sum.
        return total_sum
