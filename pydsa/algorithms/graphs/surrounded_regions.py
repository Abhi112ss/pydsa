METADATA = {
    "id": 130,
    "name": "Surrounded Regions",
    "slug": "surrounded-regions",
    "category": "Matrix",
    "aliases": [],
    "tags": ["dfs", "bfs", "matrix"],
    "difficulty": "medium",
    "time_complexity": "O(m*n)",
    "space_complexity": "O(m*n)",
    "description": "Capture all regions that are completely surrounded by 'X' by flipping 'O's to 'X's, unless they are connected to the border.",
}

def solve(board: list[list[str]]) -> None:
    """
    Modifies the board in-place to capture all surrounded regions.

    A region is captured by flipping all 'O's into 'X's in that surrounded region.
    An 'O' is not surrounded if it is on the border or connected to an 'O' on the border.

    Args:
        board: A list of lists of strings representing the grid.

    Returns:
        None. The board is modified in-place.

    Examples:
        >>> board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
        >>> solve(board)
        >>> board
        [['X', 'X', 'X', 'X'], ['X', 'X', 'X', 'X'], ['X', 'X', 'X', 'X'], ['X', 'O', 'X', 'X']]
    """
    if not board or not board[0]:
        return

    rows = len(board)
    cols = len(board[0])

    def mark_border_connected(r: int, c: int) -> None:
        """Performs DFS to mark border-connected 'O's with a temporary placeholder."""
        stack = [(r, c)]
        board[r][c] = "T"  # Use 'T' as a temporary marker for 'safe' O's
        
        while stack:
            curr_r, curr_c = stack.pop()
            # Check all 4 neighbors
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = curr_r + dr, curr_c + dc
                if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] == "O":
                    board[nr][nc] = "T"
                    stack.append((nr, nc))

    # Step 1: Traverse the borders to find all 'O's connected to the edge.
    # These 'O's and their connected neighbors cannot be surrounded.
    for r in range(rows):
        for c in [0, cols - 1]:  # First and last column
            if board[r][c] == "O":
                mark_border_connected(r, c)
                
    for c in range(cols):
        for r in [0, rows - 1]:  # First and last row
            if board[r][c] == "O":
                mark_border_connected(r, c)

    # Step 2: Iterate through the entire board.
    # If an 'O' remains, it was not connected to a border, so flip it to 'X'.
    # If it is 'T', it was connected to a border, so flip it back to 'O'.
    for r in range(rows):
        for c in range(cols):
            if board[r][c] == "O":
                board[r][c] = "X"
            elif board[r][c] == "T":
                board[r][c] = "O"
