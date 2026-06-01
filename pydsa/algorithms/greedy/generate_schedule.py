METADATA = {
    "id": 3680,
    "name": "Generate Schedule",
    "slug": "generate_schedule",
    "category": "Greedy",
    "aliases": [],
    "tags": ["greedy", "heap", "priority queue"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Generate an optimal task schedule based on priority and deadlines using a greedy approach with a priority queue.",
}

import heapq

def solve(tasks: list[dict[str, int]]) -> list[int]:
    """
    Generates an optimal schedule of task IDs based on priority and deadlines.
    
    The scheduling strategy follows a greedy approach:
    1. Sort tasks by their deadline to process them in chronological order.
    2. Use a min-heap to track the priorities of tasks currently in the schedule.
    3. If a task violates a deadline constraint, remove the task with the 
       lowest priority to make room for more valuable tasks.

    Args:
        tasks: A list of dictionaries where each dictionary contains:
            - 'id': The unique identifier for the task.
            - 'priority': The importance of the task (higher is better).
            - 'deadline': The latest time step by which the task must be completed.

    Returns:
        A list of task IDs representing the optimal schedule.

    Examples:
        >>> tasks = [{'id': 1, 'priority': 10, 'deadline': 1}, 
        ...          {'id': 2, 'priority': 20, 'deadline': 1}]
        >>> solve(tasks)
        [2]

        >>> tasks = [{'id': 1, 'priority': 5, 'deadline': 2}, 
        ...          {'id': 2, 'priority': 10, 'deadline': 1},
        ...          {'id': 3, 'priority': 15, 'deadline': 2}]
        >>> solve(tasks)
        [2, 3]
    """
    # Sort tasks by deadline to process them as time progresses
    sorted_tasks = sorted(tasks, key=lambda x: x['deadline'])
    
    # Min-heap to store priorities of tasks currently included in the schedule.
    # We store tuples of (priority, task_id) to handle ties and retrieval.
    # Using a min-heap allows us to easily discard the task with the lowest priority.
    scheduled_tasks_heap: list[tuple[int, int]] = []
    
    for task in sorted_tasks:
        task_id = task['id']
        priority = task['priority']
        deadline = task['deadline']
        
        # Add the current task to the potential schedule
        heapq.heappush(scheduled_tasks_heap, (priority, task_id))
        
        # If the number of tasks scheduled exceeds the current deadline,
        # we have a conflict. We must remove the task with the lowest priority
        # to maintain a valid schedule that respects the deadline constraints.
        if len(scheduled_tasks_heap) > deadline:
            heapq.heappop(scheduled_tasks_heap)
            
    # The heap contains the optimal set of tasks. 
    # We extract the IDs. Note: The problem usually asks for the set of tasks,
    # if a specific order is required (like by time), additional sorting is needed.
    # Here we return the IDs of the tasks that made it into the optimal set.
    result_ids = [item[1] for item in scheduled_tasks_heap]
    
    # Sorting the result by ID or original order is often expected in LeetCode 
    # unless specified otherwise; here we return them as they appear in the heap.
    return result_ids
