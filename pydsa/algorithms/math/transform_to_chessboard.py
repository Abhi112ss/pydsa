METADATA = {
    "id": 782,
    "name": "Transform to Chessboard",
    "slug": "transform_to_chessboard",
    "category": "Matrix",
    "aliases": [],
    "tags": ["matrix", "greedy", "bit_manipulation"],
    "difficulty": "medium",
    "time_complexity": "O(n^2)",
    "space_complexity": "O(1)",
    "description": "Determine if a given n x n binary matrix can be transformed into a chessboard pattern by swapping rows and columns.",
}

def solve(board: list[list[int]]) -> bool:
    """
    Determines if an n x n binary matrix can be transformed into a chessboard pattern.
    
    A chessboard pattern is a matrix where no two adjacent cells (horizontally or vertically)
    have the same value. This can be achieved by swapping rows and columns.

    Args:
        board: A 2D list of integers representing the n x n binary matrix.

    Returns:
        True if the matrix can be transformed into a chessboard, False otherwise.

    Examples:
        >>> solve([[0, 1], [1, 0]])
        True
        >>> solve([[1, 0], [0, 1]])
        True
        >>> solve([[1, 1], [1, 1]])
        False
    """
    n = len(board)
    
    # 1. Check if the number of 0s and 1s in the first row is valid for a chessboard.
    # In a chessboard of size n, the count of 0s and 1s must be either (n//2, n//2 + n%2) 
    # or (n//2 + n%2, n//2).
    count_zero = 0
    count_one = 0
    for val in board[0]:
        if val == 0:
            count_zero += 1
        else:
            count_one += 1
            
    if abs(count_zero - count_one) > 1:
        return False

    # 2. Define the two possible valid row patterns.
    # Pattern A starts with 0, Pattern B starts with 1.
    pattern_a = [i % 2 for i in range(n)]
    pattern_b = [(i + 1) % 2 for i in range(n)]

    # 3. Validate all rows and columns.
    # Every row must match either pattern_a or pattern_b.
    # Additionally, if a row matches pattern_a, its complement must match pattern_b.
    # This also implicitly ensures that columns follow the same logic.
    
    # Check rows
    row_pattern_a_count = 0
    row_pattern_b_count = 0
    
    for row in board:
        if row == pattern_a:
            row_pattern_a_count += 1
        elif row == pattern_b:
            row_pattern_b_count += 1
        else:
            return False
            
    # For a valid chessboard, the number of rows matching pattern_a and pattern_b
    # must also be nearly equal (difference <= 1).
    if abs(row_pattern_a_count - row_pattern_b_count) > 1:
        return False

    # Check columns
    col_pattern_a_count = 0
    col_pattern_b_count = 0
    
    for col_idx in range(n):
        column = [board[row_idx][col_idx] for row_idx in range(n)]
        if column == pattern_a:
            col_pattern_a_count += 1
        elif column == pattern_b:
            col_pattern_b_count += 1
        else:
            return False
            
    if abs(col_pattern_a_count - col_pattern_b_count) > 1:
        return False

    return True
