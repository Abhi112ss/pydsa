METADATA = {
    "id": 37,
    "name": "Sudoku Solver",
    "slug": "sudoku-solver",
    "category": "Backtracking",
    "aliases": [],
    "tags": ["backtracking", "matrix"],
    "difficulty": "hard",
    "time_complexity": "O(9^m) where m is the number of empty cells",
    "space_complexity": "O(1) as the board size is fixed at 9x9",
    "description": "Solve a 9x9 Sudoku puzzle by filling empty cells with digits 1-9 such that each row, column, and 3x3 subgrid contains all digits from 1 to 9.",
}

def solve(board: list[list[str]]) -> None:
    """
    Solves a 9x9 Sudoku board in-place using backtracking.

    Args:
        board: A 9x9 list of lists of strings representing the Sudoku board.
               Empty cells are denoted by '.'.

    Returns:
        None. The board is modified in-place.

    Examples:
        >>> board = [
        ...     ["5","3",".",".","7",".",".",".","."],
        ...     ["6",".",".","1","9","5",".",".","."],
        ...     [".","9","8",".",".",".",".","6","."],
        ...     ["8",".",".",".","6",".",".",".","3"],
        ...     ["4",".",".","8",".","3",".",".","1"],
        ...     ["7",".",".",".","2",".",".",".","6"],
        ...     [".","6",".",".",".",".","2","8","."],
        ...     [".",".",".","4","1","9",".",".","5"],
        ...     [".",".",".",".","8",".",".","7","9"]
        ... ]
        >>> solve(board)
        >>> board[0][2]
        '4'
    """

    def is_valid(row: int, col: int, char: str) -> bool:
        """Checks if placing char at board[row][col] is valid."""
        for i in range(9):
            # Check row constraint
            if board[row][i] == char:
                return False
            # Check column constraint
            if board[i][col] == char:
                return False
            # Check 3x3 subgrid constraint
            # (row // 3 * 3) finds the top row of the subgrid
            # (col // 3 * 3) finds the left col of the subgrid
            subgrid_row = 3 * (row // 3) + i // 3
            subgrid_col = 3 * (col // 3) + i % 3
            if board[subgrid_row][subgrid_col] == char:
                return False
        return True

    def backtrack() -> bool:
        """Core backtracking function to explore possibilities."""
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    # Try every possible digit from '1' to '9'
                    for digit in "123456789":
                        if is_valid(r, c, digit):
                            board[r][c] = digit
                            
                            # Recursively attempt to solve the rest of the board
                            if backtrack():
                                return True
                            
                            # If placing digit doesn't lead to a solution, backtrack
                            board[r][c] = "."
                    
                    # If no digit 1-9 works in this cell, trigger backtracking
                    return False
        # If no empty cells are left, the puzzle is solved
        return True

    backtrack()