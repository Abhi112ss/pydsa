METADATA = {
    "id": 419,
    "name": "Battleships in a Board",
    "slug": "battleships-in-a-board",
    "category": "Matrix",
    "aliases": [],
    "tags": ["matrix", "traversal"],
    "difficulty": "medium",
    "time_complexity": "O(m*n)",
    "space_complexity": "O(1)",
    "description": "Count the number of battleships in a 2D board where ships are placed horizontally or vertically and do not touch.",
}

def solve(board: list[list[str]]) -> int:
    """
    Counts the number of battleships in a given 2D board.

    A battleship is represented by 'X' and empty spaces by '.'. 
    Ships are placed horizontally or vertically and do not touch each other.
    The algorithm identifies the 'head' of each ship (the top-leftmost cell)
    to ensure each ship is counted exactly once without using extra space.

    Args:
        board: A 2D list of strings representing the board.

    Returns:
        The total number of battleships found.

    Examples:
        >>> solve([["X",".",".","X"],["X",".",".","X"],[".",".",".","."]])
        2
        >>> solve([["X","X","X","X"],["X",".",".","X"],["X",".",".","X"],["X","X","X","X"]])
        1
    """
    if not board or not board[0]:
        return 0

    rows = len(board)
    cols = len(board[0])
    ship_count = 0

    for r in range(rows):
        for c in range(cols):
            # Only process if we find a part of a ship
            if board[r][c] == "X":
                # Check if this 'X' is the start (head) of a ship.
                # A cell is a head if there is no 'X' directly above it 
                # and no 'X' directly to its left.
                is_top_edge = (r == 0 or board[r - 1][c] == ".")
                is_left_edge = (c == 0 or board[r][c - 1] == ".")

                if is_top_edge and is_left_edge:
                    ship_count += 1

    return ship_count
