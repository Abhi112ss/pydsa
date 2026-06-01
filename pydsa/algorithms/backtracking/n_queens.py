METADATA = {
    "id": 51,
    "name": "N-Queens",
    "slug": "n-queens",
    "category": "Backtracking",
    "aliases": [],
    "tags": ["backtracking", "recursion", "matrix"],
    "difficulty": "hard",
    "time_complexity": "O(N!)",
    "space_complexity": "O(N^2)",
    "description": "Find all distinct solutions to the n-queens puzzle.",
}

def solve(n: int) -> list[list[str]]:
    """
    Finds all distinct solutions to the n-queens puzzle.

    Args:
        n: The number of queens to place on an n x n chessboard.

    Returns:
        A list of all distinct board configurations, where each configuration 
        is represented by a list of strings.

    Examples:
        >>> solve(4)
        [['.Q..', '...Q', 'Q...', '..Q.'], ['..Q.', 'Q...', '...Q', '.Q..']]
    """
    results: list[list[str]] = []
    # The board is represented as a list of lists of characters for mutability
    board: list[list[str]] = [["." for _ in range(n)] for _ in range(n)]

    # Sets to track occupied paths in O(1) time
    cols = set()
    pos_diag = set()  # (row + col) is constant for positive diagonals (/)
    neg_diag = set()  # (row - col) is constant for negative diagonals (\)

    def backtrack(row: int) -> None:
        # Base case: If all rows are filled, we found a valid configuration
        if row == n:
            results.append(["".join(r) for r in board])
            return

        for col in range(n):
            # Check if the current position is under attack
            if col in cols or (row + col) in pos_diag or (row - col) in neg_diag:
                continue

            # Place the queen and update the tracking sets
            board[row][col] = "Q"
            cols.add(col)
            pos_diag.add(row + col)
            neg_diag.add(row - col)

            # Move to the next row
            backtrack(row + 1)

            # Backtrack: Remove the queen and restore the tracking sets
            board[row][col] = "."
            cols.remove(col)
            pos_diag.remove(row + col)
            neg_diag.remove(row - col)

    backtrack(0)
    return results
