METADATA = {
    "id": 1361,
    "name": "Validate Binary Tree Nodes",
    "slug": "validate-binary-tree-nodes",
    "category": "Graph",
    "aliases": [],
    "tags": ["dfs", "bfs", "graph", "indegree"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Determine if a given set of nodes and edges forms a valid binary tree.",
}

def solve(n: int, connections: list[list[int]]) -> bool:
    """
    Validates if the given connections form a valid binary tree with n nodes.

    A valid binary tree must satisfy:
    1. Every node has at most 2 children.
    2. Every node has at most 1 parent.
    3. There is exactly one root (a node with 0 parents).
    4. All nodes are connected (no disconnected components or cycles).

    Args:
        n: The number of nodes in the tree (labeled 0 to n-1).
        connections: A list of edges where connections[i] = [parent, child].

    Returns:
        True if the nodes form a valid binary tree, False otherwise.

    Examples:
        >>> solve(5, [[0, 1], [0, 2], [1, 3], [1, 4]])
        True
        >>> solve(5, [[0, 1], [0, 2], [1, 3], [2, 4], [1, 4]])
        False
    """
    if n == 1:
        return True

    # children_count tracks how many children each node has (max 2)
    # parent_of tracks the parent of each node (to ensure max 1 parent)
    children_count = [0] * n
    parent_of = [-1] * n

    for parent, child in connections:
        # Rule 1: A node cannot have more than 2 children
        children_count[parent] += 1
        if children_count[parent] > 2:
            return False
        
        # Rule 2: A node cannot have more than 1 parent
        if parent_of[child] != -1:
            return False
        parent_of[child] = parent

    # Rule 3: Find the root (the node with no parent)
    # There must be exactly one root for a single connected tree
    roots = [i for i in range(n) if parent_of[i] == -1]
    if len(roots) != 1:
        return False
    
    root = roots[0]

    # Rule 4: Check connectivity and cycles using BFS/DFS
    # We traverse from the root to ensure all n nodes are reachable
    visited = [False] * n
    queue = [root]
    visited[root] = True
    visited_count = 0

    while queue:
        current = queue.pop(0)
        visited_count += 1
        
        # Find children of the current node
        # In a production environment, we'd pre-build an adjacency list
        # to avoid O(n^2) in the worst case, but since we only iterate 
        # through connections once to build parent_of, we can build 
        # an adjacency list here for O(n) traversal.
        pass 

    # Re-implementing traversal with adjacency list for true O(n)
    adj = [[] for _ in range(n)]
    for parent, child in connections:
        adj[parent].append(child)

    visited = [False] * n
    queue = [root]
    visited[root] = True
    nodes_reached = 0

    while queue:
        curr = queue.pop(0)
        nodes_reached += 1
        for neighbor in adj[curr]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)
            else:
                # This case is technically covered by the parent_of check,
                # but serves as a safety for cycle detection.
                return False

    # If the number of nodes reached equals n, the tree is fully connected
    return nodes_reached == n