METADATA = {
    "id": 1275,
    "name": "Find Winner on a Tic Tac Toe Game",
    "slug": "find-winner-on-a-tic-tac-toe-game",
    "category": "Simulation",
    "aliases": [],
    "tags": ["matrix", "simulation"],
    "difficulty": "medium",
    "time_complexity": "O(1)",
    "space_complexity": "O(1)",
    "description": "Determine the winner of a 3x3 Tic Tac Toe game based on a sequence of moves.",
}

def solve(moves: list[list[int]]) -> str:
    """
    Determines the winner of a 3x3 Tic Tac Toe game.

    Args:
        moves: A list of moves where moves[i] = [row_i, col_i] represents the 
               position of the i-th move. Even indices are Player A, odd are Player B.

    Returns:
        "A" if Player A wins, "B" if Player B wins, "Draw" if no one wins, 
        or "Pending" if the game is not finished.

    Examples:
        >>> solve([[0, 0], [1, 1], [2, 2]])
        'A'
        >>> solve([[0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2]])
        'A'
        >>> solve([[0, 0], [0, 1], [0, 2]])
        'A'
    """
    # Since the board is fixed at 3x3, we use arrays to track counts.
    # rows[i] tracks how many marks player A or B has in row i.
    # We use positive values for Player A and negative for Player B.
    rows = [0] * 3
    cols = [0] * 3
    diag = 0
    anti_diag = 0
    
    for i, (r, c) in enumerate(moves):
        # Determine player: Player A (0, 2, 4...) gets +1, Player B (1, 3, 5...) gets -1
        player_val = 1 if i % 2 == 0 else -1
        player_id = "A" if i % 2 == 0 else "B"

        # Update row and column counts
        rows[r] += player_val
        cols[c] += player_val

        # Update main diagonal (top-left to bottom-right)
        if r == c:
            diag += player_val
        
        # Update anti-diagonal (top-right to bottom-left)
        if r + c == 2:
            anti_diag += player_val

        # Check if the current move resulted in a win
        # A win occurs if any count reaches 3 (for A) or -3 (for B)
        if abs(rows[r]) == 3 or abs(cols[c]) == 3 or abs(diag) == 3 or abs(anti_diag) == 3:
            return player_id

    # If no winner is found, check if the board is full
    if len(moves) == 9:
        return "Draw"
    
    return "Pending"
