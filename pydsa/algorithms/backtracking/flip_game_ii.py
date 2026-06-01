METADATA = {
    "id": 294,
    "name": "Flip Game II",
    "slug": "flip-game-ii",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["backtracking", "game_theory", "memoization"],
    "difficulty": "medium",
    "time_complexity": "O(2^n)",
    "space_complexity": "O(n)",
    "description": "Determine if the first player can win a game by flipping a 2x2 subgrid of 0s in a 2D grid.",
}

def solve(board: list[list[int]]) -> bool:
    """
    Determines if the current player can win the game starting from the given board state.
    
    The game involves flipping a 2x2 subgrid of 0s. A player wins if they can 
    make a move that results in the opponent being in a losing position.

    Args:
        board: A 2D list of integers representing the game board.

    Returns:
        True if the current player can win, False otherwise.

    Examples:
        >>> solve([[0,0,0],[0,0,0],[0,0,0]])
        True
        >>> solve([[1,1,1],[1,1,1],[1,1,1]])
        False
    """
    memo: dict[tuple[tuple[int, ...], tuple[int, ...]], bool] = {}
    rows = len(board)
    cols = len(board[0])

    def get_state() -> tuple[tuple[int, ...], tuple[int, ...]]:
        """Converts the 2D list into a hashable tuple format for memoization."""
        return (tuple(board[0]), tuple(board[1]), tuple(board[2])) if rows == 3 else (tuple(board[0]), tuple(board[1]))

    def can_win() -> bool:
        state = get_state()
        if state in memo:
            return memo[state]

        # Iterate through every possible top-left corner of a 2x2 subgrid
        for r in range(rows - 1):
            for c in range(cols - 1):
                # Check if the 2x2 subgrid consists entirely of 0s
                if (board[r][c] == 0 and board[r][c+1] == 0 and 
                    board[r+1][c] == 0 and board[r+1][c+1] == 0):
                    
                    # Perform the flip (change 0s to 1s)
                    board[r][c] = board[r][c+1] = board[r+1][c] = board[r+1][c+1] = 1
                    
                    # If the opponent cannot win from this new state, the current player wins
                    opponent_can_win = can_win()
                    
                    # Backtrack: restore the board state for other recursive branches
                    board[r][c] = board[r][c+1] = board[r+1][c] = board[r+1][c+1] = 0
                    
                    if not opponent_can_win:
                        memo[state] = True
                        return True
        
        # If no move leads to an opponent's loss, the current player loses
        memo[state] = False
        return False

    return can_win()
