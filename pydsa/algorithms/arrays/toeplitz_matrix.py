METADATA = {
    "id": 766,
    "name": "Toeplitz Matrix",
    "slug": "toeplitz_matrix",
    "category": "Array",
    "aliases": [],
    "tags": ["arrays", "matrix"],
    "difficulty": "easy",
    "time_complexity": "O(m * n)",
    "space_complexity": "O(1)",
    "description": "Determine if a given matrix is Toeplitz, meaning every diagonal from top-left to bottom-right has the same elements.",
}


def solve(matrix: list[list[int]]) -> bool:
    """Check whether a matrix is Toeplitz.

    A matrix is Toeplitz if every diagonal from top-left to bottom-right
    contains the same element. This is verified by checking that each
    element (starting from the second row and second column) equals its
    top-left neighbor.

    Args:
        matrix: A 2D list of integers with dimensions m x n.

    Returns:
        True if the matrix is Toeplitz, False otherwise.

    Examples:
        >>> solve([[1, 2, 3, 4], [5, 1, 2, 3], [9, 5, 1, 2]])
        True
        >>> solve([[1, 2], [2, 2]])
        False
    """
    num_rows = len(matrix)
    num_cols = len(matrix[0])

    # Start from row 1, col 1 so that every element has a top-left neighbor.
    for row_index in range(1, num_rows):
        for col_index in range(1, num_cols):
            # Each element must match its top-left diagonal neighbor.
            if matrix[row_index][col_index] != matrix[row_index - 1][col_index - 1]:
                return False

    return True