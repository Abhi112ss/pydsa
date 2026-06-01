METADATA = {
    "id": 867,
    "name": "Transpose Matrix",
    "slug": "transpose_matrix",
    "category": "Array",
    "aliases": [],
    "tags": ["matrix", "array_manipulation"],
    "difficulty": "easy",
    "time_complexity": "O(R * C)",
    "space_complexity": "O(R * C)",
    "description": "Given a 2D integer array matrix, return the transpose of matrix.",
}


def solve(matrix: list[list[int]]) -> list[list[int]]:
    """Return the transpose of a given 2D matrix.

    The transpose of a matrix is obtained by flipping it over its main diagonal,
    switching the row and column indices. Element at position [i][j] in the
    transposed matrix comes from position [j][i] in the original matrix.

    Args:
        matrix: A 2D list of integers with R rows and C columns.

    Returns:
        A new 2D list representing the transposed matrix with C rows and R columns.

    Examples:
        >>> solve([[1, 2, 3], [4, 5, 6]])
        [[1, 4], [2, 5], [3, 6]]
        >>> solve([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
        >>> solve([[1]])
        [[1]]
    """
    num_rows = len(matrix)
    num_cols = len(matrix[0])

    # Build the transposed matrix: each new row i collects column i from the original
    transposed: list[list[int]] = []
    for col_index in range(num_cols):
        new_row: list[int] = []
        for row_index in range(num_rows):
            # Element at [col_index][row_index] in transposed = [row_index][col_index] in original
            new_row.append(matrix[row_index][col_index])
        transposed.append(new_row)

    return transposed