METADATA = {
    "id": 2536,
    "name": "Increment Submatrices by One",
    "slug": "increment_submatrices_by_one",
    "category": "Arrays",
    "aliases": [],
    "tags": ["arrays", "2d_prefix_sum", "matrix"],
    "difficulty": "medium",
    "time_complexity": "O(m * n)",
    "space_complexity": "O(m * n)",
    "description": "Apply multiple submatrix increments using a 2D difference array and return the final matrix.",
}

def solve(grid: list[list[int]], queries: list[list[int]]) -> list[list[int]]:
    """
    Increments submatrices defined by queries by one using a 2D difference array.

    Args:
        grid: A 2D list of integers representing the initial matrix.
        queries: A list of queries where each query is [r1, c1, r2, c2] 
                 representing the top-left and bottom-right corners.

    Returns:
        The modified grid after all increments have been applied.

    Examples:
        >>> grid = [[0,0],[0,0]]
        >>> queries = [[0,0,1,1],[0,1,1,1]]
        >>> solve(grid, queries)
        [[1, 2], [1, 2]]
    """
    rows = len(grid)
    cols = len(grid[0])
    
    # Initialize a 2D difference array with an extra row and column 
    # to handle boundary conditions without complex if-statements.
    diff = [[0] * (cols + 1) for _ in range(rows + 1)]

    for r1, c1, r2, c2 in queries:
        # Apply the 2D difference array update logic:
        # Increment the top-left corner
        diff[r1][c1] += 1
        # Decrement the boundaries to restrict the increment to the submatrix
        if r2 + 1 < rows:
            diff[r2 + 1][c1] -= 1
        if c2 + 1 < cols:
            diff[r1][c2 + 1] -= 1
        if r2 + 1 < rows and c2 + 1 < cols:
            diff[r2 + 1][c2 + 1] += 1

    # Compute the 2D prefix sum to reconstruct the increment values
    # and add them to the original grid.
    for r in range(rows):
        for c in range(cols):
            # Standard 2D prefix sum formula: 
            # current = diff[r][c] + top + left - top_left_diagonal
            top = diff[r - 1][c] if r > 0 else 0
            left = diff[r][c - 1] if c > 0 else 0
            top_left = diff[r - 1][c - 1] if (r > 0 and c > 0) else 0
            
            # We update the diff array in-place to act as the prefix sum array
            diff[r][c] += top + left - top_left
            
            # Add the calculated increment to the original grid value
            grid[r][c] += diff[r][c]

    return grid
