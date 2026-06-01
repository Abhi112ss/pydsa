METADATA = {
    "id": 310,
    "name": "Minimum Height Trees",
    "slug": "minimum-height-trees",
    "category": "Graph",
    "aliases": [],
    "tags": ["topological_sort", "bfs", "graph", "tree"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Find all root nodes that result in the minimum height of a tree.",
}

from collections import deque

def solve(n: int, edges: list[list[int]]) -> list[int]:
    """
    Finds the roots that produce the minimum height trees using a topological sort approach.

    The algorithm works by iteratively removing the leaf nodes (nodes with degree 1) 
    layer by layer, similar to BFS, until only the centroid(s) of the graph remain.
    A tree can have at most two centroids.

    Args:
        n: The number of nodes in the graph.
        edges: A list of undirected edges where edges[i] = [u, v].

    Returns:
        A list of integers representing the indices of the nodes that are roots of MHTs.

    Examples:
        >>> solve(4, [[1, 0], [1, 2], [1, 3]])
        [1]
        >>> solve(6, [[3, 0], [3, 1], [3, 2], [3, 4], [5, 4]])
        [3, 4]
    """
    # Base case: If there is only one node, it is the root of the MHT.
    if n <= 1:
        return [0]

    # Build adjacency list and track the degree of each node.
    adj: dict[int, set[int]] = {i: set() for i in range(n)}
    degree: list[int] = [0] * n
    for u, v in edges:
        adj[u].add(v)
        adj[v].add(u)
        degree[u] += 1
        degree[v] += 1

    # Initialize the first layer of leaves (nodes with exactly one connection).
    leaves: deque[int] = deque([i for i in range(n) if degree[i] == 1])

    # Keep track of how many nodes are left to process.
    remaining_nodes = n
    
    # Continue removing leaves until 1 or 2 nodes remain.
    while remaining_nodes > 2:
        leaves_count = len(leaves)
        remaining_nodes -= leaves_count
        
        # Process all current leaves in the current "layer".
        for _ in range(leaves_count):
            leaf = leaves.popleft()
            
            # Find the neighbor of the leaf to update its degree.
            # Since it's a leaf, it only has one neighbor in the current graph.
            for neighbor in adj[leaf]:
                # Remove the connection from the neighbor.
                adj[neighbor].remove(leaf)
                degree[neighbor] -= 1
                
                # If the neighbor becomes a leaf, add it to the next layer.
                if degree[neighbor] == 1:
                    leaves.append(neighbor)
            
            # Clear the leaf's connections to free memory/logic.
            adj[leaf].clear()

    # The remaining nodes in the queue are the centroids.
    return list(leaves)
