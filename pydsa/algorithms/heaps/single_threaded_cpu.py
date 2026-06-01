METADATA = {
    "id": 1834,
    "name": "Single-Threaded CPU",
    "slug": "single-threaded-cpu",
    "category": "Heap",
    "aliases": [],
    "tags": ["heap", "sorting", "priority queue"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Simulate a single-threaded CPU processing tasks based on arrival time and processing duration using a priority queue.",
}

import heapq

def solve(enqueue_time: list[int], processing_time: list[int]) -> list[int]:
    """
    Simulates a single-threaded CPU processing tasks.

    The CPU picks the task with the shortest processing time among available tasks.
    If multiple tasks have the same shortest processing time, the one with the 
    smallest index is picked.

    Args:
        enqueue_time: A list of integers representing the time each task becomes available.
        processing_time: A list of integers representing the duration of each task.

    Returns:
        A list of integers representing the order in which tasks are processed.

    Examples:
        >>> solve([1, 2, 3, 4], [1, 2, 3, 4])
        [0, 1, 2, 3]
        >>> solve([10, 2, 5], [5, 10, 2])
        [1, 2, 0]
    """
    n = len(enqueue_time)
    # Combine tasks into a list of tuples (arrival_time, processing_time, original_index)
    # and sort them by arrival time to process them as they become available.
    tasks = []
    for i in range(n):
        tasks.append((enqueue_time[i], processing_time[i], i))
    tasks.sort()

    result = []
    available_tasks_heap = []  # Min-heap storing (processing_time, original_index)
    current_time = 0
    task_idx = 0

    while task_idx < n or available_tasks_heap:
        # If no tasks are currently available and the CPU is idle, 
        # jump current_time to the arrival time of the next available task.
        if not available_tasks_heap and current_time < tasks[task_idx][0]:
            current_time = tasks[task_idx][0]

        # Add all tasks that have arrived by the current_time into the priority queue.
        while task_idx < n and tasks[task_idx][0] <= current_time:
            arrival, duration, index = tasks[task_idx]
            heapq.heappush(available_tasks_heap, (duration, index))
            task_idx += 1

        # Process the task with the shortest duration (and smallest index as tie-breaker).
        if available_tasks_heap:
            duration, index = heapq.heappop(available_tasks_heap)
            result.append(index)
            # Advance the CPU clock by the duration of the processed task.
            current_time += duration

    return result
