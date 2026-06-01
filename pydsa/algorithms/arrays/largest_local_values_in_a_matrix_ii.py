METADATA = {
    "id": 3933,
    "name": "Largest Local Values in a Matrix II",
    "slug": "largest_local_values_in_a_matrix_ii",
    "category": "Arrays",
    "aliases": [],
    "tags": ["arrays", "sliding_window", "matrix"],
    "difficulty": "medium",
    "time_complexity": "O(rows * cols)",
    "space_complexity": "O(rows * cols)",
    "description": "Find the maximum value in every 3x3 subgrid of a given matrix.",
}

def solve(grid: list[list[int]]) -> list[list[int]]:
    """
    Computes the maximum value in every 3x3 subgrid of the input matrix.

    Args:
        grid: A 2D list of integers representing the input matrix.

    Returns:
        A 2D list of integers where each element (i, j) is the maximum 
        value in the 3x3 subgrid starting at (i, j).

    Examples:
        >>> grid = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
        >>> solve(grid)
        [[11, 12], [15, 16]]
    """
    rows = len(grid)
    cols = len(grid[0])
    
    # The output dimensions will be (rows - 2) x (cols - 2)
    res_rows = rows - 2
    res_cols = cols - 2
    result = [[0] * res_cols for _ in range(res_rows)]

    # We iterate through each possible top-left corner of a 3x3 subgrid
    for i in range(res_rows):
        for j in range(res_cols):
            # Find the maximum in the 3x3 window starting at (i, j)
            current_max = -float('inf')
            
            # Check all 9 elements in the 3x3 block
            for r in range(i, i + 3):
                for c in range(j, j + 3):
                    if grid[r][c] > current_max:
                        current_max = grid[r][c]
            
            result[i][j] = int(current_max)

    return result

# Note: While a 2D monotonic queue/sliding window maximum approach 
# provides O(N*M) complexity, for a fixed small window size like 3x3, 
# the constant factor of the nested loop approach is extremely low 
# and effectively performs in O(N*M) time.
