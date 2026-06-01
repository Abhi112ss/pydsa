METADATA = {
    "id": 48,
    "name": "Rotate Image",
    "slug": "rotate-image",
    "category": "Matrix",
    "aliases": [],
    "tags": ["matrix", "math", "array_manipulation"],
    "difficulty": "medium",
    "time_complexity": "O(n^2)",
    "space_complexity": "O(1)",
    "description": "Rotate an n x n 2D matrix by 90 degrees clockwise in-place.",
}

def solve(matrix: list[list[int]]) -> None:
    """
    Rotates the n x n matrix 90 degrees clockwise in-place.

    The transformation is achieved in two steps:
    1. Transpose the matrix (swap matrix[i][j] with matrix[j][i]).
    2. Reverse each row.

    Args:
        matrix: A list of lists of integers representing an n x n matrix.

    Returns:
        None. The operation is performed in-place.

    Examples:
        >>> mat = [[1,2,3],[4,5,6],[7,8,9]]
        >>> solve(mat)
        >>> mat
        [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
    """
    n = len(matrix)

    # Step 1: Transpose the matrix
    # We iterate through the upper triangle (j > i) to avoid swapping elements back
    for row_index in range(n):
        for col_index in range(row_index + 1, n):
            matrix[row_index][col_index], matrix[col_index][row_index] = (
                matrix[col_index][row_index],
                matrix[row_index][col_index],
            )

    # Step 2: Reverse each row
    # Reversing the elements in each row completes the 90-degree clockwise rotation
    for row_index in range(n):
        matrix[row_index].reverse()
