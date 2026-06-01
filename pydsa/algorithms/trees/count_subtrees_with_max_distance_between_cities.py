METADATA = {
    "id": 1617,
    "name": "Count Subtrees With Max Distance Between Cities",
    "slug": "count-subtrees-with-max-distance-between-cities",
    "category": "Trees",
    "aliases": [],
    "tags": ["trees", "dfs", "depth-first-search"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Count the number of subtrees where the maximum distance between any two nodes is at most k.",
}

def solve(n: int, edges: list[list[int]], k: int) -> int:
    """
    Counts the number of subtrees where the diameter (max distance between any two nodes) 
    is less than or equal to k.

    Args:
        n: The number of cities.
        edges: A list of undirected edges representing connections between cities.
        k: The maximum allowed distance between any two cities in a subtree.

    Returns:
        The total number of valid subtrees.

    Examples:
        >>> solve(3, [[0,1],[1,2]], 1)
        2
        >>> solve(3, [[0,1],[1,2]], 2)
        4
    """
    # Build adjacency list
    adj: dict[int, list[int]] = {i: [] for i in range(n)}
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)

    valid_subtree_count = 0

    def dfs(current_node: int, parent_node: int) -> int:
        """
        Performs DFS to calculate the maximum depth of the subtree rooted at current_node.
        Also updates the global valid_subtree_count by checking the diameter.
        
        Returns:
            The maximum distance from current_node to any leaf in its subtree.
        """
        nonlocal valid_subtree_count
        
        # Store the depths of all child branches
        child_depths: list[int] = []
        
        for neighbor in adj[current_node]:
            if neighbor != parent_node:
                # Recursively find the max depth of the child's subtree
                child_depths.append(dfs(neighbor, current_node) + 1)
        
        # Sort depths to easily find the two longest paths passing through current_node
        child_depths.sort(reverse=True)
        
        # The diameter of the subtree rooted at current_node is the sum of the 
        # two largest depths (if they exist) or just the largest depth.
        current_diameter = 0
        if len(child_depths) >= 2:
            current_diameter = child_depths[0] + child_depths[1]
        elif len(child_depths) == 1:
            current_diameter = child_depths[0]
            
        # If the diameter of the subtree rooted at this node is <= k, it's a valid subtree
        if current_diameter <= k:
            valid_subtree_count += 1
            
        # Return the longest path from this node downwards to its parent
        return child_depths[0] if child_depths else 0

    # Start DFS from node 0 (assuming the graph is a tree and connected)
    dfs(0, -1)
    
    return valid_subtree_count
