METADATA = {
    "id": 1761,
    "name": "Minimum Degree of a Connected Trio in a Graph",
    "slug": "minimum-degree-of-a-connected-trio-in-a-graph",
    "category": "Graph",
    "aliases": [],
    "tags": ["hash_set", "graph"],
    "difficulty": "medium",
    "time_complexity": "O(n^2)",
    "space_complexity": "O(n^2)",
    "description": "Find the minimum degree of a trio of nodes that are all connected to each other in a graph.",
}

def solve(n: int, edges: list[list[int]]) -> int:
    """
    Finds the minimum degree among all connected trios in a graph.
    
    A trio is a set of three distinct nodes where every pair of nodes 
    in the set is connected by an edge.

    Args:
        n: The number of nodes in the graph (nodes are 0-indexed).
        edges: A list of edges where edges[i] = [u, v] represents an edge between u and v.

    Returns:
        The minimum degree of a connected trio, or -1 if no such trio exists.

    Examples:
        >>> solve(4, [[0,1],[1,2],[2,3],[3,0],[0,2]])
        2
        >>> solve(4, [[0,1],[1,2],[2,3]])
        -1
    """
    # Calculate the degree of each node
    degrees = [0] * n
    # Use an adjacency set for O(1) edge existence checks
    adj = [set() for _ in range(n)]
    
    for u, v in edges:
        degrees[u] += 1
        degrees[v] += 1
        adj[u].add(v)
        adj[v].add(u)
        
    min_degree = float('inf')
    found_trio = False

    # Iterate through every edge (u, v)
    # A trio exists if there is a common neighbor 'w' for both u and v
    for u, v in edges:
        # To optimize, we iterate through the neighbors of the node with the smaller degree
        # However, checking the intersection of sets is generally efficient in Python
        # We look for a node 'w' that is connected to both u and v
        
        # Optimization: only check neighbors of the node with fewer connections
        if len(adj[u]) > len(adj[v]):
            u, v = v, u
            
        for w in adj[u]:
            # Check if w is also a neighbor of v, forming a triangle (u, v, w)
            if w in adj[v]:
                found_trio = True
                # The degree of the trio is the sum of degrees of its members
                current_trio_degree = degrees[u] + degrees[v] + degrees[w]
                if current_trio_degree < min_degree:
                    min_degree = current_trio_degree
                    
    return int(min_degree) if found_trio else -1
