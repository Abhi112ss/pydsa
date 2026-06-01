METADATA = {
    "id": 2373,
    "name": "Largest Local Values in a Matrix",
    "slug": "largest_local_values_in_a_matrix",
    "category": "array",
    "aliases": [],
    "tags": ["arrays", "matrix"],
    "difficulty": "easy",
    "time_complexity": "O(n^2)",
    "space_complexity": "O(n^2)",
    "description": "Return a matrix where each element is the maximum of the corresponding 3x3 submatrix of the input.",
}


def solve(matrix: list[list[int]]) -> list[list[int]]:
    """Compute the largest local values for each 3x3 submatrix.

    Args:
        matrix: A square 2D list of integers with dimensions n x n (n >= 3).

    Returns:
        A 2D list of integers with dimensions (n-2) x (n-2) where each element
        is the maximum value within the corresponding 3x3 window of the input.

    Examples:
        >>> solve([[9,9,8,1],[5,2,2,7],[9,6,3,8],[4,6,5,2]])
        [[9,9],[9,8]]
        >>> solve([[1,1,1],[1,1,1],[1,1,1]])
        [[1]]
    """
    n = len(matrix)
    result_size = n - 2
    # Initialize result matrix with zeros
    result: list[list[int]] = [[0] * result_size for _ in range(result_size)]

    for row_start in range(result_size):
        for col_start in range(result_size):
            # Compute maximum in the current 3x3 window
            window_max = matrix[row_start][col_start]
            for dr in range(3):
                for dc in range(3):
                    current_value = matrix[row_start + dr][col_start + dc]
                    if current_value > window_max:
                        window_max = current_value
            result[row_start][col_start] = window_max

    return result