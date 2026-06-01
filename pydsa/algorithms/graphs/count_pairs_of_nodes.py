METADATA = {
    "id": 1782,
    "name": "Count Pairs Of Nodes",
    "slug": "count_pairs_of_nodes",
    "category": "Graph",
    "aliases": [],
    "tags": ["bfs", "dfs", "graph_traversal"],
    "difficulty": "medium",
    "time_complexity": "O(n^2)",
    "space_complexity": "O(n)",
    "description": "Count the number of pairs of nodes (u, v) in a tree such that the distance between them is exactly k.",
}

def solve(n: int, edges: list[list[int]], k: int) -> int:
    """
    Counts the number of pairs of nodes in a tree that are exactly distance k apart.

    Args:
        n: The number of nodes in the tree (nodes are labeled 0 to n-1).
        edges: A list of undirected edges where edges[i] = [u, v].
        k: The target distance between nodes.

    Returns:
        The total number of pairs (u, v) with u < v such that distance(u, v) == k.

    Examples:
        >>> solve(5, [[0, 1], [1, 2], [2, 3], [3, 4]], 2)
        3
        >>> solve(5, [[0, 1], [1, 2], [2, 3], [3, 4]], 3)
        2
    """
    # Build adjacency list representation of the tree
    adj: dict[int, list[int]] = {i: [] for i in range(n)}
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)

    total_pairs = 0

    # Since it's a tree and we need to find pairs for every node,
    # we can perform a BFS/DFS from every single node to find nodes at distance k.
    for start_node in range(n):
        # Standard BFS to find nodes at distance k from start_node
        # queue stores (current_node, current_distance, parent_node)
        # parent_node is used to avoid moving back to the node we just came from
        queue: list[tuple[int, int, int]] = [(start_node, 0, -1)]
        
        # We use a simple pointer for the queue to simulate O(1) popleft
        head = 0
        while head < len(queue):
            curr, dist, parent = queue[head]
            head += 1

            if dist == k:
                # We found a node at distance k. 
                # To avoid double counting (u,v) and (v,u), we only count if u < v.
                if start_node < curr:
                    total_pairs += 1
                # No need to explore further than distance k
                continue

            for neighbor in adj[curr]:
                if neighbor != parent:
                    queue.append((neighbor, dist + 1, curr))

    return total_pairs
