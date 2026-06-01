METADATA = {
    "id": 1501,
    "name": "Countries You Can Safely Invest In",
    "slug": "countries-you-can-safely-invest-in",
    "category": "Graph",
    "aliases": [],
    "tags": ["dfs", "bfs", "graph", "topological_sort"],
    "difficulty": "medium",
    "time_complexity": "O(V + E)",
    "space_complexity": "O(V + E)",
    "description": "Identify nodes in a directed graph that are not part of a cycle and cannot reach any cycle.",
}

def solve(n: int, connections: list[list[int]]) -> list[int]:
    """
    Finds all countries that are safe to invest in. A country is safe if it 
    is not part of a cycle and cannot reach a cycle.

    This is equivalent to finding all nodes that can be removed via 
    Kahn's algorithm (topological sort) on the reversed graph.

    Args:
        n: The number of countries.
        connections: A list of directed edges where connections[i] = [u, v] 
                     means there is a directed edge from u to v.

    Returns:
        A list of safe country indices sorted in ascending order.

    Examples:
        >>> solve(4, [[1, 2], [2, 3], [3, 1]])
        [4]
        >>> solve(3, [[1, 2], [2, 3]])
        [1, 2, 3]
    """
    # Build adjacency list for the reversed graph.
    # In the original graph, an edge u -> v means u can reach v.
    # If v is part of a cycle, u is unsafe.
    # In the reversed graph, if we perform topological sort, we find nodes 
    # that have no outgoing edges (in the original graph, these are nodes 
    # that don't lead to anything, or rather, nodes that are 'sinks').
    # Actually, the simplest way: A node is safe if it is NOT in a cycle 
    # and cannot reach a cycle. This is exactly what nodes removed by 
    # Kahn's algorithm on the ORIGINAL graph are NOT.
    # Wait, Kahn's algorithm removes nodes with in-degree 0. 
    # If we want to find nodes that cannot reach a cycle, we should 
    # look at the graph where edges are reversed and find nodes with 
    # in-degree 0 in the reversed graph (which are out-degree 0 in original).
    
    # Let's use the standard Kahn's approach:
    # A node is safe if it is not part of a cycle and cannot reach a cycle.
    # This is equivalent to saying: if we repeatedly remove nodes with 
    # OUT-DEGREE 0, the nodes we remove are the safe ones.
    
    adj_reversed = [[] for _ in range(n + 1)]
    out_degree = [0] * (n + 1)
    
    for u, v in connections:
        # Original: u -> v
        # Reversed: v -> u
        adj_reversed[v].append(u)
        out_degree[u] += 1
        
    # Kahn's algorithm using out-degree
    queue = []
    for i in range(1, n + 1):
        if out_degree[i] == 0:
            queue.append(i)
            
    safe_countries = []
    head = 0
    while head < len(queue):
        current = queue[head]
        head += 1
        safe_countries.append(current)
        
        # For every node 'prev' that points to 'current' in the original graph
        for prev in adj_reversed[current]:
            out_degree[prev] -= 1
            # If 'prev' now has no outgoing edges to unsafe nodes
            if out_degree[prev] == 0:
                queue.append(prev)
                
    return sorted(safe_countries)
