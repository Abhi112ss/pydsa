METADATA = {
    "id": 3656,
    "name": "Determine if a Simple Graph Exists",
    "slug": "determine-if-a-simple-graph-exists",
    "category": "math",
    "aliases": [],
    "tags": ["graphs", "math"],
    "difficulty": "easy",
    "time_complexity": "O(1)",
    "space_complexity": "O(1)",
    "description": "Determine if a simple graph can exist given the number of vertices and edges.",
}

def solve(n: int, m: int) -> bool:
    """
    Determines if a simple undirected graph can exist with n vertices and m edges.
    
    A simple graph is defined as a graph that has no self-loops and no multiple edges 
    between the same pair of vertices. For a graph with n vertices, the maximum 
    number of edges possible in a simple graph is the number of ways to choose 
    2 distinct vertices out of n, which is n * (n - 1) / 2.

    Args:
        n (int): The number of vertices in the graph.
        m (int): The number of edges in the graph.

    Returns:
        bool: True if a simple graph can exist, False otherwise.

    Examples:
        >>> solve(3, 2)
        True
        >>> solve(3, 4)
        False
        >>> solve(1, 0)
        True
    """
    # A simple graph cannot have a negative number of edges.
    if m < 0:
        return False
    
    # A simple graph with n vertices can have at most n * (n - 1) / 2 edges.
    # This represents the maximum number of unique pairs of vertices.
    # For n < 2, the maximum edges is 0.
    if n < 2:
        max_edges = 0
    else:
        max_edges = (n * (n - 1)) // 2
        
    return m <= max_edges