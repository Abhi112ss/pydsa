METADATA = {
    "id": 1222,
    "name": "Queens That Can Attack the King",
    "slug": "queens-that-can-attack-the-king",
    "category": "Simulation",
    "aliases": [],
    "tags": ["array", "matrix", "simulation"],
    "difficulty": "medium",
    "time_complexity": "O(1)",
    "space_complexity": "O(1)",
    "description": "Count how many queens can attack a king on an n x n chessboard.",
}

def solve(board: list[list[str]]) -> int:
    """
    Counts the number of queens that can attack the king on an n x n chessboard.

    A queen can attack the king if it is in the same row, column, or diagonal
    as the king and there are no other pieces between them.

    Args:
        board: An n x n grid of strings where 'K' is the king and 'Q' is a queen.

    Returns:
        The total number of queens that can attack the king.

    Examples:
        >>> solve([["..Q", "K..", "..."]])
        1
        >>> solve([["..Q", ".K.", "Q.."]])
        2
    """
    n = len(board)
    king_row, king_col = -1, -1

    # Find the position of the king
    for r in range(n):
        for c in range(n):
            if board[r][c] == 'K':
                king_row, king_col = r, c
                break
        if king_row != -1:
            break

    # The 8 possible directions a queen can move to attack a king
    directions = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),           (0, 1),
        (1, -1),  (1, 0),  (1, 1)
    ]

    attack_count = 0

    for dr, dc in directions:
        r, c = king_row + dr, king_col + dc
        
        # Traverse in the current direction until we hit the board edge
        while 0 <= r < n and 0 <= c < n:
            if board[r][c] == 'Q':
                # Found a queen that can attack the king
                attack_count += 1
                break
            # If we hit another piece (though problem implies only K and Q), 
            # we would stop, but here we only care about finding the first Q.
            # In this specific problem, there are no other pieces besides K and Q.
            r += dr
            c += dc

    return attack_count
