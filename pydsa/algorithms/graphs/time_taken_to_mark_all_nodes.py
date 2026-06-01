METADATA = {
    "id": 3241,
    "name": "Time Taken to Mark All Nodes",
    "slug": "time_taken_to_mark_all_nodes",
    "category": "Tree",
    "aliases": [],
    "tags": ["bfs", "dfs", "tree", "diameter"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Find the minimum time required to mark all nodes in a tree where each second, all unmarked nodes adjacent to marked nodes become marked.",
}

def solve(n: int, edges: list[list[int]]) -> int:
    """
    Calculates the minimum time required to mark all nodes in a tree.
    
    The problem is equivalent to finding the radius of the tree. 
    The time taken is equal to ceil(diameter / 2).
    
    Args:
        n: The number of nodes in the tree.
        edges: A list of undirected edges representing the tree.
        
    Returns:
        The minimum time (integer) to mark all nodes.
        
    Examples:
        >>> solve(2, [[0, 1]])
        1
        >>> solve(3, [[0, 1], [1, 2]])
        1
        >>> solve(4, [[0, 1], [1, 2], [2, 3]])
        2
    """
    if n <= 1:
        return 0

    # Build adjacency list
    adj: dict[int, list[int]] = {i: [] for i in range(n)}
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)

    def get_farthest_node(start_node: int) -> tuple[int, int]:
        """
        Performs BFS to find the farthest node from the start_node.
        Returns a tuple of (farthest_node, distance).
        """
        distances = [-1] * n
        distances[start_node] = 0
        queue = [start_node]
        
        farthest_node = start_node
        max_dist = 0
        
        idx = 0
        while idx < len(queue):
            curr = queue[idx]
            idx += 1
            
            if distances[curr] > max_dist:
                max_dist = distances[curr]
                farthest_node = curr
                
            for neighbor in adj[curr]:
                if distances[neighbor] == -1:
                    distances[neighbor] = distances[curr] + 1
                    queue.append(neighbor)
                    
        return farthest_node, max_dist

    # Step 1: Find one end of the diameter by starting BFS from an arbitrary node (0)
    node_a, _ = get_farthest_node(0)
    
    # Step 2: Find the other end of the diameter and the diameter length itself
    _, diameter = get_farthest_node(node_a)

    # The time taken to mark all nodes is the radius of the tree.
    # For a tree, radius = ceil(diameter / 2).
    return (diameter + 1) // 2
