METADATA = {
    "id": 1557,
    "name": "Minimum Number of Vertices to Reach All Nodes",
    "slug": "minimum-number-of-vertices-to-reach-all-nodes",
    "category": "Graph",
    "aliases": [],
    "tags": ["graphs", "indegree"],
    "difficulty": "medium",
    "time_complexity": "O(V + E)",
    "space_complexity": "O(V)",
    "description": "Find the minimum number of vertices required to reach all nodes in a directed graph.",
}

def solve(n: int, edges: list[list[int]]) -> int:
    """
    Calculates the minimum number of vertices needed to reach all nodes in a directed graph.
    
    The key insight is that any node with an in-degree of zero must be part of the 
    starting set, because no other node can reach it. In a directed acyclic graph 
    or any graph structure where we want to cover all nodes, these source nodes 
    are the only necessary starting points.

    Args:
        n: The total number of nodes in the graph (labeled 0 to n-1).
        edges: A list of directed edges where edges[i] = [from_i, to_i].

    Returns:
        The minimum number of vertices required to reach all nodes.

    Examples:
        >>> solve(6, [[0,1],[2,3],[3,4],[1,2],[4,5]])
        1
        >>> solve(3, [[3,3],[4,4],[7,7],[5,6],[7,6],[8,8]]) # Note: n is context dependent
        # Example 2 from LeetCode: n=3, edges=[[0,1],[0,2]] -> 1
        >>> solve(3, [[0,1],[2,1]])
        2
    """
    # Track which nodes have at least one incoming edge
    has_incoming_edge = [False] * n

    # Iterate through all edges to mark destination nodes
    for _, destination in edges:
        has_incoming_edge[destination] = True

    # The minimum set of vertices consists of all nodes that are never a destination
    # because they cannot be reached from any other node.
    min_vertices_count = 0
    for i in range(n):
        if not has_incoming_edge[i]:
            min_vertices_count += 1

    return min_vertices_count
