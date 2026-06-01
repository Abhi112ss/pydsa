METADATA = {
    "id": 1582,
    "name": "Special Positions in a Binary Matrix",
    "slug": "special-positions-in-a-binary-matrix",
    "category": "Matrix",
    "aliases": [],
    "tags": ["matrix", "prefix_sum", "counting"],
    "difficulty": "medium",
    "time_complexity": "O(m * n)",
    "space_complexity": "O(m + n)",
    "description": "Find the number of cells containing 1 such that the sum of its row and column is equal to 2.",
}

def solve(mat: list[list[int]]) -> int:
    """
    Finds the number of special positions in a binary matrix.
    A position (r, c) is special if mat[r][c] == 1 and the sum of 
    elements in row r and column c is exactly 2.

    Args:
        mat: A 2D list of integers representing a binary matrix.

    Returns:
        The count of special positions.

    Examples:
        >>> solve([[1, 0, 0], [0, 0, 0], [0, 0, 1]])
        2
        >>> solve([[1, 1], [1, 1]])
        0
    """
    if not mat or not mat[0]:
        return 0

    rows_count = len(mat)
    cols_count = len(mat[0])

    # Precompute the sum of 1s for every row and every column
    row_sums = [0] * rows_count
    col_sums = [0] * cols_count

    for r in range(rows_count):
        for c in range(cols_count):
            if mat[r][c] == 1:
                row_sums[r] += 1
                col_sums[c] += 1

    special_positions_count = 0

    # Iterate through the matrix to find cells that satisfy the condition
    for r in range(rows_count):
        # Optimization: if row sum is not 1, no cell in this row can be special
        # because row_sum + col_sum must equal 2, and mat[r][c] is 1.
        # Therefore, col_sum must be 1.
        if row_sums[r] == 1:
            for c in range(cols_count):
                if mat[r][c] == 1:
                    # Check if the column sum is also exactly 1
                    if col_sums[c] == 1:
                        special_positions_count += 1

    return special_positions_count
