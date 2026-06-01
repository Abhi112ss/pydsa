METADATA = {
    "id": 1319,
    "name": "Number of Operations to Make Network Connected",
    "slug": "number-of-operations-to-make-network-connected",
    "category": "Graph",
    "aliases": [],
    "tags": ["union_find", "dfs", "connected_components", "disjoint_set_union"],
    "difficulty": "medium",
    "time_complexity": "O(V + E)",
    "space_complexity": "O(V)",
    "description": "Find the minimum number of operations to connect all computers in a network given existing connections.",
}

def solve(n: int, connections: list[list[int]]) -> int:
    """
    Calculates the minimum number of cables to move to make all computers connected.

    The problem can be modeled as finding the number of connected components in a graph.
    To connect 'k' components, we need exactly 'k - 1' additional edges.
    First, we check if we have enough total cables (edges) to form a spanning tree (n - 1 edges).

    Args:
        n: The number of computers (nodes).
        connections: A list of pairs representing existing cable connections (edges).

    Returns:
        The minimum number of operations required, or -1 if it is impossible.

    Examples:
        >>> solve(4, [[0,1],[0,2],[1,2]])
        1
        >>> solve(6, [[0,1],[0,2],[0,3],[1,2],[1,3]])
        2
        >>> solve(6, [[0,1],[0,2],[0,3],[1,2]])
        -1
    """
    # A connected graph with n nodes must have at least n - 1 edges.
    if len(connections) < n - 1:
        return -1

    # Disjoint Set Union (DSU) to find connected components
    parent = list(range(n))
    
    def find(i: int) -> int:
        if parent[i] == i:
            return i
        # Path compression
        parent[i] = find(parent[i])
        return parent[i]

    def union(i: int, j: int) -> bool:
        root_i = find(i)
        root_j = find(j)
        if root_i != root_j:
            parent[root_i] = root_j
            return True
        return False

    # Track the number of connected components. 
    # Initially, every node is its own component.
    num_components = n

    for u, v in connections:
        # If union returns True, two components were merged into one.
        if union(u, v):
            num_components -= 1

    # To connect 'k' components, we need 'k - 1' edges.
    # Since we already checked that total edges >= n - 1, 
    # we are guaranteed to have enough redundant cables.
    return num_components - 1
