METADATA = {
    "id": 3033,
    "name": "Modify the Matrix",
    "slug": "modify_the_matrix",
    "category": "Matrix",
    "aliases": [],
    "tags": ["matrix", "implementation"],
    "difficulty": "easy",
    "time_complexity": "O(m * n)",
    "space_complexity": "O(1)",
    "description": "Modify the elements of a matrix based on their row and column indices parity.",
}

def solve(grid: list[list[int]]) -> list[list[int]]:
    """
    Modifies the elements of a 2D grid based on the parity of row and column indices.
    
    The transformation rules are:
    - If row index is even and column index is even: grid[i][j] = grid[i][j] + 1
    - If row index is even and column index is odd: grid[i][j] = grid[i][j] - 1
    - If row index is odd and column index is even: grid[i][j] = grid[i][j] - 1
    - If row index is odd and column index is odd: grid[i][j] = grid[i][j] + 1

    Args:
        grid: A 2D list of integers representing the matrix.

    Returns:
        The modified 2D list of integers.

    Examples:
        >>> solve([[1, 1], [1, 1]])
        [[2, 0], [0, 2]]
        >>> solve([[1, 2, 3], [4, 5, 6]])
        [[2, 1, 4], [3, 6, 5]]
    """
    rows = len(grid)
    cols = len(grid[0])

    for r in range(rows):
        for c in range(cols):
            # Determine parity: (r % 2 == c % 2) is True if both are even or both are odd
            # This covers (even, even) and (odd, odd) cases
            if (r % 2) == (c % 2):
                grid[r][c] += 1
            else:
                # This covers (even, odd) and (odd, even) cases
                grid[r][c] -= 1
                
    return grid
