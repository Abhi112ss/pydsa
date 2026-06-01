METADATA = {
    "id": 562,
    "name": "Longest Line of Consecutive One in Matrix",
    "slug": "longest-line-of-consecutive-one-in-matrix",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dynamic_programming", "matrix", "array"],
    "difficulty": "medium",
    "time_complexity": "O(m * n)",
    "space_complexity": "O(m * n)",
    "description": "Find the longest line of consecutive ones in a 2D matrix in four directions: horizontal, vertical, and two diagonals.",
}

def solve(matrix: list[list[int]]) -> int:
    """
    Finds the length of the longest line of consecutive ones in a 2D matrix.
    The line can be horizontal, vertical, or diagonal (both directions).

    Args:
        matrix: A 2D list of integers where 0 represents empty and 1 represents a line.

    Returns:
        The length of the longest consecutive line of ones.

    Examples:
        >>> solve([[0,1,0],[1,1,1],[0,1,0]])
        3
        >>> solve([[1,1,0,0,0],[0,1,1,0,0],[0,0,1,1,0],[0,0,0,1,1]])
        2
    """
    if not matrix or not matrix[0]:
        return 0

    rows = len(matrix)
    cols = len(matrix[0])
    max_length = 0

    # dp[r][c] will store a dictionary or list representing the length of 
    # consecutive ones ending at (r, c) for 4 directions:
    # 0: Horizontal (left to right)
    # 1: Vertical (top to bottom)
    # 2: Diagonal (top-left to bottom-right)
    # 3: Anti-diagonal (top-right to bottom-left)
    dp = [[[0] * 4 for _ in range(cols)] for _ in range(rows)]

    for r in range(rows):
        for c in range(cols):
            if matrix[r][c] == 1:
                # 1. Horizontal: check cell to the left
                dp[r][c][0] = (dp[r][c - 1][0] + 1) if c > 0 else 1
                
                # 2. Vertical: check cell above
                dp[r][c][1] = (dp[r - 1][c][1] + 1) if r > 0 else 1
                
                # 3. Diagonal: check cell top-left
                dp[r][c][2] = (dp[r - 1][c - 1][2] + 1) if (r > 0 and c > 0) else 1
                
                # 4. Anti-diagonal: check cell top-right
                dp[r][c][3] = (dp[r - 1][c + 1][3] + 1) if (r > 0 and c < cols - 1) else 1
                
                # Update the global maximum with the best direction at this cell
                current_max = max(dp[r][c])
                if current_max > max_length:
                    max_length = current_max

    return max_length
