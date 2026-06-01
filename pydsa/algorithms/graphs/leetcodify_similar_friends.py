METADATA = {
    "id": 1919,
    "name": "Find Center of Star Graph",
    "slug": "find-center-of-star-graph",
    "category": "Graphs",
    "aliases": [],
    "tags": ["graphs", "hash_map"],
    "difficulty": "easy",
    "time_complexity": "O(1)",
    "space_complexity": "O(1)",
    "description": "Find the center node of a star graph given its edges.",
}

def solve(edges: list[list[int]]) -> int:
    """
    Finds the center node of a star graph.
    
    In a star graph, there is one central node that is connected to all other nodes.
    Therefore, the center node must appear in every single edge of the graph.
    We only need to check the first two edges to find the common node.

    Args:
        edges: A list of edges where edges[i] = [u, v] represents an edge between u and v.

    Returns:
        The integer representing the center node.

    Examples:
        >>> solve([[1, 2], [2, 3], [4, 2]])
        2
        >>> solve([[1, 2], [2, 3], [3, 4]])
        # Note: This input wouldn't be a star graph per problem constraints, 
        # but the logic finds the commonality.
    """
    # A star graph center must appear in every edge.
    # We only need to compare the first two edges to find the node that appears twice.
    edge_one_u, edge_one_v = edges[0]
    edge_two_u, edge_two_v = edges[1]

    # If the first node of the first edge is in the second edge, it's the center.
    if edge_one_u == edge_two_u or edge_one_u == edge_two_v:
        return edge_one_u
    
    # Otherwise, the second node of the first edge must be the center.
    return edge_one_v
