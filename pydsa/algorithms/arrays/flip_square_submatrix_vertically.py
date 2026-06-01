METADATA = {
    "id": 3643,
    "name": "Flip Square Submatrix Vertically",
    "slug": "flip_square_submatrix_vertically",
    "category": "Matrix",
    "aliases": [],
    "tags": ["matrix", "simulation"],
    "difficulty": "medium",
    "time_complexity": "O(n^2)",
    "space_complexity": "O(1)",
    "description": "Flips a square submatrix within a given matrix vertically.",
}

def solve(matrix: list[list[int]], row_start: int, col_start: int, size: int) -> list[list[int]]:
    """
    Flips a square submatrix of a given size vertically within the provided matrix.

    The flip is performed in-place by swapping elements across the horizontal 
    center line of the submatrix.

    Args:
        matrix: A 2D list of integers representing the input matrix.
        row_start: The starting row index of the submatrix.
        col_start: The starting column index of the submatrix.
        size: The side length of the square submatrix.

    Returns:
        The modified matrix after the vertical flip.

    Examples:
        >>> matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        >>> solve(matrix, 0, 0, 2)
        [[4, 5, 3], [1, 2, 6], [7, 8, 9]]
    """
    # The vertical flip means the top row of the submatrix swaps with the bottom row,
    # the second row swaps with the second-to-last, and so on.
    # We only need to iterate through half of the submatrix height.
    for i in range(size // 2):
        # Calculate the indices of the two rows to be swapped
        top_row_idx = row_start + i
        bottom_row_idx = row_start + size - 1 - i
        
        # Swap elements within the columns defined by the submatrix boundaries
        for j in range(col_start, col_start + size):
            matrix[top_row_idx][j], matrix[bottom_row_idx][j] = (
                matrix[bottom_row_idx][j],
                matrix[top_row_idx][j],
            )
            
    return matrix
