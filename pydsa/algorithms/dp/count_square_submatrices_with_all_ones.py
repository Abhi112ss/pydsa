METADATA = {
    "id": 1277,
    "name": "Count Square Submatrices with All Ones",
    "slug": "count-square-submatrices-with-all-ones",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dynamic_programming", "matrix"],
    "difficulty": "medium",
    "time_complexity": "O(m * n)",
    "space_complexity": "O(m * n)",
    "description": "Count the total number of square submatrices that contain only ones.",
}

def solve(matrix: list[list[int]]) -> int:
    """
    Counts the total number of square submatrices with all ones in a given matrix.

    The algorithm uses dynamic programming where dp[i][j] represents the side 
    length of the largest square submatrix whose bottom-right corner is at (i, j).
    The value of dp[i][j] also happens to be the number of square submatrices 
    ending at that specific cell.

    Args:
        matrix: A 2D list of integers where each element is either 0 or 1.

    Returns:
        The total count of square submatrices containing only ones.

    Examples:
        >>> solve([[0,1,1,1],[1,1,1,1],[0,1,1,1]])
        15
        >>> solve([[1]])
        1
    """
    if not matrix or not matrix[0]:
        return 0

    rows = len(matrix)
    cols = len(matrix[0])
    
    # Initialize a DP table with the same dimensions as the matrix
    # dp[i][j] stores the side length of the largest square ending at (i, j)
    dp = [[0] * cols for _ in range(rows)]
    total_squares = 0

    for i in range(rows):
        for j in range(cols):
            # Only process if the current cell contains a 1
            if matrix[i][j] == 1:
                # If we are at the first row or first column, 
                # the largest square ending here is just the cell itself (size 1)
                if i == 0 or j == 0:
                    dp[i][j] = 1
                else:
                    # The size of the square is limited by the minimum of its 
                    # top, left, and top-left neighbors plus 1
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
                
                # The value in dp[i][j] is exactly the number of squares 
                # that have (i, j) as their bottom-right corner
                total_squares += dp[i][j]

    return total_squares
