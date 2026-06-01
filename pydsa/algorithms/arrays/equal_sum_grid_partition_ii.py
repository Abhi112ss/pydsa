METADATA = {
    "id": 3548,
    "name": "Equal Sum Grid Partition II",
    "slug": "equal_sum_grid_partition_ii",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dynamic_programming", "matrix", "grid"],
    "difficulty": "hard",
    "time_complexity": "O(m^2 * n^2)",
    "space_complexity": "O(m * n)",
    "description": "Partition a grid into four rectangular regions with equal sums using horizontal and vertical cuts.",
}

def solve(grid: list[list[int]]) -> bool:
    """
    Determines if a grid can be partitioned into four rectangular regions 
    with equal sums using one horizontal cut and one vertical cut.

    The partition is formed by a horizontal line at index 'i' and a 
    vertical line at index 'j', creating four quadrants:
    Top-Left, Top-Right, Bottom-Left, Bottom-Right.

    Args:
        grid: A 2D list of integers representing the grid.

    Returns:
        True if such a partition exists, False otherwise.

    Examples:
        >>> solve([[1, 1], [1, 1]])
        True
        >>> solve([[1, 2], [3, 4]])
        False
    """
    rows = len(grid)
    cols = len(grid[0])

    # Precompute 2D prefix sums for O(1) rectangle sum queries
    # prefix_sum[i][j] stores sum of grid[0...i-1][0...j-1]
    prefix_sum = [[0] * (cols + 1) for _ in range(rows + 1)]
    for r in range(rows):
        for c in range(cols):
            prefix_sum[r + 1][c + 1] = (
                grid[r][c]
                + prefix_sum[r][c + 1]
                + prefix_sum[r + 1][c]
                - prefix_sum[r][c]
            )

    def get_sum(r1: int, c1: int, r2: int, c2: int) -> int:
        """Returns the sum of the rectangle from (r1, c1) to (r2, c2) inclusive."""
        return (
            prefix_sum[r2 + 1][c2 + 1]
            - prefix_sum[r1][c2 + 1]
            - prefix_sum[r2 + 1][c1]
            + prefix_sum[r1][c1]
        )

    # Iterate through all possible horizontal cut positions
    # i is the index of the first row in the bottom half
    for i in range(1, rows):
        # Iterate through all possible vertical cut positions
        # j is the index of the first column in the right half
        for j in range(1, cols):
            # Calculate sums of the four quadrants
            # Top-Left: (0,0) to (i-1, j-1)
            sum_tl = get_sum(0, 0, i - 1, j - 1)
            # Top-Right: (0, j) to (i-1, cols-1)
            sum_tr = get_sum(0, j, i - 1, cols - 1)
            # Bottom-Left: (i, 0) to (rows-1, j-1)
            sum_bl = get_sum(i, 0, rows - 1, j - 1)
            # Bottom-Right: (i, j) to (rows-1, cols-1)
            sum_br = get_sum(i, j, rows - 1, cols - 1)

            # Check if all four quadrants have equal sums
            if sum_tl == sum_tr == sum_bl == sum_br:
                return True

    return False
