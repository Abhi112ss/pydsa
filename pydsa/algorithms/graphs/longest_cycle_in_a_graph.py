METADATA = {
    "id": 2360,
    "name": "Longest Cycle in a Graph",
    "slug": "longest-cycle-in-a-graph",
    "category": "Graphs",
    "aliases": [],
    "tags": ["dfs", "graphs", "topological sort"],
    "difficulty": "hard",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Find the length of the longest cycle in a directed graph where each node has at most one outgoing edge.",
}

def solve(edges: list[int]) -> int:
    """
    Finds the length of the longest cycle in a directed graph where each node 
    has at most one outgoing edge.

    Args:
        edges: A list of integers where edges[i] is the destination of the edge 
               from node i. If edges[i] is -1, there is no outgoing edge.

    Returns:
        The length of the longest cycle found. Returns -1 if no cycle exists.

    Examples:
        >>> solve([3, 3, 4, 2, 3])
        3
        >>> solve([3, 3, 4, 2, -1, -1])
        3
        >>> solve([-1, -1])
        -1
    """
    n = len(edges)
    visited = [False] * n
    max_cycle_length = -1

    # We iterate through every node to ensure we cover disconnected components
    for start_node in range(n):
        if visited[start_node]:
            continue

        # Track nodes visited in the current traversal path and their distance from start
        current_path_map = {}
        curr = start_node
        distance = 0

        # Traverse the path until we hit a dead end or a node we've seen before
        while curr != -1 and not visited[curr]:
            visited[curr] = True
            current_path_map[curr] = distance
            curr = edges[curr]
            distance += 1

        # If we hit a node that was part of the CURRENT traversal, a cycle is found
        if curr != -1 and curr in current_path_map:
            cycle_length = distance - current_path_map[curr]
            max_cycle_length = max(max_cycle_length, cycle_length)
            
        # Note: If curr was already visited but NOT in current_path_map, 
        # it means we merged into a previously explored path that didn't lead to a new cycle.

    return max_cycle_length
