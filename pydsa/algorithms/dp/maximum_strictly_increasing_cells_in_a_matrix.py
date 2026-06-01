METADATA = {
    "id": 2713,
    "name": "Maximum Strictly Increasing Cells in a Matrix",
    "slug": "maximum-strictly-increasing-cells-in-a-matrix",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dp", "graphs", "matrix", "dfs"],
    "difficulty": "hard",
    "time_complexity": "O(m * n)",
    "space_complexity": "O(m * n)",
    "description": "Find the maximum number of cells in a strictly increasing path within a matrix.",
}

def solve(matrix: list[list[int]]) -> int:
    """
    Finds the maximum number of cells in a strictly increasing path in a matrix.

    Args:
        matrix: A 2D list of integers representing the grid.

    Returns:
        The length of the longest strictly increasing path.

    Examples:
        >>> solve([[1, 2], [3, 4]])
        4
        >>> solve([[1, 1], [1, 1]])
        1
    """
    if not matrix or not matrix[0]:
        return 0

    rows = len(matrix)
    cols = len(matrix[0])
    
    # memo[r][c] stores the length of the longest increasing path starting from (r, c)
    memo: list[list[int]] = [[0] * cols for _ in range(rows)]

    def get_longest_path(r: int, c: int) -> int:
        # If already computed, return the cached value
        if memo[r][c] != 0:
            return memo[r][c]

        max_len = 1
        current_val = matrix[r][c]

        # Explore 4-directional neighbors
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nr, nc = r + dr, c + dc

            # Check boundaries and the strictly increasing condition
            if 0 <= nr < rows and 0 <= nc < cols and matrix[nr][nc] > current_val:
                max_len = max(max_len, 1 + get_longest_path(nr, nc))

        # Cache the result for this cell
        memo[r][c] = max_len
        return max_len

    overall_max = 0
    # Iterate through every cell to ensure we find the global maximum
    for r in range(rows):
        for c in range(cols):
            overall_max = max(overall_max, get_longest_path(r, c))

    return overall_max
