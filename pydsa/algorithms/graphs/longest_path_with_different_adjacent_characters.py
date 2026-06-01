METADATA = {
    "id": 2246,
    "name": "Longest Path With Different Adjacent Characters",
    "slug": "longest-path-with-different-adjacent-characters",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dfs", "dp", "grid"],
    "difficulty": "hard",
    "time_complexity": "O(m * n)",
    "space_complexity": "O(m * n)",
    "description": "Find the length of the longest path in a grid where every adjacent character in the path is different.",
}

def solve(grid: list[list[str]]) -> int:
    """
    Finds the length of the longest path in a grid where no two adjacent 
    characters in the path are the same.

    Args:
        grid: A 2D list of characters representing the grid.

    Returns:
        The length of the longest valid path.

    Examples:
        >>> solve([["a","b","a"],["b","a","b"],["a","b","a"]])
        1
        >>> solve([["a","a","a"],["a","b","a"],["a","a","a"]])
        2
    """
    if not grid or not grid[0]:
        return 0

    rows = len(grid)
    cols = len(grid[0])
    # memo[r][c] stores the longest path starting from cell (r, c)
    memo: list[list[int]] = [[-1 for _ in range(cols)] for _ in range(rows)]

    def get_longest_path_from(r: int, c: int) -> int:
        """Recursive DFS with memoization to find the longest path from (r, c)."""
        if memo[r][c] != -1:
            return memo[r][c]

        max_len = 1
        current_char = grid[r][c]

        # Explore all 4 directions: up, down, left, right
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nr, nc = r + dr, c + dc

            # Check boundaries and ensure the adjacent character is different
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] != current_char:
                # The path length from current cell is 1 + path length from neighbor
                max_len = max(max_len, 1 + get_longest_path_from(nr, nc))

        memo[r][c] = max_len
        return max_len

    longest_overall_path = 0
    # We must attempt to start a path from every single cell in the grid
    for r in range(rows):
        for c in range(cols):
            longest_overall_path = max(longest_overall_path, get_longest_path_from(r, c))

    return longest_overall_path
