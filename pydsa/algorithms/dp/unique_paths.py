METADATA = {
    "id": 62,
    "name": "Unique Paths",
    "slug": "unique-paths",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dynamic_programming", "math", "combinatorics"],
    "difficulty": "medium",
    "time_complexity": "O(m * n)",
    "space_complexity": "O(n)",
    "description": "Calculate the number of possible unique paths from the top-left corner to the bottom-right corner of an m x n grid, moving only down or right.",
}

def solve(m: int, n: int) -> int:
    """
    Calculates the number of unique paths in an m x n grid using dynamic programming.

    The algorithm uses a space-optimized 1D array to store the number of ways 
    to reach each column in the current row.

    Args:
        m: The number of rows in the grid.
        n: The number of columns in the grid.

    Returns:
        The total number of unique paths from (0, 0) to (m-1, n-1).

    Examples:
        >>> solve(3, 7)
        28
        >>> solve(3, 2)
        3
    """
    # If the grid is empty or invalid, there are no paths.
    if m <= 0 or n <= 0:
        return 0

    # We use a 1D array to represent the current row being processed.
    # Initialize with 1s because there is only 1 way to reach any cell in the first row.
    current_row_paths = [1] * n

    # Iterate through each row starting from the second row (index 1).
    for row_index in range(1, m):
        # Iterate through each column starting from the second column (index 1).
        # The first column (index 0) always remains 1 because there's only one way to go straight down.
        for col_index in range(1, n):
            # The number of ways to reach the current cell is the sum of:
            # 1. Ways to reach the cell above (already stored in current_row_paths[col_index])
            # 2. Ways to reach the cell to the left (newly updated current_row_paths[col_index - 1])
            current_row_paths[col_index] += current_row_paths[col_index - 1]

    return current_row_paths[n - 1]
