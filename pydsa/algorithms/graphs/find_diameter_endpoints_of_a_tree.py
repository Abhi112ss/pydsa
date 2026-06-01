METADATA = {
    "id": 3787,
    "name": "Find Diameter Endpoints of a Tree",
    "slug": "find_diameter_endpoints_of_a_tree",
    "category": "Trees",
    "aliases": [],
    "tags": ["trees", "bfs", "graph"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Find the two nodes that form the endpoints of the longest path (diameter) in a tree.",
}

from collections import deque

def solve(n: int, edges: list[list[int]]) -> list[int]:
    """
    Finds the two endpoints of the diameter of a tree.

    The diameter of a tree is the longest path between any two nodes.
    The algorithm uses two BFS traversals:
    1. Start from an arbitrary node (0) to find the farthest node (u).
    2. Start from node (u) to find the farthest node (v).
    The pair (u, v) represents the endpoints of the diameter.

    Args:
        n: The number of nodes in the tree.
        edges: A list of undirected edges where edges[i] = [u, v].

    Returns:
        A list of two integers representing the endpoints of the diameter,
        sorted in ascending order.

    Examples:
        >>> solve(5, [[0, 1], [1, 2], [1, 3], [3, 4]])
        [2, 4]
        >>> solve(2, [[0, 1]])
        [0, 1]
    """
    if n <= 1:
        return [0, 0] if n == 1 else []

    # Build adjacency list
    adj: dict[int, list[int]] = {i: [] for i in range(n)}
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)

    def get_farthest_node(start_node: int) -> tuple[int, int]:
        """
        Performs BFS to find the farthest node from the start_node.

        Returns:
            A tuple containing (farthest_node, distance).
        """
        distances: dict[int, int] = {start_node: 0}
        queue: deque[int] = deque([start_node])
        farthest_node = start_node
        max_dist = 0

        while queue:
            curr = queue.popleft()
            curr_dist = distances[curr]

            if curr_dist > max_dist:
                max_dist = curr_dist
                farthest_node = curr

            for neighbor in adj[curr]:
                if neighbor not in distances:
                    distances[neighbor] = curr_dist + 1
                    queue.append(neighbor)
        
        return farthest_node, max_dist

    # Step 1: Find one endpoint of the diameter by starting from node 0
    u, _ = get_farthest_node(0)

    # Step 2: Find the other endpoint by starting from node u
    v, _ = get_farthest_node(u)

    # Return endpoints in ascending order as per standard convention
    return sorted([u, v])
