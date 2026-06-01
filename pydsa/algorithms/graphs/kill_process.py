METADATA = {
    "id": 582,
    "name": "Kill Process",
    "slug": "kill-process",
    "category": "Graph",
    "aliases": [],
    "tags": ["bfs", "dfs", "hash_map", "tree"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Find the total number of processes that will be killed when a specific process ID is terminated, given a list of parent-child relationships.",
}

def solve(processes: list[list[int]], pid_to_kill: int) -> int:
    """
    Calculates the total number of processes killed when a specific PID is terminated.
    
    A process kills all its descendants in the process tree.

    Args:
        processes: A list of pairs where processes[i] = [pid_i, parent_i].
                   The parent of the root process is 0.
        pid_to_kill: The ID of the process to be terminated.

    Returns:
        The total count of processes (including the target) that are killed.

    Examples:
        >>> solve([[1, 5], [2, 5], [3, 5], [4, 4], [5, 0]], 4)
        1
        >>> solve([[1, 5], [2, 5], [3, 5], [4, 4], [5, 0]], 5)
        5
    """
    # Build an adjacency list representing the tree structure: parent -> [children]
    # This allows us to traverse downwards from any given node.
    adjacency_list: dict[int, list[int]] = {}
    for pid, parent in processes:
        if parent not in adjacency_list:
            adjacency_list[parent] = []
        adjacency_list[parent].append(pid)

    # If the target PID has no children, only the target itself is killed.
    if pid_to_kill not in adjacency_list:
        return 1

    # Perform a Breadth-First Search (BFS) to count all descendants.
    # We start from the pid_to_kill and visit all its children, grandchildren, etc.
    killed_count = 0
    queue: list[int] = [pid_to_kill]
    
    # Using a simple pointer for the queue to maintain O(1) pop-like behavior 
    # without using collections.deque for a single-file script.
    head = 0
    while head < len(queue):
        current_pid = queue[head]
        head += 1
        killed_count += 1
        
        # If the current process has children, add them to the queue to be processed.
        if current_pid in adjacency_list:
            for child in adjacency_list[current_pid]:
                queue.append(child)

    return killed_count
