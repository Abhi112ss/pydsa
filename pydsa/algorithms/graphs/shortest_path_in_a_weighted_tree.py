METADATA = {
    "id": 3515,
    "name": "Shortest Path in a Weighted Tree",
    "slug": "shortest_path_in_a_weighted_tree",
    "category": "Trees",
    "aliases": [],
    "tags": ["dfs", "bfs", "trees", "lca"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Find the unique shortest path distance between two nodes in a weighted tree.",
}

from typing import List, Dict, Tuple

def solve(n: int, edges: List[List[int]], start_node: int, end_node: int) -> int:
    """
    Calculates the shortest path distance between two nodes in a weighted tree.
    
    In a tree, there is exactly one simple path between any two nodes. 
    The shortest path is this unique path. We can find it using a simple 
    Depth First Search (DFS) to traverse the tree.

    Args:
        n: The number of nodes in the tree.
        edges: A list of edges where each edge is [u, v, weight].
        start_node: The starting node index.
        end_node: The target node index.

    Returns:
        The total weight of the unique path between start_node and end_node.

    Examples:
        >>> solve(3, [[0, 1, 5], [1, 2, 10]], 0, 2)
        15
        >>> solve(4, [[0, 1, 1], [0, 2, 2], [2, 3, 3]], 1, 3)
        6
    """
    # Build adjacency list: node -> list of (neighbor, weight)
    adj: Dict[int, List[Tuple[int, int]]] = {i: [] for i in range(n)}
    for u, v, w in edges:
        adj[u].append((v, w))
        adj[v].append((u, w))

    # Stack for iterative DFS: (current_node, parent_node, cumulative_distance)
    # Using parent_node to avoid going back up the tree without needing a 'visited' set
    stack: List[Tuple[int, int, int]] = [(start_node, -1, 0)]

    while stack:
        current, parent, current_dist = stack.pop()

        # If we reached the target node, return the accumulated distance
        if current == end_node:
            return current_dist

        # Explore neighbors
        for neighbor, weight in adj[current]:
            if neighbor != parent:
                # Push neighbor to stack with updated distance
                stack.append((neighbor, current, current_dist + weight))

    # If no path is found (should not happen in a connected tree)
    return -1
