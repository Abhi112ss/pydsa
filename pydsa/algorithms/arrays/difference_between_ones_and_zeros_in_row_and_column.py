METADATA = {
    "id": 2482,
    "name": "Difference Between Ones and Zeros in Row and Column",
    "slug": "difference_between_ones_and_zeros_in_row_and_column",
    "category": "array",
    "aliases": [],
    "tags": ["matrix", "array"],
    "difficulty": "medium",
    "time_complexity": "O(m*n)",
    "space_complexity": "O(m+n)",
    "description": "Return a matrix where each cell contains the difference between the number of ones and zeros in its row and column.",
}


def solve(grid: list[list[int]]) -> list[list[int]]:
    """Compute the difference between the number of ones and zeros in each row and column.

    For each cell (i, j) in the binary matrix `grid`, the result is:
        (row_ones[i] - row_zeros[i]) + (col_ones[j] - col_zeros[j])

    Args:
        grid: A list of `m` rows, each containing `n` binary integers (0 or 1).

    Returns:
        A new matrix of the same dimensions where each entry holds the described difference.

    Examples:
        >>> solve([[0,1,1],[1,0,1],[0,0,0]])
        [[0, 0, 2], [2, 0, 2], [-2, -2, 0]]
        >>> solve([[1]])
        [[2]]
    """
    if not grid:
        return []

    row_count = len(grid)
    col_count = len(grid[0])

    # First pass: count ones in each column.
    column_ones = [0] * col_count
    for row in grid:
        for col_index, value in enumerate(row):
            column_ones[col_index] += value

    # Second pass: build answer while counting ones in the current row.
    answer = []
    for row in grid:
        row_ones = sum(row)                     # total ones in this row
        row_diff = 2 * row_ones - col_count      # (row_ones - row_zeros)
        answer_row = []
        for col_index, value in enumerate(row):
            col_diff = 2 * column_ones[col_index] - row_count  # (col_ones - col_zeros)
            answer_row.append(row_diff + col_diff)
        answer.append(answer_row)

    return answer