METADATA = {
    "id": 79,
    "name": "Word Search",
    "slug": "word-search",
    "category": "Backtracking",
    "aliases": [],
    "tags": ["backtracking", "matrix", "dfs"],
    "difficulty": "medium",
    "time_complexity": "O(M * N * 4^L)",
    "space_complexity": "O(L)",
    "description": "Determine if a given word exists in a 2D grid of characters by following adjacent cells.",
}

def solve(board: list[list[str]], word: str) -> bool:
    """
    Determines if the target word can be constructed from letters of sequentially 
    adjacent cells in the grid.

    Args:
        board: A 2D list of characters representing the grid.
        word: The target string to search for.

    Returns:
        True if the word exists in the grid, False otherwise.

    Examples:
        >>> solve([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED")
        True
        >>> solve([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "SEE")
        True
        >>> solve([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCB")
        False
    """
    if not board or not board[0]:
        return False

    rows_count = len(board)
    cols_count = len(board[0])
    word_length = len(word)

    def backtrack(row_idx: int, col_idx: int, word_idx: int) -> bool:
        # Base case: all characters in the word have been matched
        if word_idx == word_length:
            return True

        # Boundary checks and character mismatch check
        if (
            row_idx < 0
            or row_idx >= rows_count
            or col_idx < 0
            or col_idx >= cols_count
            or board[row_idx][col_idx] != word[word_idx]
        ):
            return False

        # Mark the current cell as visited by temporarily changing its value
        temp_char = board[row_idx][col_idx]
        board[row_idx][col_idx] = "#"

        # Explore all 4 possible directions: up, down, left, right
        found = (
            backtrack(row_idx + 1, col_idx, word_idx + 1)
            or backtrack(row_idx - 1, col_idx, word_idx + 1)
            or backtrack(row_idx, col_idx + 1, word_idx + 1)
            or backtrack(row_idx, col_idx - 1, word_idx + 1)
        )

        # Backtrack: restore the original character for other potential paths
        board[row_idx][col_idx] = temp_char
        
        return found

    # Iterate through every cell in the grid to find a starting point
    for r in range(rows_count):
        for c in range(cols_count):
            # Optimization: only start DFS if the first character matches
            if board[r][c] == word[0]:
                if backtrack(r, c, 0):
                    return True

    return False