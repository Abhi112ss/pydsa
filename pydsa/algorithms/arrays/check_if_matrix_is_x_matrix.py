METADATA = {
    "id": 2319,
    "name": "Check if Matrix Is X-Matrix",
    "slug": "check_if_matrix_is_x_matrix",
    "category": "array",
    "aliases": [],
    "tags": ["arrays"],
    "difficulty": "easy",
    "time_complexity": "O(m * n)",
    "space_complexity": "O(1)",
    "description": "Determine whether a given matrix is an X‑matrix, where all diagonal elements are non‑zero and all off‑diagonal elements are zero.",
}


def solve(matrix: list[list[int]]) -> bool:
    """Check if the given matrix is an X‑matrix.

    An X‑matrix satisfies:
    * Every element on the main diagonal (i == j) or the anti‑diagonal (i + j == n - 1) is non‑zero.
    * Every other element is zero.

    Args:
        matrix: A list of lists of integers representing a square matrix.

    Returns:
        True if the matrix is an X‑matrix, False otherwise.

    Examples:
        >>> solve([[2,0,0,1],[0,3,1,0],[0,1,4,0],[5,0,0,6]])
        True
        >>> solve([[5,0,0],[0,5,0],[0,0,5]])
        False
    """
    row_count: int = len(matrix)
    if row_count == 0:
        return False
    column_count: int = len(matrix[0])
    if row_count != column_count:
        return False

    size: int = row_count
    for row_index in range(size):
        for column_index in range(size):
            is_on_main_diagonal: bool = row_index == column_index
            is_on_anti_diagonal: bool = row_index + column_index == size - 1
            if is_on_main_diagonal or is_on_anti_diagonal:
                # Diagonal elements must be non‑zero
                if matrix[row_index][column_index] == 0:
                    return False
            else:
                # Off‑diagonal elements must be zero
                if matrix[row_index][column_index] != 0:
                    return False
    return True