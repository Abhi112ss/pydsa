METADATA = {
    "id": 1292,
    "name": "Maximum Side Length of a Square with Sum Less than or Equal to Threshold",
    "slug": "maximum-side-length-of-a-square-with-sum-less-than-or-equal-to-threshold",
    "category": "Matrix",
    "aliases": [],
    "tags": ["prefix_sum", "binary_search", "matrix"],
    "difficulty": "medium",
    "time_complexity": "O(m*n log(min(m,n)))",
    "space_complexity": "O(m*n)",
    "description": "Find the maximum side length of a square submatrix whose sum is less than or equal to a given threshold using 2D prefix sums and binary search.",
}

def solve(grid: list[list[int]], threshold: int) -> int:
    """
    Finds the maximum side length of a square submatrix with a sum <= threshold.

    Args:
        grid: A 2D list of integers representing the matrix.
        threshold: The maximum allowed sum for the square submatrix.

    Returns:
        The maximum side length of such a square.

    Examples:
        >>> solve([[1, 4, 5], [1, 1, 1], [1, 1, 1]], 4)
        2
        >>> solve([[4, 4], [4, 4]], 15)
        1
    """
    rows = len(grid)
    cols = len(grid[0])

    # Create a 2D prefix sum array (padded with zeros for easier boundary handling)
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

    def can_fit_square(side_length: int) -> bool:
        """Checks if there exists any square of side_length with sum <= threshold."""
        if side_length == 0:
            return True
        
        for r in range(side_length, rows + 1):
            for c in range(side_length, cols + 1):
                # Calculate sum of submatrix using the inclusion-exclusion principle
                current_sum = (
                    prefix_sum[r][c]
                    - prefix_sum[r - side_length][c]
                    - prefix_sum[r][c - side_length]
                    + prefix_sum[r - side_length][c - side_length]
                )
                if current_sum <= threshold:
                    return True
        return False

    # Binary search for the maximum possible side length
    low = 1
    high = min(rows, cols)
    max_side = 0

    while low <= high:
        mid = (low + high) // 2
        if can_fit_square(mid):
            max_side = mid
            low = mid + 1
        else:
            high = mid - 1

    return max_side
