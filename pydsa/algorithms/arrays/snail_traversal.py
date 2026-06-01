METADATA = {
    "id": 2624,
    "name": "Snail Traversal",
    "slug": "snail_traversal",
    "category": "Simulation",
    "aliases": [],
    "tags": ["simulation", "matrix", "array"],
    "difficulty": "medium",
    "time_complexity": "O(m * n)",
    "space_complexity": "O(1)",
    "description": "Traverse a 2D matrix in a spiral (snail) pattern starting from the top-left corner.",
}

def solve(matrix: list[list[int]]) -> list[int]:
    """
    Traverses a 2D matrix in a spiral (snail) pattern.

    Args:
        matrix: A 2D list of integers representing the matrix.

    Returns:
        A 1D list of integers containing the elements in spiral order.

    Examples:
        >>> solve([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        [1, 2, 3, 6, 9, 8, 7, 4, 5]
        >>> solve([[1, 2], [3, 4]])
        [1, 2, 4, 3]
    """
    if not matrix or not matrix[0]:
        return []

    rows = len(matrix)
    cols = len(matrix[0])
    result = []

    # Define the boundaries of the current spiral layer
    top, bottom = 0, rows - 1
    left, right = 0, cols - 1

    while top <= bottom and left <= right:
        # 1. Traverse from left to right along the top boundary
        for col_idx in range(left, right + 1):
            result.append(matrix[top][col_idx])
        top += 1

        # 2. Traverse from top to bottom along the right boundary
        for row_idx in range(top, bottom + 1):
            result.append(matrix[row_idx][right])
        right -= 1

        # Check if we still have a valid sub-matrix to traverse
        if top <= bottom:
            # 3. Traverse from right to left along the bottom boundary
            for col_idx in range(right, left - 1, -1):
                result.append(matrix[bottom][col_idx])
            bottom -= 1

        if left <= right:
            # 4. Traverse from bottom to top along the left boundary
            for row_idx in range(bottom, top - 1, -1):
                result.append(matrix[row_idx][left])
            left += 1

    return result
