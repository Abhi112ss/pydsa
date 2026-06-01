METADATA = {
    "id": 959,
    "name": "Regions Cut By Slashes",
    "slug": "regions-cut-by-slashes",
    "category": "Union Find",
    "aliases": [],
    "tags": ["union_find", "dfs", "grid_traversal"],
    "difficulty": "medium",
    "time_complexity": "O(n^2 alpha(n))",
    "space_complexity": "O(n^2)",
    "description": "Count the number of regions formed by slashes, backslashes, and spaces in an n x n grid.",
}

def solve(grid: list[str]) -> int:
    """
    Args:
        grid: A list of strings representing the n x n grid.

    Returns:
        The total number of regions formed.
    """
    n = len(grid)
    parent = list(range(4 * n * n))
    num_components = 4 * n * n

    def find(i: int) -> int:
        if parent[i] == i:
            return i
        parent[i] = find(parent[i])
        return parent[i]

    def union(i: int, j: int) -> int:
        nonlocal num_components
        root_i = find(i)
        root_j = find(j)
        if root_i != root_j:
            parent[root_i] = root_j
            num_components -= 1
            return num_components - 1
        return num_components

    for r in range(n):
        for c in range(n):
            root_index = 4 * (r * n + c)
            char = grid[r][c]

            if char == ' ':
                union(root_index + 0, root_index + 1)
                union(root_index + 1, root_index + 2)
                union(root_index + 2, root_index + 3)
            elif char == '/':
                union(root_index + 0, root_index + 3)
                union(root_index + 1, root_index + 2)
            elif char == '\\':
                union(root_index + 0, root_index + 1)
                union(root_index + 2, root_index + 3)

            if r + 1 < n:
                below_index = 4 * ((r + 1) * n + c)
                union(root_index + 2, below_index + 0)
                union(root_index + 3, below_index + 1)
            
            if c + 1 < n:
                right_index = 4 * (r * n + (c + 1))
                union(root_index + 1, right_index + 3)
                union(root_index + 2, right_index + 0)

    unique_regions = set()
    for i in range(4 * n * n):
        unique_regions.add(find(i))
        
    return len(unique_regions)