METADATA = {
    "id": 2975,
    "name": "Maximum Square Area by Removing Fences From a Field",
    "slug": "maximum-square-area-by-removing-fences-from-a-field",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dp", "arrays", "matrix"],
    "difficulty": "medium",
    "time_complexity": "O(rows * cols)",
    "space_complexity": "O(rows * cols)",
    "description": "Find the area of the largest square containing only 1s in a binary matrix.",
}

def solve(matrix: list[list[int]]) -> int:
    """
    Finds the area of the largest square containing only 1s in a binary matrix.

    Args:
        matrix: A 2D list of integers where 1 represents a field and 0 represents a fence.

    Returns:
        The area of the largest square of 1s.

    Examples:
        >>> solve([[1, 0, 1], [1, 1, 1], [1, 1, 1]])
        4
        >>> solve([[0, 0], [0, 0]])
        0
    """
    if not matrix or not matrix[0]:
        return 0

    rows = len(matrix)
    cols = len(matrix[0])
    
    # dp[i][j] represents the side length of the largest square 
    # whose bottom-right corner is at cell (i, j).
    dp = [[0] * cols for _ in range(rows)]
    max_side = 0

    for r in range(rows):
        for c in range(cols):
            # Only process if the current cell is a field (1)
            if matrix[r][c] == 1:
                # If we are at the top row or leftmost column, 
                # the largest square ending here is just the cell itself.
                if r == 0 or c == 0:
                    dp[r][c] = 1
                else:
                    # The side length is determined by the minimum of the 
                    # three adjacent squares (top, left, top-left) plus 1.
                    dp[r][c] = min(dp[r - 1][c], dp[r][c - 1], dp[r - 1][c - 1]) + 1
                
                # Track the maximum side length found so far
                if dp[r][c] > max_side:
                    max_side = dp[r][c]

    # The area of the square is the side length squared
    return max_side * max_side
