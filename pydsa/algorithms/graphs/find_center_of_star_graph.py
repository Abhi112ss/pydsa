METADATA = {
    "id": 1791,
    "name": "Find Center of Star Graph",
    "slug": "find_center_of_star_graph",
    "category": "graph",
    "aliases": [],
    "tags": ["graph_traversal"],
    "difficulty": "easy",
    "time_complexity": "O(1)",
    "space_complexity": "O(1)",
    "description": "Return the center node of a star graph given its edges."
}


def solve(edges: list[list[int]]) -> int:
    """Find the center node of a star graph.

    Args:
        edges: A list of edges where each edge is represented by a list of two
            distinct node identifiers. The graph is guaranteed to be a star
            graph (one central node connected to all other nodes).

    Returns:
        The identifier of the central node.

    Examples:
        >>> solve([[1,2],[2,3],[4,2]])
        2
        >>> solve([[5,1],[5,2],[5,3],[5,4]])
        5
    """
    # Extract the first two edges
    first_edge = edges[0]
    second_edge = edges[1]

    first_node, second_node = first_edge[0], first_edge[1]
    third_node, fourth_node = second_edge[0], second_edge[1]

    # The center appears in both edges; check which endpoint is common
    if first_node == third_node or first_node == fourth_node:
        return first_node
    else:
        return second_node