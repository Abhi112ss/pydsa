METADATA = {
    "id": 3668,
    "name": "Restore Finishing Order",
    "slug": "restore-finishing-order",
    "category": "Graphs",
    "aliases": [],
    "tags": ["topological_sort", "graphs", "dependency_resolution"],
    "difficulty": "medium",
    "time_complexity": "O(V + E)",
    "space_complexity": "O(V + E)",
    "description": "Determine a valid sequence of tasks given their dependencies using topological sorting.",
}

def solve(num_tasks: int, dependencies: list[tuple[int, int]]) -> list[int]:
    """
    Restores the finishing order of tasks based on their dependencies.
    
    A dependency (u, v) means task u must be completed before task v can start.
    This function uses Kahn's algorithm to find a valid topological sort.

    Args:
        num_tasks: The total number of tasks (labeled 0 to num_tasks - 1).
        dependencies: A list of tuples where each tuple (u, v) represents 
                      that task u must be finished before task v.

    Returns:
        A list of integers representing the valid order of tasks. 
        Returns an empty list if a cycle is detected (no valid order exists).

    Examples:
        >>> solve(3, [(0, 1), (1, 2)])
        [0, 1, 2]
        >>> solve(4, [(0, 1), (2, 3)])
        [0, 2, 1, 3]  # One of several valid orders
        >>> solve(2, [(0, 1), (1, 0)])
        []
    """
    # Build adjacency list and track in-degrees for each node
    adj_list: dict[int, list[int]] = {i: [] for i in range(num_tasks)}
    in_degree: list[int] = [0] * num_tasks

    for u, v in dependencies:
        adj_list[u].append(v)
        in_degree[v] += 1

    # Initialize queue with all nodes that have no incoming dependencies
    # Using a simple list as a queue for O(1) pop(0) is O(N), 
    # but for topological sort, a collections.deque is standard.
    # Since we only use stdlib, we'll use a list and a pointer or deque.
    from collections import deque
    queue: deque[int] = deque([i for i in range(num_tasks) if in_degree[i] == 0])
    
    finishing_order: list[int] = []

    while queue:
        current_task = queue.popleft()
        finishing_order.append(current_task)

        # Decrease in-degree for all neighbors
        for neighbor in adj_list[current_task]:
            in_degree[neighbor] -= 1
            
            # If in-degree becomes zero, all dependencies for this task are met
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    # If the finishing_order does not contain all tasks, a cycle exists
    if len(finishing_order) == num_tasks:
        return finishing_order
    else:
        return []
