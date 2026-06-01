METADATA = {
    "id": 3313,
    "name": "Find the Last Marked Nodes in Tree",
    "slug": "find-the-last-marked-nodes-in-tree",
    "category": "Trees",
    "aliases": [],
    "tags": ["trees", "dfs", "priority_queue", "greedy"],
    "difficulty": "hard",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Find the last nodes marked in a tree given a specific marking rule based on parent-child relationships.",
}

import heapq

def solve(n: int, edges: list[list[int]], marked: list[int]) -> list[int]:
    """
    Finds the last marked nodes in a tree based on a specific marking process.
    
    The process involves marking nodes such that a node can only be marked 
    after its parent is marked. We want to find the set of nodes that are 
    marked last in an optimal sequence.

    Args:
        n: The number of nodes in the tree.
        edges: A list of edges where edges[i] = [u, v] represents an edge between u and v.
        marked: A list of integers where marked[i] is 1 if node i is marked, 0 otherwise.

    Returns:
        A list of node indices that are marked last, sorted in ascending order.

    Examples:
        >>> solve(3, [[0, 1], [0, 2]], [1, 1, 1])
        [1, 2]
    """
    # Build adjacency list
    adj: list[list[int]] = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)

    # Determine parent-child relationships using BFS/DFS starting from root 0
    parent: list[int] = [-1] * n
    children: list[list[int]] = [[] for _ in range(n)]
    order: list[int] = []
    stack = [0]
    visited = [False] * n
    visited[0] = True
    
    # Standard BFS to establish hierarchy
    queue = [0]
    idx = 0
    while idx < len(queue):
        curr = queue[idx]
        idx += 1
        order.append(curr)
        for neighbor in adj[curr]:
            if not visited[neighbor]:
                visited[neighbor] = True
                parent[neighbor] = curr
                children[curr].append(neighbor)
                queue.append(neighbor)

    # The problem asks for the "last" marked nodes. 
    # In a tree where a node can only be marked after its parent, 
    # the nodes that can be marked last are the leaves of the 
    # subtree formed by the 'marked' nodes.
    
    # We calculate the 'depth' or 'rank' of each marked node.
    # A node's rank is determined by the maximum rank of its marked children + 1.
    # However, the problem logic implies we want to find nodes that are 
    # "deepest" in terms of the marking dependency chain.
    
    # Let's use the property: A node is a candidate for being 'last' if 
    # it is a marked node and none of its marked descendants can extend its chain.
    
    # We process nodes in reverse topological order (from leaves to root)
    # to calculate the maximum depth of the marked subtree rooted at each node.
    max_marked_depth: list[int] = [0] * n
    is_marked_node: list[bool] = [False] * n
    for i in range(n):
        if marked[i] == 1:
            is_marked_node[i] = True

    # Process nodes in reverse BFS order (bottom-up)
    for i in range(n - 1, -1, -1):
        u = order[i]
        if is_marked_node[u]:
            # If node is marked, its depth is 1 + max depth of its marked children
            max_child_depth = 0
            for v in children[u]:
                if is_marked_node[v]:
                    max_child_depth = max(max_child_depth, max_marked_depth[v])
            max_marked_depth[u] = 1 + max_child_depth
        else:
            # If node is not marked, it doesn't contribute to a marked chain
            max_marked_depth[u] = 0

    # The "last" nodes are the marked nodes that have the global maximum depth
    # among all marked nodes.
    if not any(is_marked_node):
        return []

    global_max_depth = max(max_marked_depth)
    
    # Collect all marked nodes that achieve this maximum depth
    result = []
    for i in range(n):
        if is_marked_node[i] and max_marked_depth[i] == global_max_depth:
            result.append(i)
            
    return sorted(result)
