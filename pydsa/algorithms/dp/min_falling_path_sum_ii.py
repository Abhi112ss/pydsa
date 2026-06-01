METADATA = {
    "id": 1289,
    "name": "Minimum Falling Path Sum II",
    "slug": "minimum-falling-path-sum-ii",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dp", "matrix"],
    "difficulty": "hard",
    "time_complexity": "O(n^2)",
    "space_complexity": "O(n)",
    "description": "Find the minimum sum of a falling path in a matrix where no two elements in the path are in the same column.",
}

def solve(matrix: list[list[int]]) -> int:
    """
    Calculates the minimum falling path sum where no two elements are in the same column.

    Args:
        matrix: A 2D list of integers representing the grid.

    Returns:
        The minimum sum of a falling path.

    Examples:
        >>> solve([[2,1,3],[6,5,4],[7,8,9]])
        11
        >>> solve([[1,2,3],[4,5,6],[7,8,9]])
        12
    """
    if not matrix or not matrix[0]:
        return 0

    rows = len(matrix)
    cols = len(matrix[0])

    # prev_min1 stores the minimum sum ending in the previous row
    # prev_min2 stores the second minimum sum ending in the previous row (different column)
    # prev_col1 stores the column index of the minimum sum
    prev_min1 = 0
    prev_min2 = 0
    prev_col1 = -1

    for r in range(rows):
        curr_min1 = float('inf')
        curr_min2 = float('inf')
        curr_col1 = -1

        for c in range(cols):
            # If the current column is the same as the column of the previous minimum,
            # we must use the second minimum from the previous row to satisfy the constraint.
            if c == prev_col1:
                current_path_sum = matrix[r][c] + prev_min2
            else:
                current_path_sum = matrix[r][c] + prev_min1

            # Update the current row's minimum and second minimum values
            if current_path_sum < curr_min1:
                curr_min2 = curr_min1
                curr_min1 = current_path_sum
                curr_col1 = c
            elif current_path_sum < curr_min2:
                curr_min2 = current_path_sum

        # Move current row results to previous row trackers for the next iteration
        prev_min1 = curr_min1
        prev_min2 = curr_min2
        prev_col1 = curr_col1

    return int(prev_min1)
