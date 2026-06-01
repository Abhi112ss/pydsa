METADATA = {
    "id": 1469,
    "name": "Find All The Lonely Nodes",
    "slug": "find_all_the_lonely_nodes",
    "category": "Graph",
    "aliases": [],
    "tags": ["graph", "hash_map", "degree"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Identify nodes in a graph that have a degree of exactly one.",
}

def solve(n: int, edges: list[list[int]]) -> list[int]:
    """
    Finds all nodes in a graph that are 'lonely', meaning they have a degree of exactly 1.

    Args:
        n: The number of nodes in the graph (nodes are labeled 0 to n-1).
        edges: A list of edges where edges[i] = [u, v] represents an edge between node u and node v.

    Returns:
        A list of integers representing the labels of all lonely nodes, sorted in ascending order.

    Examples:
        >>> solve(4, [[0, 1], [1, 2], [2, 3]])
        [0, 3]
        >>> solve(5, [[0, 1], [1, 2], [2, 3], [3, 4]])
        [0, 4]
    """
    # Initialize a degree array to store the count of connections for each node
    # Using an array is more space-efficient than a dictionary for a fixed range [0, n-1]
    degrees = [0] * n

    # Iterate through each edge and increment the degree count for both endpoints
    for u, v in edges:
        degrees[u] += 1
        degrees[v] += 1

    # Collect all nodes whose degree is exactly 1
    lonely_nodes = []
    for node_index in range(n):
        if degrees[node_index] == 1:
            lonely_nodes.append(node_index)

    return lonely_nodes
