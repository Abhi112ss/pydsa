METADATA = {
    "id": 54,
    "name": "Spiral Matrix",
    "slug": "spiral_matrix",
    "category": "Array",
    "aliases": [],
    "tags": ["matrix", "simulation", "array_manipulation"],
    "difficulty": "medium",
    "time_complexity": "O(m*n)",
    "space_complexity": "O(1)",
    "description": "Return all elements of the matrix in spiral order.",
}

def solve(matrix: list[list[int]]) -> list[int]:
    """
    Traverses a 2D matrix in a spiral order starting from the top-left corner.

    Args:
        matrix: A 2D list of integers representing the input matrix.

    Returns:
        A list of integers containing the elements of the matrix in spiral order.

    Examples:
        >>> solve([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        [1, 2, 3, 6, 9, 8, 7, 4, 5]
        >>> solve([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
        [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]
    """
    if not matrix or not matrix[0]:
        return []

    rows = len(matrix)
    cols = len(matrix[0])
    result = []

    # Define the boundaries of the current spiral layer
    top_boundary = 0
    bottom_boundary = rows - 1
    left_boundary = 0
    right_boundary = cols - 1

    while top_boundary <= bottom_boundary and left_boundary <= right_boundary:
        # 1. Traverse from left to right along the top boundary
        for col_index in range(left_boundary, right_boundary + 1):
            result.append(matrix[top_boundary][col_index])
        top_boundary += 1

        # 2. Traverse from top to bottom along the right boundary
        for row_index in range(top_boundary, bottom_boundary + 1):
            result.append(matrix[row_index][right_boundary])
        right_boundary -= 1

        # Check if boundaries have crossed after updating top and right
        if top_boundary <= bottom_boundary:
            # 3. Traverse from right to left along the bottom boundary
            for col_index in range(right_boundary, left_boundary - 1, -1):
                result.append(matrix[bottom_boundary][col_index])
            bottom_boundary -= 1

        if left_boundary <= right_boundary:
            # 4. Traverse from bottom to top along the left boundary
            for row_index in range(bottom_boundary, top_boundary - 1, -1):
                result.append(matrix[row_index][left_boundary])
            left_boundary += 1

    return result
