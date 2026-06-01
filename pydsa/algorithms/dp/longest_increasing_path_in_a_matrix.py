METADATA = {
    "id": 329,
    "name": "Longest Increasing Path in a Matrix",
    "slug": "longest_increasing_path_in_a_matrix",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["depth_first_search", "memoization", "topological_sort", "matrix"],
    "difficulty": "hard",
    "time_complexity": "O(m * n)",
    "space_complexity": "O(m * n)",
    "description": "Find the length of the longest increasing path in a given m x n integer matrix.",
}

def solve(matrix: list[list[int]]) -> int:
    """
    Finds the length of the longest increasing path in a matrix using DFS and memoization.

    Args:
        matrix: A 2D list of integers representing the grid.

    Returns:
        The length of the longest increasing path.

    Examples:
        >>> solve([[9,9,9],[9,1,9],[9,9,9]])
        1
        >>> solve([[3,4,5],[3,2,6],[2,2,2]])
        4
    """
    if not matrix or not matrix[0]:
        return 0

    rows_count = len(matrix)
    cols_count = len(matrix[0])
    
    # memo[r][c] stores the longest increasing path starting from cell (r, c)
    memo: list[list[int]] = [[0] * cols_count for _ in range(rows_count)]

    def get_longest_path_from(row: int, col: int) -> int:
        # If already computed, return the cached value
        if memo[row][col] != 0:
            return memo[row][col]

        max_path = 1
        # Explore 4 possible directions: up, down, left, right
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            next_row, next_col = row + dr, col + dc

            # Check boundaries and ensure the next cell value is strictly greater
            if (0 <= next_row < rows_count and 
                0 <= next_col < cols_count and 
                matrix[next_row][next_col] > matrix[row][col]):
                
                # The path from current cell is 1 + path from the next cell
                path_length = 1 + get_longest_path_from(next_row, next_col)
                max_path = max(max_path, path_length)

        # Cache the result before returning
        memo[row][col] = max_path
        return max_path

    longest_overall_path = 0
    # Iterate through every cell in the matrix to find the global maximum
    for r in range(rows_count):
        for c in range(cols_count):
            longest_overall_path = max(longest_overall_path, get_longest_path_from(r, c))

    return longest_overall_path
