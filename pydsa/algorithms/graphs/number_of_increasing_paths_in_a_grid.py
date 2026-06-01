METADATA = {
    "id": 2328,
    "name": "Number of Increasing Paths in a Grid",
    "slug": "number-of-increasing-paths-in-a-grid",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dfs", "memoization", "dp", "matrix"],
    "difficulty": "hard",
    "time_complexity": "O(m * n)",
    "space_complexity": "O(m * n)",
    "description": "Find the total number of strictly increasing paths in a given grid.",
}

def solve(grid: list[list[int]]) -> int:
    """
    Calculates the total number of strictly increasing paths in a 2D grid.

    Args:
        grid: A 2D list of integers representing the grid values.

    Returns:
        The total count of strictly increasing paths modulo 10^9 + 7.

    Examples:
        >>> solve([[1,1],[3,3]])
        5
        >>> solve([[3,4,5],[3,2,6]])
        13
    """
    if not grid or not grid[0]:
        return 0

    rows = len(grid)
    cols = len(grid[0])
    MOD = 1_000_000_007

    # memo[r][c] stores the number of increasing paths starting from cell (r, c)
    memo: list[list[int]] = [[-1 for _ in range(cols)] for _ in range(rows)]

    def dfs(r: int, c: int) -> int:
        """
        Performs DFS with memoization to find paths starting from (r, c).
        """
        if memo[r][c] != -1:
            return memo[r][c]

        # Every single cell is a valid path of length 1
        count = 1

        # Explore 4-directional neighbors
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nr, nc = r + dr, c + dc

            # Check boundaries and the strictly increasing condition
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] > grid[r][c]:
                count = (count + dfs(nr, nc)) % MOD

        memo[r][c] = count
        return count

    total_paths = 0
    # Iterate through every cell in the grid as a potential starting point
    for r in range(rows):
        for c in range(cols):
            total_paths = (total_paths + dfs(r, c)) % MOD

    return total_paths
