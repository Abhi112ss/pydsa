METADATA = {
    "id": 2365,
    "name": "Task Scheduler II",
    "slug": "task-scheduler-ii",
    "category": "Greedy",
    "aliases": [],
    "tags": ["greedy", "hash_map"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(k)",
    "description": "Calculate the minimum number of days required to complete a sequence of tasks given a minimum gap between identical tasks.",
}

def solve(tasks: list[int], gap: int) -> int:
    """
    Calculates the minimum number of days required to complete all tasks.

    Each task must be performed on a specific day. If a task is repeated, 
    there must be at least 'gap' days between the current task and the 
    previous occurrence of the same task.

    Args:
        tasks: A list of integers representing the task IDs.
        gap: The minimum number of days required between two identical tasks.

    Returns:
        The total number of days required to complete all tasks.

    Examples:
        >>> solve([1, 2, 1, 2, 3, 1], 3)
        10
        >>> solve([1, 1, 1], 2)
        7
    """
    # current_day tracks the day index we are currently on (1-indexed)
    current_day = 0
    
    # last_performed_day maps task_id -> the day it was last completed
    last_performed_day: dict[int, int] = {}

    for task in tasks:
        # Move to the next day to attempt the current task
        current_day += 1
        
        if task in last_performed_day:
            # Calculate the earliest possible day this task can be performed again
            # The gap requirement means: current_day > last_day + gap
            # So, current_day must be at least last_day + gap + 1
            earliest_allowed_day = last_performed_day[task] + gap + 1
            
            # If the current day is earlier than the allowed day, jump to it
            if current_day < earliest_allowed_day:
                current_day = earliest_allowed_day
        
        # Record the day this task was completed
        last_performed_day[task] = current_day

    return current_day
