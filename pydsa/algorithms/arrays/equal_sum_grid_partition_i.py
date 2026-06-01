METADATA = {
    "id": 3546,
    "name": "Equal Sum Grid Partition I",
    "slug": "equal_sum_grid_partition_i",
    "category": "Matrix",
    "aliases": [],
    "tags": ["prefix_sum", "matrix"],
    "difficulty": "medium",
    "time_complexity": "O(m * n)",
    "space_complexity": "O(m * n)",
    "description": "Determine if a grid can be partitioned into four equal-sum rectangular subgrids using a single horizontal and a single vertical cut.",
}

def solve(grid: list[list[int]]) -> bool:
    """
    Determines if a grid can be partitioned into four equal-sum rectangular subgrids
    by making one horizontal cut and one vertical cut.

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

    # Build a 2D prefix sum table to allow O(1) subgrid sum queries.
    # prefix_sum[i][j] stores the sum of grid[0...i-1][0...j-1]
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

    total_sum = prefix_sum[rows][cols]

    # A partition into 4 equal parts is only possible if the total sum is divisible by 4.
    if total_sum % 4 != 0:
        return False
    
    target = total_sum // 4

    # Iterate through all possible horizontal cut positions (after row i)
    # and all possible vertical cut positions (after column j).
    # A cut at row i means the top part is rows 0 to i.
    # A cut at col j means the left part is cols 0 to j.
    for i in range(rows - 1):
        for j in range(cols - 1):
            # Top-left quadrant: (0, 0) to (i, j)
            if get_sum(0, 0, i, j) != target:
                continue
            
            # Top-right quadrant: (0, j+1) to (i, cols-1)
            if get_sum(0, j + 1, i, cols - 1) != target:
                continue
            
            # Bottom-left quadrant: (i+1, 0) to (rows-1, j)
            if get_sum(i + 1, 0, rows - 1, j) != target:
                continue
            
            # Bottom-right quadrant: (i+1, j+1) to (rows-1, cols-1)
            if get_sum(i + 1, j + 1, rows - 1, cols - 1) != target:
                continue
            
            # If all four quadrants equal the target, we found a valid partition.
            return True

    return False
