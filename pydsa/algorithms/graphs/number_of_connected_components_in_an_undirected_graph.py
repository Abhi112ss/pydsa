METADATA = {
    "id": 323,
    "name": "Number of Connected Components in an Undirected Graph",
    "slug": "number_of_connected_components_in_an_undirected_graph",
    "category": "Graph",
    "aliases": [],
    "tags": ["union_find", "depth_first_search", "breadth_first_search"],
    "difficulty": "medium",
    "time_complexity": "O(V + E)",
    "space_complexity": "O(V)",
    "description": "Find the total number of connected components in an undirected graph given its vertices and edges.",
}

def solve(n: int, edges: list[list[int]]) -> int:
    """
    Calculates the number of connected components in an undirected graph using Union-Find.

    Args:
        n: The number of nodes in the graph (nodes are labeled 0 to n-1).
        edges: A list of undirected edges where edges[i] = [u, v] represents an edge between u and v.

    Returns:
        The total number of connected components.

    Examples:
        >>> solve(5, [[0, 1], [1, 2], [3, 4]])
        2
        >>> solve(5, [[0, 1], [1, 2], [2, 3], [3, 4]])
        1
    """
    # parent array for Union-Find, initially each node is its own parent
    parent = list(range(n))
    # Track the number of components; initially, every node is a separate component
    component_count = n

    def find(node: int) -> int:
        """Finds the root of the node with path compression."""
        if parent[node] != node:
            parent[node] = find(parent[node])
        return parent[node]

    def union(node_a: int, node_b: int) -> bool:
        """Unites two sets. Returns True if a merge occurred, False if already in same set."""
        root_a = find(node_a)
        root_b = find(node_b)
        
        if root_a != root_b:
            # Merge the two components
            parent[root_a] = root_b
            return True
        return False

    # Iterate through all edges and perform union operations
    for u, v in edges:
        # If union is successful, it means two previously separate components are now connected
        if union(u, v):
            component_count -= 1

    return component_count
