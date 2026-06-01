METADATA = {
    "id": 3683,
    "name": "Earliest Time to Finish One Task",
    "slug": "earliest-time-to-finish-one-task",
    "category": "Greedy",
    "aliases": [],
    "tags": ["greedy", "sorting"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(1)",
    "description": "Find the earliest time to complete at least one task given processing requirements and deadlines.",
}

def solve(tasks: list[list[int]]) -> int:
    """
    Calculates the earliest time to finish at least one task.
    
    Each task is represented as [processing_time, deadline].
    To finish a task, the current time must be at least the processing_time,
    and the completion time (current_time + processing_time) must be <= deadline.
    However, the problem asks for the earliest time we can *start* or *finish* 
    based on the constraints. Given the greedy nature, we want to find the 
    minimum time required to satisfy the condition for any single task.

    Args:
        tasks: A list of lists where tasks[i] = [processing_time, deadline].

    Returns:
        The earliest time a task can be completed, or -1 if no task can be completed.

    Examples:
        >>> solve([[2, 5], [1, 2]])
        2
        >>> solve([[5, 4]])
        -1
    """
    # To minimize the completion time, we should look for tasks that can 
    # be completed as early as possible. The earliest a task can finish 
    # is simply its own processing time, provided that processing time 
    # does not exceed its deadline.
    
    earliest_finish_time = float('inf')
    can_complete_any = False

    for processing_time, deadline in tasks:
        # A task can be completed if its processing time is within its deadline
        if processing_time <= deadline:
            # The earliest this specific task can finish is at time 'processing_time'
            # assuming we start at time 0.
            if processing_time < earliest_finish_time:
                earliest_finish_time = processing_time
                can_complete_any = True

    return int(earliest_finish_time) if can_complete_any else -1
