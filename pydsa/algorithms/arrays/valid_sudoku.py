METADATA = {
    "id": 36,
    "name": "Valid Sudoku",
    "slug": "valid-sudoku",
    "category": "Matrix",
    "aliases": [],
    "tags": ["hash_set", "matrix"],
    "difficulty": "medium",
    "time_complexity": "O(1)",
    "space_complexity": "O(1)",
    "description": "Determine if a 9x9 Sudoku board is valid based on the rules of rows, columns, and 3x3 sub-boxes.",
}

def solve(board: list[list[str]]) -> bool:
    """
    Determines if a 9x9 Sudoku board is valid.

    A valid Sudoku board must satisfy three conditions:
    1. Each row must contain the digits 1-9 without repetition.
    2. Each column must contain the digits 1-9 without repetition.
    3. Each of the nine 3x3 sub-boxes must contain the digits 1-9 without repetition.

    Args:
        board: A 9x9 list of lists of strings representing the Sudoku board.
               Empty cells are represented by '.'.

    Returns:
        True if the board is valid, False otherwise.

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
        True
    """
    # We use sets to track seen numbers for each row, column, and 3x3 box.
    # Since the board size is fixed at 9x9, the space complexity is O(1).
    rows = [set() for _ in range(9)]
    cols = [set() for _ in range(9)]
    boxes = [set() for _ in range(9)]

    for r in range(9):
        for c in range(9):
            val = board[r][c]

            if val == ".":
                continue

            # Calculate the index for the 3x3 sub-box.
            # Dividing row and col by 3 maps the 9x9 grid into 9 boxes (0-8).
            box_index = (r // 3) * 3 + (c // 3)

            # Check if the value has already been encountered in the current row, col, or box.
            if (val in rows[r] or 
                val in cols[c] or 
                val in boxes[box_index]):
                return False

            # Add the value to the respective sets to mark it as seen.
            rows[r].add(val)
            cols[c].add(val)
            boxes[box_index].add(val)

    return True
