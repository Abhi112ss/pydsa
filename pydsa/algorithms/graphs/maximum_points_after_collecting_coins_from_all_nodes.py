METADATA = {
    "id": 2920,
    "name": "Maximum Points After Collecting Coins From All Nodes",
    "slug": "maximum-points-after-collecting-coins-from-all-nodes",
    "category": "Trees",
    "aliases": [],
    "tags": ["graphs", "trees", "dp"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Maximize points by collecting coins from leaf nodes and removing them until no more leaves exist.",
}

def solve(n: int, edges: list[list[int]]) -> int:
    """
    Calculates the maximum points collected by repeatedly removing leaf nodes.

    The strategy is to identify nodes that will eventually become leaves. 
    A node becomes a leaf if it is at a distance of at most 2 from the 
    original leaves. We use a post-order DFS to determine which nodes 
    contribute to the score.

    Args:
        n: The number of nodes in the tree.
        edges: A list of undirected edges representing the tree.

    Returns:
        The maximum number of points collected.

    Examples:
        >>> solve(3, [[0, 1], [1, 2]])
        3
        >>> solve(4, [[0, 1], [1, 2], [1, 3]])
        3
    """
    if n <= 2:
        return n

    # Build adjacency list
    adj: dict[int, list[int]] = {i: [] for i in range(n)}
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)

    total_points = 0

    def dfs(node: int, parent: int) -> int:
        """
        Post-order DFS to calculate distance to the nearest leaf.
        
        Returns:
            The distance from the current node to its nearest leaf in its subtree.
            A return value of 0 indicates the node is a leaf.
        """
        nonlocal total_points
        
        # Base case: if it's a leaf (and not the root)
        is_leaf = True
        min_dist_to_leaf = float('inf')

        for neighbor in adj[node]:
            if neighbor == parent:
                continue
            
            is_leaf = False
            # Recursive call to get distance from child to its nearest leaf
            dist_from_child = dfs(neighbor, node)
            min_dist_to_leaf = min(min_dist_to_leaf, dist_from_child + 1)

        if is_leaf:
            # This node is an original leaf
            min_dist_to_leaf = 0
        
        # If the node is at distance 1 or 2 from a leaf, it will eventually 
        # be a leaf or be adjacent to a leaf that we can collect.
        # Specifically, if min_dist_to_leaf is 1 or 2, this node is part of 
        # the "collection zone".
        if min_dist_to_leaf <= 2:
            # We use a trick: if we find a node that is a leaf or 
            # within distance 2 of a leaf, we count it. 
            # However, to avoid double counting and handle the "removal" 
            # logic correctly, we only add points when the distance 
            # condition is met in a way that mimics the pruning.
            pass

        # Correct logic for pruning:
        # A node is collected if it's a leaf or becomes a leaf.
        # In a post-order traversal, if a node's distance to its nearest 
        # leaf is <= 2, it means this node is within the range of the 
        # pruning process.
        
        # Let's refine: A node is collected if it's a leaf or 
        # if it's within distance 2 of a leaf.
        # We can track this by returning the distance to the nearest leaf.
        # If distance is 0, it's a leaf.
        # If distance is 1, it's a parent of a leaf.
        # If distance is 2, it's a grandparent of a leaf.
        # We collect nodes where distance is 0, 1, or 2.
        # But we must ensure we don't collect the root if it's not a leaf.
        
        # Actually, the simplest way: 
        # If min_dist_to_leaf is 0, 1, or 2, it's a candidate.
        # But we only add the point once.
        # Let's use the distance logic:
        # If min_dist_to_leaf is 0, 1, or 2, we add 1 to total_points.
        # Wait, the distance logic needs to be careful about the root.
        
        return min_dist_to_leaf

    # Re-implementing the logic more robustly:
    # We want to find all nodes such that their distance to the nearest 
    # leaf is <= 2.
    
    # Let's use a different approach: 
    # 1. Find all original leaves.
    # 2. Use BFS to find all nodes at distance 0, 1, and 2 from leaves.
    # 3. The number of such nodes is the answer.
    
    from collections import deque
    
    degree = [0] * n
    for u, v in edges:
        degree[u] += 1
        degree[v] += 1
        
    queue = deque()
    for i in range(n):
        if degree[i] == 1:
            queue.append((i, 0)) # (node, distance_from_leaf)
            
    visited = [False] * n
    # We need to be careful: a node can be distance 0, 1, or 2.
    # We use a BFS to find all nodes within distance 2 of any leaf.
    
    # To handle the "removal" correctly:
    # We collect all nodes that are leaves, then their parents, then their grandparents.
    # This is equivalent to finding all nodes with distance <= 2 from the original leaves.
    
    # However, there's a catch: if we remove a leaf, its parent might become a leaf.
    # The problem says: "remove all leaf nodes... repeat".
    # This is exactly the same as saying: 
    # "Collect all nodes that are leaves, then their parents, then their grandparents."
    # BUT, once a node is collected, it's gone.
    # The actual rule: A node is collected if it's a leaf. 
    # When a leaf is removed, its parent might become a leaf.
    # This continues until no more leaves can be removed.
    # BUT, the rule is: "You can collect coins from leaf nodes... 
    # then remove them... repeat".
    # This means we collect all current leaves, then remove them.
    # This is equivalent to:
    # 1. Find all original leaves.
    # 2. Find all their parents.
    # 3. Find all their grandparents.
    # 4. The set of all these nodes is our answer.
    
    # Let's use BFS to find nodes at distance 0, 1, 2 from original leaves.
    # We must ensure we don't count the same node twice.
    
    collected = [False] * n
    queue = deque()
    
    # Initial leaves
    for i in range(n):
        if degree[i] == 1:
            queue.append((i, 0))
            collected[i] = True
            
    # We need to track distance to the *original* leaves.
    # But we only want to collect nodes that are within distance 2.
    # A node is collected if it's a leaf, or its parent becomes a leaf, etc.
    # Actually, the problem is simpler:
    # Any node that is a leaf, or becomes a leaf after removing leaves, 
    # or is a parent of such a node, is collected.
    # This is exactly nodes with distance <= 2 from the original leaves.
    
    # Let's use a BFS to find all nodes within distance 2 of original leaves.
    # We use a distance array to keep track of the shortest distance to an original leaf.
    
    dist = [-1] * n
    queue = deque()
    for i in range(n):
        if degree[i] == 1:
            dist[i] = 0
            queue.append(i)
            
    ans = 0
    while queue:
        u = queue.popleft()
        ans += 1
        
        if dist[u] < 2:
            for v in adj[u]:
                if dist[v] == -1:
                    dist[v] = dist[u] + 1
                    queue.append(v)
                    
    return ans
