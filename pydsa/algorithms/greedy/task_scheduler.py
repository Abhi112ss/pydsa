METADATA = {
    "id": 621,
    "name": "Task Scheduler",
    "slug": "task-scheduler",
    "category": "Greedy",
    "aliases": [],
    "tags": ["greedy", "heap", "hash_map", "math"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Calculate the minimum number of units of time needed to complete all tasks given a cooling period.",
}

def solve(tasks: list[str], n: int) -> int:
    """
    Calculates the minimum time required to complete all tasks with a cooling period.

    The core logic uses a greedy approach based on the frequency of the most 
    frequent task. We calculate the number of 'idle' slots required by 
    arranging the most frequent tasks first and filling the gaps.

    Args:
        tasks: A list of task identifiers (strings).
        n: The cooling period required between two identical tasks.

    Returns:
        The minimum total time units required.

    Examples:
        >>> solve(["A","A","A","B","B","B"], 2)
        8
        >>> solve(["A","A","A","B","C","D","E"], 2)
        7
    """
    if not tasks:
        return 0

    # Count frequencies of each task
    # Since tasks are uppercase English letters, the map size is at most 26
    counts = {}
    for task in tasks:
        counts[task] = counts.get(task, 0) + 1

    # Find the maximum frequency
    max_freq = 0
    for count in counts.values():
        if count > max_freq:
            max_freq = count

    # Count how many tasks have that maximum frequency
    # These tasks will all occupy the last 'row' of our scheduling grid
    max_freq_tasks_count = 0
    for count in counts.values():
        if count == max_freq:
            max_freq_tasks_count += 1

    # The formula is derived from arranging the most frequent tasks:
    # We have (max_freq - 1) chunks of time.
    # Each chunk has a length of (n + 1) to account for the task and its cooling period.
    # The last chunk only contains the tasks that have the max frequency.
    # Formula: (max_freq - 1) * (n + 1) + max_freq_tasks_count
    
    # Example: A, A, A, B, B, B and n=2
    # Max freq = 3 (A and B), max_freq_tasks_count = 2
    # (3 - 1) * (2 + 1) + 2 = 2 * 3 + 2 = 8
    # Pattern: A B _ | A B _ | A B
    
    min_time_by_pattern = (max_freq - 1) * (n + 1) + max_freq_tasks_count

    # The actual time required is either the pattern-based time or the total 
    # number of tasks (if the number of tasks is so large that no idle time is needed).
    return max(len(tasks), min_time_by_pattern)
