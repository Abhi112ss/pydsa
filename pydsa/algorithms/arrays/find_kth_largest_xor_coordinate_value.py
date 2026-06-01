METADATA = {
    "id": 1738,
    "name": "Find Kth Largest XOR Coordinate Value",
    "slug": "find_kth_largest_xor_coordinate_value",
    "category": "algorithms",
    "aliases": [],
    "tags": ["bit_manipulation", "prefix_sum", "heaps"],
    "difficulty": "medium",
    "time_complexity": "O(m * n log(m * n))",
    "space_complexity": "O(m * n)",
    "description": "Return the k-th largest XOR coordinate value from all submatrices of a given matrix.",
}


def solve(matrix: list[list[int]], k: int) -> int:
    """Compute the k-th largest XOR coordinate value.

    Args:
        matrix: A 2D list of non‑negative integers representing the input matrix.
        k: The 1‑based rank of the largest value to retrieve.

    Returns:
        The k-th largest XOR coordinate value among all possible submatrices
        that start at the origin (0, 0) and end at (i, j).

    Examples:
        >>> solve([[5,2],[1,6]], 1)
        7
        >>> solve([[5,2],[1,6]], 3)
        4
    """
    row_count: int = len(matrix)
    column_count: int = len(matrix[0]) if row_count > 0 else 0

    # dp[i][j] stores XOR of submatrix (0,0) to (i,j)
    dp: list[list[int]] = [[0] * column_count for _ in range(row_count)]
    xor_values: list[int] = []

    for i in range(row_count):
        for j in range(column_count):
            top: int = dp[i - 1][j] if i > 0 else 0
            left: int = dp[i][j - 1] if j > 0 else 0
            top_left: int = dp[i - 1][j - 1] if i > 0 and j > 0 else 0
            dp[i][j] = matrix[i][j] ^ top ^ left ^ top_left
            xor_values.append(dp[i][j])

    # Sort descending and pick the k‑th element (1‑based)
    xor_values.sort(reverse=True)
    return xor_values[k - 1]