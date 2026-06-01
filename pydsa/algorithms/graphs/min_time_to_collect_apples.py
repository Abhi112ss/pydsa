METADATA = {
    "id": 1443,
    "name": "Minimum Time to Collect All Apples in a Tree",
    "slug": "minimum-time-to-collect-all-apples-in-a-tree",
    "category": "Tree",
    "aliases": [],
    "tags": ["dfs", "tree", "recursion"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Calculate the minimum time to collect all apples in a tree given the adjacency list and apple locations.",
}

def solve(edges: list[list[int]], apples: list[int]) -> int:
    """
    Calculates the minimum time to collect all apples in a tree.

    Args:
        edges: A list of edges where edges[i] = [u, v] represents an edge between nodes u and v.
        apples: A list of nodes that contain an apple.

    Returns:
        The minimum time required to collect all apples and return to the root.

    Examples:
        >>> solve([[2, 5], [5, 5, 3], [5, 5, 2], [4, 5, 7], [3, 5, 4], [3, 5, 1], [5, 5, 6]], [9, 8, 7, 6, 1])
        16
    """
    n = len(edges)
    adj = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)

    apple_set = set(apples)
    total_time = 0

    def dfs(node: int, parent: int) -> bool:
        """
        Performs DFS to find if a subtree contains any apples.
        
        Returns:
            True if the current subtree (rooted at 'node') contains at least one apple.
        """
        nonlocal total_time
        has_apple_in_subtree = False
        
        # Check if the current node itself has an apple
        if node in apple_set:
            has_apple_in_subtree = True

        for neighbor in adj[node]:
            if neighbor != parent:
                # Recursively check if the child's subtree has an apple
                if dfs(neighbor, node):
                    has_apple_in_subtree = True
                    # If child has an apple, we must travel to it and back (2 units of time)
                    total_time += 2

        return has_apple_in_subtree

    # Start DFS from the root (node 0)
    dfs(0, -1)
    return total_time
