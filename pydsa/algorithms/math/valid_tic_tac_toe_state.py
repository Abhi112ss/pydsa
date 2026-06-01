METADATA = {
    "id": 794,
    "name": "Valid Tic-Tac-Toe State",
    "slug": "valid-tic-tac-toe-state",
    "category": "Simulation",
    "aliases": [],
    "tags": ["matrix", "simulation"],
    "difficulty": "medium",
    "time_complexity": "O(1)",
    "space_complexity": "O(1)",
    "description": "Determine if a given 3x3 board state is a valid state in a Tic-Tac-Toe game.",
}

def solve(board: list[list[str]]) -> bool:
    """
    Determines if the given 3x3 Tic-Tac-Toe board represents a valid game state.

    A state is valid if:
    1. The number of 'X's and 'O's follows the turn order (X starts first).
    2. There is at most one winner.
    3. If 'X' wins, the number of 'X's must be exactly one more than 'O's.
    4. If 'O' wins, the number of 'X's must be equal to the number of 'O's.

    Args:
        board: A 3x3 list of lists containing 'X', 'O', or '.'.

    Returns:
        True if the state is valid, False otherwise.

    Examples:
        >>> solve([["X", "O", "X"], ["X", "O", "O"], ["O", "X", "X"]])
        True
        >>> solve([["X", "X", "X"], ["O", "O", "O"], ["X", "X", "X"]])
        False
    """
    x_count = 0
    o_count = 0

    # Count occurrences of X and O
    for row in board:
        for cell in row:
            if cell == "X":
                x_count += 1
            elif cell == "O":
                o_count += 1

    # Rule 1: X starts first, so x_count must be o_count or o_count + 1
    if not (x_count == o_count or x_count == o_count + 1):
        return False

    def check_winner(player: str) -> bool:
        """Helper to check if a specific player has won."""
        # Check rows and columns
        for i in range(3):
            if all(board[i][j] == player for j in range(3)):
                return True
            if all(board[j][i] == player for j in range(3)):
                return True
        
        # Check diagonals
        if all(board[i][i] == player for i in range(3)):
            return True
        if all(board[i][2 - i] == player for i in range(3)):
            return True
            
        return False

    x_wins = check_winner("X")
    o_wins = check_winner("O")

    # Rule 2: Both players cannot win simultaneously
    if x_wins and o_wins:
        return False

    # Rule 3: If X wins, X must have made one more move than O
    if x_wins and x_count != o_count + 1:
        return False

    # Rule 4: If O wins, X and O must have made the same number of moves
    if o_wins and x_count != o_count:
        return False

    return True
