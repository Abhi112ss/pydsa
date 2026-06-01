METADATA = {
    "id": 2056,
    "name": "Number of Valid Move Combinations On Chessboard",
    "slug": "number-of-valid-move-combinations-on-chessboard",
    "category": "Math",
    "aliases": [],
    "tags": ["math", "combinatorics"],
    "difficulty": "medium",
    "time_complexity": "O(1)",
    "space_complexity": "O(1)",
    "description": "Calculate the number of ways to place two non-attacking knights on an m x n chessboard.",
}

def solve(m: int, n: int) -> int:
    """
    Calculates the number of ways to place two knights on an m x n chessboard 
    such that they do not attack each other.

    The total number of ways to place two distinct knights is (m * n) * (m * n - 1).
    However, since the problem asks for combinations (unordered pairs), we use 
    (m * n * (m * n - 1)) // 2.
    A knight attacks another if they are in a 2x3 or 3x2 rectangle. 
    Each such rectangle contains exactly two pairs of attacking knights.

    Args:
        m: The number of rows on the chessboard.
        n: The number of columns on the chessboard.

    Returns:
        The total number of valid combinations of two non-attacking knights.

    Examples:
        >>> solve(3, 3)
        36
        >>> solve(2, 4)
        24
    """
    # Total ways to choose 2 squares out of m * n squares
    total_squares = m * n
    total_combinations = (total_squares * (total_squares - 1)) // 2

    # A knight attack occurs within every 2x3 or 3x2 sub-grid.
    # In a 2x3 sub-grid, there are 2 possible attacking pairs.
    # In a 3x2 sub-grid, there are 2 possible attacking pairs.
    
    # Number of 2x3 rectangles: (m-1) * (n-2)
    # Number of 3x2 rectangles: (m-2) * (n-1)
    
    attacking_pairs = 0
    
    if m >= 1 and n >= 3:
        attacking_pairs += (m - 1) * (n - 2) * 2
        
    if m >= 3 and n >= 1:
        attacking_pairs += (m - 2) * (n - 1) * 2

    # The result is total combinations minus the number of attacking pairs
    return total_combinations - attacking_pairs
