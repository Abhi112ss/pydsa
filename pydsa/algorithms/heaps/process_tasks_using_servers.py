METADATA = {
    "id": 1882,
    "name": "Process Tasks Using Servers",
    "slug": "process-tasks-using-servers",
    "category": "Heap",
    "aliases": [],
    "tags": ["heap", "priority_queue", "greedy"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Assign tasks to the first available server with the smallest index, or the one that becomes free earliest.",
}

import heapq

def solve(tasks: list[list[int]], servers: list[int]) -> list[int]:
    """
    Assigns tasks to servers based on availability and index.

    Args:
        tasks: A list of tasks where tasks[i] = [enqueueTime, processingTime].
        servers: A list of integers representing the capacity of each server.

    Returns:
        A list of integers representing the server index assigned to each task.

    Examples:
        >>> solve([[1, 2], [2, 3], [3, 9], [2, 6]], [1, 2])
        [0, 1, 0, 0]
    """
    n_tasks = len(tasks)
    n_servers = len(servers)
    results = [0] * n_tasks

    # available_servers: min-heap of (server_index)
    # We use this to quickly find the smallest index among free servers.
    available_servers = []
    for i in range(n_servers):
        heapq.heappush(available_servers, i)

    # busy_servers: min-heap of (free_at_time, server_index)
    # We use this to track when servers will become available again.
    busy_servers = []
    
    # current_time tracks the progression of time.
    current_time = 0
    
    # Pointer to track which tasks have been processed.
    task_idx = 0

    while task_idx < n_tasks:
        enqueue_time, processing_time = tasks[task_idx]
        
        # If no servers are available, jump time to the next moment a server becomes free
        # or to the time the current task is actually enqueued.
        if not available_servers and busy_servers[0][0] > current_time:
            current_time = max(current_time, busy_servers[0][0])
        
        # Ensure current_time is at least the enqueue time of the current task.
        current_time = max(current_time, enqueue_time)

        # 1. Move all servers that have finished their tasks by current_time to available_servers.
        while busy_servers and busy_servers[0][0] <= current_time:
            _, server_idx = heapq.heappop(busy_servers)
            heapq.heappush(available_servers, server_idx)

        # 2. If no servers are available even after updating, we must wait for the next busy server.
        if not available_servers:
            current_time = busy_servers[0][0]
            while busy_servers and busy_servers[0][0] <= current_time:
                _, server_idx = heapq.heappop(busy_servers)
                heapq.heappush(available_servers, server_idx)

        # 3. Assign the task to the available server with the smallest index.
        server_idx = heapq.heappop(available_servers)
        results[task_idx] = server_idx
        
        # Calculate when this server will be free again.
        free_at = current_time + processing_time
        heapq.heappush(busy_servers, (free_at, server_idx))
        
        task_idx += 1

    return results
