METADATA = {
    "id": 1219,
    "name": "Path with Maximum Gold",
    "slug": "path-with-maximum-gold",
    "category": "Backtracking",
    "aliases": [],
    "tags": ["backtracking", "dfs", "matrix"],
    "difficulty": "medium",
    "time_complexity": "O(k * 3^k)",
    "space_complexity": "O(m * n)",
    "description": "Find the maximum amount of gold you can collect by following a path of non-zero cells without visiting the same cell twice.",
}

def solve(grid: list[list[int]]) -> int:
    """
    Finds the maximum gold that can be collected in a grid.

    Args:
        grid: A 2D list of integers representing the amount of gold in each cell.

    Returns:
        The maximum amount of gold that can be collected.

    Examples:
        >>> solve([[0,6,0],[5,8,7],[0,9,0]])
        26
        >>> solve([[1]])
        1
        >>> solve([[0,0,0],[0,0,0]])
        0
    """
    if not grid or not grid[0]:
        return 0

    rows = len(grid)
    cols = len(grid[0])
    max_gold = 0

    def backtrack(r: int, c: int) -> int:
        """
        Explores all possible paths starting from (r, c) using DFS.
        """
        # Base case: if out of bounds or cell has no gold
        if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == 0:
            return 0

        # Store current gold and mark cell as visited by setting it to 0
        current_gold = grid[r][c]
        grid[r][c] = 0
        
        local_max = 0
        # Explore 4 directions: up, down, left, right
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            local_max = max(local_max, backtrack(r + dr, c + dc))
        
        # Backtrack: restore the gold in the cell for other path explorations
        grid[r][c] = current_gold
        
        return current_gold + local_max

    # Iterate through every cell to find the best starting point
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] > 0:
                max_gold = max(max_gold, backtrack(r, c))

    return max_gold
