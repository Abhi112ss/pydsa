METADATA = {
    "id": 566,
    "name": "Reshape the Matrix",
    "slug": "reshape_the_matrix",
    "category": "Array",
    "aliases": [],
    "tags": ["matrix", "array"],
    "difficulty": "medium",
    "time_complexity": "O(m * n)",
    "space_complexity": "O(m * n)",
    "description": "Convert a matrix to a different size while preserving element order.",
}


def solve(matrix: list[list[int]], r: int, c: int) -> list[list[int]]:
    """Reshape a given matrix to the desired dimensions.

    Args:
        matrix: A 2‑D list representing the original m × n matrix.
        r: Desired number of rows in the reshaped matrix.
        c: Desired number of columns in the reshaped matrix.

    Returns:
        A new matrix with dimensions r × c containing the same elements
        in row‑major order if reshaping is possible; otherwise, the original
        matrix is returned unchanged.

    Examples:
        >>> solve([[1,2],[3,4]], 1, 4)
        [[1, 2, 3, 4]]
        >>> solve([[1,2,3],[4,5,6]], 3, 2)
        [[1, 2], [3, 4], [5, 6]]
        >>> solve([[1,2],[3,4]], 2, 3)
        [[1, 2], [3, 4]]
    """
    original_row_count = len(matrix)
    original_col_count = len(matrix[0]) if matrix else 0
    total_elements = original_row_count * original_col_count

    # If the total number of elements does not match, reshaping is impossible.
    if total_elements != r * c:
        return matrix

    # Prepare the result matrix filled with zeros.
    reshaped = [[0 for _ in range(c)] for _ in range(r)]

    for linear_index in range(total_elements):
        # Map linear index to coordinates in the original matrix.
        original_row = linear_index // original_col_count
        original_col = linear_index % original_col_count

        # Map linear index to coordinates in the reshaped matrix.
        new_row = linear_index // c
        new_col = linear_index % c

        reshaped[new_row][new_col] = matrix[original_row][original_col]

    return reshaped