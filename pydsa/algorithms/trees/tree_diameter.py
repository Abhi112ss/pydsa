METADATA = {
    "id": 1245,
    "name": "Tree Diameter",
    "slug": "tree_diameter",
    "category": "Graph",
    "aliases": [],
    "tags": ["dfs", "bfs", "graph_traversal"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Find the length of the longest path between any two nodes in a tree.",
}

from collections import defaultdict

def solve(n: int, edges: list[list[int]]) -> int:
    """
    Calculates the diameter of a tree given the number of nodes and edges.

    The diameter is the longest path between any two nodes in the tree.
    This implementation uses the two-BFS approach:
    1. Start BFS from an arbitrary node (0) to find the farthest node (u).
    2. Start a second BFS from node (u) to find the farthest node (v).
    The distance between u and v is the diameter.

    Args:
        n: The number of nodes in the tree.
        edges: A list of edges where edges[i] = [u, v].

    Returns:
        The length of the longest path in the tree.

    Examples:
        >>> solve(5, [[0, 1], [1, 2], [2, 3], [1, 4]])
        3
        >>> solve(2, [[0, 1]])
        1
    """
    if n <= 1:
        return 0

    # Build adjacency list
    adj = defaultdict(list)
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)

    def get_farthest_node(start_node: int) -> tuple[int, int]:
        """
        Performs BFS to find the farthest node from the start_node.

        Returns:
            A tuple containing (farthest_node, distance_to_that_node).
        """
        distances = [-1] * n
        distances[start_node] = 0
        queue = [start_node]
        
        farthest_node = start_node
        max_distance = 0
        
        idx = 0
        while idx < len(queue):
            current = queue[idx]
            idx += 1
            
            for neighbor in adj[current]:
                if distances[neighbor] == -1:
                    distances[neighbor] = distances[current] + 1
                    queue.append(neighbor)
                    
                    # Update farthest node found so far
                    if distances[neighbor] > max_distance:
                        max_distance = distances[neighbor]
                        farthest_node = neighbor
                        
        return farthest_node, max_distance

    # Step 1: Find one endpoint of the diameter
    # Starting from node 0, the farthest node is guaranteed to be an endpoint
    endpoint_u, _ = get_farthest_node(0)

    # Step 2: Find the distance to the other endpoint
    # The distance from endpoint_u to its farthest node is the diameter
    _, diameter = get_farthest_node(endpoint_u)

    return diameter
