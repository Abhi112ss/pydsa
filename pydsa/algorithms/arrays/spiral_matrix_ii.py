METADATA = {
    "id": 59,
    "name": "Spiral Matrix II",
    "slug": "spiral-matrix-ii",
    "category": "Matrix",
    "aliases": [],
    "tags": ["matrix", "simulation", "array_manipulation"],
    "difficulty": "medium",
    "time_complexity": "O(n^2)",
    "space_complexity": "O(1)",
    "description": "Generate an n x n matrix filled with elements from 1 to n^2 in spiral order.",
}

def solve(n: int) -> list[list[int]]:
    """
    Generates an n x n matrix filled with elements from 1 to n^2 in spiral order.

    Args:
        n: The dimension of the square matrix.

    Returns:
        A 2D list representing the n x n spiral matrix.

    Examples:
        >>> solve(3)
        [[1, 2, 3], [8, 9, 4], [7, 6, 5]]
        >>> solve(1)
        [[1]]
    """
    if n <= 0:
        return []

    # Initialize the matrix with zeros
    matrix = [[0] * n for _ in range(n)]
    
    # Define the boundaries of the current spiral layer
    top, bottom = 0, n - 1
    left, right = 0, n - 1
    
    current_value = 1
    total_elements = n * n

    while current_value <= total_elements:
        # 1. Traverse from left to right along the top boundary
        for col in range(left, right + 1):
            matrix[top][col] = current_value
            current_value += 1
        top += 1

        # 2. Traverse from top to bottom along the right boundary
        for row in range(top, bottom + 1):
            matrix[row][right] = current_value
            current_value += 1
        right -= 1

        # 3. Traverse from right to left along the bottom boundary
        # Check if top <= bottom to ensure we haven't crossed boundaries
        if top <= bottom:
            for col in range(right, left - 1, -1):
                matrix[bottom][col] = current_value
                current_value += 1
            bottom -= 1

        # 4. Traverse from bottom to top along the left boundary
        # Check if left <= right to ensure we haven't crossed boundaries
        if left <= right:
            for row in range(bottom, top - 1, -1):
                matrix[row][left] = current_value
                current_value += 1
            left += 1

    return matrix
