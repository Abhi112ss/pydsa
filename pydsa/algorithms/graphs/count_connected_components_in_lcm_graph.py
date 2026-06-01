METADATA = {
    "id": 3378,
    "name": "Count Connected Components in LCM Graph",
    "slug": "count-connected-components-in-lcm-graph",
    "category": "Graphs",
    "aliases": [],
    "tags": ["graphs", "union_find", "math"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Count the number of connected components in a graph where edges exist between numbers if their least common multiple is within a given range.",
}

def solve(n: int, m: int) -> int:
    """
    Args:
        n: The upper bound of the numbers in the set.
        m: The maximum allowed least common multiple.

    Returns:
        The number of connected components in the LCM graph.
    """
    parent = list(range(n + 1))
    components = n

    def find(i: int) -> int:
        root = i
        while parent[root] != root:
            root = parent[root]
        while parent[i] != root:
            next_node = parent[i]
            parent[i] = root
            i = next_node
        return root

    def union(i: int, j: int) -> bool:
        nonlocal components
        root_i = find(i)
        root_j = find(j)
        if root_i != root_j:
            parent[root_i] = root_j
            components -= 1
            return True
        return False

    for i in range(1, n + 1):
        for j in range(2 * i, n + 1, i):
            if (i * j) // i <= m:
                union(i, j)
            else:
                break

    return components