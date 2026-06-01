METADATA = {
    "id": 2508,
    "name": "Add Edges to Make Degrees of All Nodes Even",
    "slug": "add-edges-to-make-degrees-of-all-nodes-even",
    "category": "Graphs",
    "aliases": [],
    "tags": ["graphs", "greedy"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Find the minimum number of edges to add to a graph such that every node has an even degree.",
}

def solve(n: int, edges: list[list[int]]) -> int:
    """
    Calculates the minimum number of edges needed to make the degree of every node even.

    The problem can be solved by identifying all nodes that currently have an odd degree.
    Since adding one edge between two odd-degree nodes changes both their degrees to even,
    the minimum number of edges required is exactly half the number of odd-degree nodes.
    Because the sum of degrees in any graph is always even, the number of odd-degree 
    nodes is guaranteed to be even.

    Args:
        n: The number of nodes in the graph (labeled 1 to n).
        edges: A list of edges where edges[i] = [u, v] represents an edge between u and v.

    Returns:
        The minimum number of edges to add.

    Examples:
        >>> solve(6, [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6]])
        1
        >>> solve(4, [[1, 2], [3, 4]])
        1
        >>> solve(3, [[1, 2], [2, 3], [3, 1]])
        0
    """
    # Initialize degree array for nodes 1 to n
    # Using n + 1 to allow 1-based indexing for convenience
    degrees = [0] * (n + 1)

    # Count the degree of each node
    for u, v in edges:
        degrees[u] += 1
        degrees[v] += 1

    # Count how many nodes have an odd degree
    odd_degree_count = 0
    for i in range(1, n + 1):
        if degrees[i] % 2 != 0:
            odd_degree_count += 1

    # Each added edge can fix exactly two odd-degree nodes.
    # The sum of degrees is always even, so odd_degree_count is always even.
    return odd_degree_count // 2
