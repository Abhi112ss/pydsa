METADATA = {
    "id": 847,
    "name": "Shortest Path Visiting All Nodes",
    "slug": "shortest-path-visiting-all-nodes",
    "category": "Graph",
    "aliases": [],
    "tags": ["bfs", "bitmask", "dynamic_programming", "graph"],
    "difficulty": "hard",
    "time_complexity": "O(n * 2^n)",
    "space_complexity": "O(n * 2^n)",
    "description": "Find the length of the shortest path that visits every node in an undirected graph.",
}

from collections import deque

def solve(graph: list[list[int]]) -> int:
    """
    Finds the shortest path length that visits all nodes in an undirected graph.

    Args:
        graph: An adjacency list where graph[i] is a list of nodes adjacent to node i.

    Returns:
        The minimum number of edges to visit all nodes.

    Examples:
        >>> solve([[1,2,3],[0],[0],[0]])
        4
        >>> solve([[1],[0]])
        1
    """
    n = len(graph)
    if n <= 1:
        return 0

    # The target state is when all bits are set to 1 in the bitmask.
    # For n nodes, the mask is (1 << n) - 1.
    target_mask = (1 << n) - 1
    
    # Queue for BFS: stores tuples of (current_node, visited_mask, current_distance)
    queue = deque()
    
    # visited_states stores (node, mask) to prevent redundant processing.
    # A state is defined by the current node and the set of nodes visited so far.
    visited_states = set()

    # We can start the path from any node.
    for start_node in range(n):
        initial_mask = 1 << start_node
        queue.append((start_node, initial_mask, 0))
        visited_states.add((start_node, initial_mask))

    while queue:
        current_node, current_mask, distance = queue.popleft()

        # If all nodes have been visited, return the distance immediately.
        # Since we use BFS, the first time we hit this, it's the shortest path.
        if current_mask == target_mask:
            return distance

        # Explore neighbors
        for neighbor in graph[current_node]:
            new_mask = current_mask | (1 << neighbor)
            
            # Check if this specific (node, mask) combination has been seen before.
            # This allows revisiting nodes but not revisiting the same state.
            if (neighbor, new_mask) not in visited_states:
                visited_states.add((neighbor, new_mask))
                queue.append((neighbor, new_mask, distance + 1))

    return -1
