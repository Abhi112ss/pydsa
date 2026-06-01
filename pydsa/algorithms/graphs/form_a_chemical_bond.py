METADATA = {
    "id": 2480,
    "name": "Form a Chemical Bond",
    "slug": "form-a-chemical-bond",
    "category": "Graphs",
    "aliases": [],
    "tags": ["graphs", "dfs", "union_find", "connectivity"],
    "difficulty": "medium",
    "time_complexity": "O(n + e)",
    "space_complexity": "O(n)",
    "description": "Determine if two atoms can form a chemical bond by checking if they belong to the same connected component in a graph of existing bonds.",
}

def solve(n: int, bonds: list[list[int]], atom1: int, atom2: int) -> bool:
    """
    Determines if two atoms can form a chemical bond based on existing bonds.
    
    Two atoms can form a bond if there is a path of existing bonds connecting them.
    This is a connectivity problem in an undirected graph.

    Args:
        n: The total number of atoms (labeled 0 to n-1).
        bonds: A list of pairs [u, v] representing an existing bond between atom u and atom v.
        atom1: The index of the first atom to check.
        atom2: The index of the second atom to check.

    Returns:
        True if atom1 and atom2 are in the same connected component, False otherwise.

    Examples:
        >>> solve(3, [[0, 1], [1, 2]], 0, 2)
        True
        >>> solve(3, [[0, 1]], 0, 2)
        False
    """
    # Build adjacency list to represent the graph
    adj: dict[int, list[int]] = {i: [] for i in range(n)}
    for u, v in bonds:
        adj[u].append(v)
        adj[v].append(u)

    # Use a set to keep track of visited atoms during traversal
    visited: set[int] = set()
    
    # Iterative DFS to check connectivity
    stack: list[int] = [atom1]
    visited.add(atom1)

    while stack:
        current_atom = stack.pop()
        
        # If we reached the target atom, a path exists
        if current_atom == atom2:
            return True
            
        for neighbor in adj[current_atom]:
            if neighbor not in visited:
                visited.add(neighbor)
                stack.append(neighbor)

    return False
