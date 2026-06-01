METADATA = {
    "id": 3004,
    "name": "Maximum Subtree of the Same Color",
    "slug": "maximum_subtree_of_the_same_color",
    "category": "tree",
    "aliases": ["Max Subtree Same Color"],
    "tags": ["dfs", "tree", "hash_map"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Find the size of the largest subtree where all nodes have the same color.",
}

import sys

def solve(edges: list[list[int]], colors: list[int]) -> int:
    """
    Finds the size of the largest subtree where all nodes have the same color.

    Args:
        edges: A list of pairs representing edges in the tree.
        colors: A list of integers where colors[i] is the color of node i.

    Returns:
        The size of the largest monochromatic subtree.

    Examples:
        >>> solve([[0,1],[0,2],[2,3],[2,4],[2,5]], [1,1,2,2,2,2])
        4
    """
    # Increase recursion depth for deep trees
    sys.setrecursionlimit(200000)
    
    num_nodes = len(colors)
    if num_nodes == 0:
        return 0
    
    # Build adjacency list
    adj = [[] for _ in range(num_nodes)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
    
    max_monochromatic_size = 0

    def dfs(u: int, p: int) -> tuple[int, bool]:
        """
        Performs DFS to calculate subtree size and check if it's monochromatic.
        
        Returns:
            (subtree_size, is_monochromatic)
        """
        nonlocal max_monochromatic_size
        
        current_size = 1
        is_monochromatic = True
        
        for v in adj[u]:
            if v == p:
                continue
            
            child_size, child_monochromatic = dfs(v, u)
            current_size += child_size
            
            # A subtree rooted at u is monochromatic if:
            # 1. All its children's subtrees are monochromatic.
            # 2. All children have the same color as u.
            if not child_monochromatic or colors[v] != colors[u]:
                is_monochromatic = False
        
        # If the entire subtree rooted at u is monochromatic, update the global max
        if is_monochromatic:
            max_monochromatic_size = max(max_monochromatic_size, current_size)
            
        return current_size, is_monochromatic

    # Start DFS from root (node 0)
    dfs(0, -1)
    
    return max_monochromatic_size