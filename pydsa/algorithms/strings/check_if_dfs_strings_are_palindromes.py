METADATA = {
    "id": 3327,
    "name": "Check if DFS Strings Are Palindromes",
    "slug": "check-if-dfs-strings-are-palindromes",
    "category": "String",
    "aliases": [],
    "tags": ["dfs", "strings", "palindrome", "graph"],
    "difficulty": "medium",
    "time_complexity": "O(N)",
    "space_complexity": "O(N)",
    "description": "Determine if the string formed by all possible DFS paths in a directed graph is a palindrome.",
}

def solve(n: int, edges: list[list[int]], s: str) -> bool:
    """
    Determines if the string formed by all possible DFS paths in a directed graph is a palindrome.
    
    Note: The problem implies a specific traversal order or structure. Based on the 
    standard interpretation of such problems, we reconstruct the sequence of characters 
    visited during a DFS traversal and check if that sequence is a palindrome.

    Args:
        n: The number of nodes in the graph.
        edges: A list of directed edges where edges[i] = [u, v].
        s: The string where s[i] is the character associated with node i.

    Returns:
        True if the resulting DFS string is a palindrome, False otherwise.

    Examples:
        >>> solve(3, [[0, 1], [1, 2]], "aba")
        True
        >>> solve(3, [[0, 1], [0, 2]], "abc")
        False
    """
    # Build adjacency list
    adj: dict[int, list[int]] = {i: [] for i in range(n)}
    for u, v in edges:
        adj[u].append(v)
    
    # Sort adjacency lists to ensure deterministic DFS traversal order
    for u in adj:
        adj[u].sort()

    visited: list[bool] = [False] * n
    dfs_sequence: list[str] = []

    def dfs(curr_node: int) -> None:
        visited[curr_node] = True
        dfs_sequence.append(s[curr_node])
        
        for neighbor in adj[curr_node]:
            if not visited[neighbor]:
                dfs(neighbor)

    # Start DFS from node 0 (assuming 0 is the root/start node)
    # If the graph has multiple components, we iterate through all nodes
    for i in range(n):
        if not visited[i]:
            dfs(i)

    # Two-pointer approach to check if the reconstructed string is a palindrome
    left, right = 0, len(dfs_sequence) - 1
    while left < right:
        if dfs_sequence[left] != dfs_sequence[right]:
            return False
        left += 1
        right -= 1
        
    return True
