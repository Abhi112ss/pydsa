METADATA = {
    "id": 1953,
    "name": "Maximum Number of Weeks for Which You Can Work",
    "slug": "maximum-number-of-weeks-for-which-you-can-work",
    "category": "Greedy",
    "aliases": [],
    "tags": ["greedy", "math"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Calculate the maximum number of weeks you can work given task counts for different types, ensuring no two consecutive weeks have the same task type.",
}

def solve(tasks: list[int]) -> int:
    """
    Calculates the maximum number of weeks you can work such that no two 
    consecutive weeks have the same task type.

    The problem is a variation of the scheduling problem. If the most frequent 
    task type has more than half of the total tasks (plus one if we consider 
    alternating), it will eventually force two consecutive weeks of the same 
    task. Otherwise, we can arrange all tasks to work every single week.

    Args:
        tasks: A list of integers where tasks[i] is the number of tasks of type i.

    Returns:
        The maximum number of weeks you can work.

    Examples:
        >>> solve([1, 2, 3])
        6
        >>> solve([10, 1, 1])
        3
    """
    total_tasks = sum(tasks)
    max_tasks = max(tasks)
    
    # The number of 'other' tasks available to act as separators
    other_tasks = total_tasks - max_tasks
    
    # If the most frequent task is so large that even using all other tasks 
    # as separators cannot prevent two identical tasks from being adjacent.
    # The maximum number of the most frequent task we can use is (other_tasks + 1).
    if max_tasks > other_tasks + 1:
        # We can use all 'other_tasks' and (other_tasks + 1) of the max_tasks.
        # Total weeks = other_tasks + (other_tasks + 1)
        return 2 * other_tasks + 1
    
    # Otherwise, we can arrange all tasks such that no two are consecutive.
    return total_tasks
