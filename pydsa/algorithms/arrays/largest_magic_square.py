METADATA = {
    "id": 1895,
    "name": "Largest Magic Square",
    "slug": "largest_magic_square",
    "category": "Matrix",
    "aliases": [],
    "tags": ["matrix", "brute_force"],
    "difficulty": "medium",
    "time_complexity": "O(n^3)",
    "space_complexity": "O(1)",
    "description": "Find the size of the largest magic square within a given matrix.",
}

def solve(matrix: list[list[int]]) -> int:
    """
    Finds the size of the largest magic square in a given matrix.
    
    A magic square is a square matrix where the sum of every row, 
    every column, and both main diagonals are equal.

    Args:
        matrix: A 2D list of integers representing the grid.

    Returns:
        The size (side length) of the largest magic square found.

    Examples:
        >>> solve([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        1
        >>> solve([[1, 1, 1], [1, 1, 1], [1, 1, 1]])
        3
    """
    rows = len(matrix)
    cols = len(matrix[0])

    def is_magic(start_row: int, start_col: int, size: int) -> bool:
        """Checks if a square of a given size starting at (start_row, start_col) is magic."""
        # Calculate the target sum using the first row
        target_sum = sum(matrix[start_row][start_col : start_col + size])

        # Check all rows
        for r in range(start_row + 1, start_row + size):
            if sum(matrix[r][start_col : start_col + size]) != target_sum:
                return False

        # Check all columns
        for c in range(start_col, start_col + size):
            col_sum = 0
            for r in range(start_row, start_row + size):
                col_sum += matrix[r][c]
            if col_sum != target_sum:
                return False

        # Check main diagonal (top-left to bottom-right)
        diag1_sum = 0
        for i in range(size):
            diag1_sum += matrix[start_row + i][start_col + i]
        if diag1_sum != target_sum:
            return False

        # Check anti-diagonal (top-right to bottom-left)
        diag2_sum = 0
        for i in range(size):
            diag2_sum += matrix[start_row + i][start_col + size - 1 - i]
        if diag2_sum != target_sum:
            return False

        return True

    # Iterate through possible sizes from largest possible down to 1
    # This allows us to return immediately once the largest is found
    max_possible_size = min(rows, cols)
    
    for size in range(max_possible_size, 1, -1):
        # Iterate through all possible top-left corners for the current size
        for r in range(rows - size + 1):
            for c in range(cols - size + 1):
                if is_magic(r, c, size):
                    return size

    # If no magic square of size > 1 is found, the largest is size 1
    return 1
