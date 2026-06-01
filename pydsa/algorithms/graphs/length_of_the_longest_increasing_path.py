METADATA = {
    "id": 3288,
    "name": "Length of the Longest Increasing Path in a Matrix",
    "slug": "length-of-the-longest-increasing-path-in-a-matrix",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dfs", "memoization", "dp", "matrix"],
    "difficulty": "hard",
    "time_complexity": "O(m * n)",
    "space_complexity": "O(m * n)",
    "description": "Find the length of the longest increasing path in an m x n integer matrix.",
}

def solve(matrix: list[list[int]]) -> int:
    """
    Calculates the length of the longest increasing path in a given matrix.

    Args:
        matrix: A 2D list of integers representing the grid.

    Returns:
        The length of the longest increasing path.

    Examples:
        >>> solve([[9,9,4],[6,6,8],[2,1,1]])
        4
        >>> solve([[3,4,5],[3,2,6],[2,7,8]])
        5
    """
    if not matrix or not matrix[0]:
        return 0

    rows_count = len(matrix)
    cols_count = len(matrix[0])
    
    # memo[r][c] stores the length of the longest increasing path starting from (r, c)
    memo: list[list[int]] = [[0] * cols_count for _ in range(rows_count)]

    def get_longest_path_from(row: int, col: int) -> int:
        # If we have already computed the result for this cell, return it
        if memo[row][col] != 0:
            return memo[row][col]

        max_length = 1
        # Explore all 4 possible directions: up, down, left, right
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_row, new_col = row + dr, col + dc

            # Check boundaries and ensure the next cell value is strictly greater
            if (0 <= new_row < rows_count and 
                0 <= new_col < cols_count and 
                matrix[new_row][new_col] > matrix[row][col]):
                
                # The path length from current cell is 1 + path length from the next cell
                path_len = 1 + get_longest_path_from(new_row, new_col)
                max_length = max(max_length, path_len)

        # Store the result in memo before returning
        memo[row][col] = max_length
        return max_length

    overall_max_path = 0
    # Iterate through every cell in the matrix to find the global maximum
    for r in range(rows_count):
        for c in range(cols_count):
            overall_max_path = max(overall_max_path, get_longest_path_from(r, c))

    return overall_max_path
