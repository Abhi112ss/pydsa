METADATA = {
    "id": 723,
    "name": "Candy Crush",
    "slug": "candy-crush",
    "category": "Simulation",
    "aliases": [],
    "tags": ["simulation", "two_pointer", "matrix"],
    "difficulty": "medium",
    "time_complexity": "O((R*C)^2)",
    "space_complexity": "O(1)",
    "description": "Simulate the candy crush game where matching candies in rows or columns are removed and gravity pulls remaining candies down.",
}

def solve(board: list[list[int]]) -> list[list[int]]:
    """
    Simulates the Candy Crush game logic on a 2D grid.

    Args:
        board: A 2D list of integers representing the candy grid.

    Returns:
        The modified board after all possible crushing and gravity steps are completed.

    Examples:
        >>> board = [[1, 1, 1, 2], [3, 4, 5, 6], [1, 1, 1, 2]]
        >>> solve(board)
        [[0, 0, 0, 0], [0, 4, 5, 6], [0, 0, 0, 0]]
    """
    if not board or not board[0]:
        return board

    rows = len(board)
    cols = len(board[0])

    while True:
        to_crush = set()

        # 1. Identify horizontal matches (3 or more in a row)
        for r in range(rows):
            for c in range(cols - 2):
                if board[r][c] != 0 and board[r][c] == board[r][c + 1] == board[r][c + 2]:
                    to_crush.add((r, c))
                    to_crush.add((r, c + 1))
                    to_crush.add((r, c + 2))

        # 2. Identify vertical matches (3 or more in a column)
        for r in range(rows - 2):
            for c in range(cols):
                if board[r][c] != 0 and board[r][c] == board[r + 1][c] == board[r + 2][c]:
                    to_crush.add((r, c))
                    to_crush.add((r + 1, c))
                    to_crush.add((r + 2, c))

        # If no candies were marked for crushing, the board is stable
        if not to_crush:
            break

        # 3. Mark candies for removal by setting them to 0
        for r, c in to_crush:
            board[r][c] = 0

        # 4. Apply gravity: Shift non-zero elements down for each column
        for c in range(cols):
            write_idx = rows - 1
            # Iterate from bottom to top to move elements down
            for r in range(rows - 1, -1, -1):
                if board[r][c] != 0:
                    board[write_idx][c] = board[r][c]
                    if write_idx != r:
                        board[r][c] = 0
                    write_idx -= 1
            
            # Fill the remaining top cells with 0
            for r in range(write_idx, -1, -1):
                board[r][c] = 0

    return board
