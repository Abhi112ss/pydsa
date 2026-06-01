METADATA = {
    "id": 999,
    "name": "Available Captures for Rook",
    "slug": "available-captures-for-rook",
    "category": "Simulation",
    "aliases": [],
    "tags": ["matrix", "simulation"],
    "difficulty": "easy",
    "time_complexity": "O(1)",
    "space_complexity": "O(1)",
    "description": "Calculate the number of pawns a rook can capture in four cardinal directions on a chessboard.",
}

def solve(board: list[list[str]]) -> int:
    """
    Calculates the total number of pawns a rook can capture in four directions.

    The rook moves horizontally and vertically. It can capture exactly one 
    pawn in a direction before being blocked by an obstacle or the board edge.

    Args:
        board: A 8x8 grid representing the chessboard. 
               'R' is the rook, 'P' is a pawn, and '.' is an empty space.

    Returns:
        The total number of pawns the rook can capture.

    Examples:
        >>> board = [
        ...     ['.', '.', '.', '.', '.', '.', '.', '.'],
        ...     ['.', '.', '.', '.', '.', '.', '.', '.'],
        ...     ['.', '.', '.', 'R', '.', '.', '.', '.'],
        ...     ['.', '.', '.', 'P', '.', '.', '.', '.'],
        ...     ['.', '.', '.', '.', '.', '.', '.', '.'],
        ...     ['.', '.', '.', '.', '.', '.', '.', '.'],
        ...     ['.', '.', '.', '.', '.', '.', '.', '.'],
        ...     ['.', '.', '.', '.', '.', '.', '.', '.']
        ... ]
        >>> solve(board)
        1
    """
    rows = len(board)
    cols = len(board[0])
    rook_row = -1
    rook_col = -1

    # Find the position of the rook 'R'
    for r in range(rows):
        for c in range(cols):
            if board[r][c] == 'R':
                rook_row, rook_col = r, c
                break
        if rook_row != -1:
            break

    captures = 0
    # Directions: Up, Down, Left, Right
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for dr, dc in directions:
        curr_r, curr_c = rook_row + dr, rook_col + dc
        
        # Traverse in the current direction until we hit the edge
        while 0 <= curr_r < rows and 0 <= curr_c < cols:
            if board[curr_r][curr_c] == 'P':
                # Found a pawn, increment count and stop in this direction
                captures += 1
                break
            # If we hit an empty space, continue moving
            curr_r += dr
            curr_c += dc
            
    return captures
