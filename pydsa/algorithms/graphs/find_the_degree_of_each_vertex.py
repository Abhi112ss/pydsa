METADATA = {
    "id": 3898,
    "name": "Find the Degree of Each Vertex",
    "slug": "find_the_degree_of_each_vertex",
    "category": "Graphs",
    "aliases": [],
    "tags": ["graphs", "hash_map"],
    "difficulty": "easy",
    "time_complexity": "O(V + E)",
    "space_complexity": "O(V)",
    "description": "Calculate the degree of every vertex in an undirected graph represented by an adjacency list.",
}

def solve(n: int, edges: list[list[int]]) -> dict[int, int]:
    """
    Calculates the degree of each vertex in an undirected graph.

    The degree of a vertex is the number of edges connected to it. 
    Since the graph is undirected, each edge (u, v) contributes 1 to 
    the degree of u and 1 to the degree of v.

    Args:
        n: The number of vertices in the graph (vertices are labeled 0 to n-1).
        edges: A list of edges where edges[i] = [u, v] represents an edge between u and v.

    Returns:
        A dictionary where keys are vertex indices and values are their respective degrees.

    Examples:
        >>> solve(3, [[0, 1], [1, 2]])
        {0: 1, 1: 2, 2: 1}
        >>> solve(4, [[0, 1], [0, 2], [0, 3]])
        {0: 3, 1: 1, 2: 1, 3: 1}
    """
    # Initialize the degree map for all vertices from 0 to n-1
    # Using a dictionary to store degrees, though a list would also work for O(1) access
    degrees: dict[int, int] = {i: 0 for i in range(n)}

    # Iterate through each edge in the input list
    for u, v in edges:
        # Since the graph is undirected, increment degree for both endpoints
        degrees[u] += 1
        degrees[v] += 1

    return degrees
