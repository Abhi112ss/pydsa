METADATA = {
    "id": 1337,
    "name": "The K Weakest Rows in a Matrix",
    "slug": "the_k_weakest_rows_in_a_matrix",
    "category": "Array",
    "aliases": [],
    "tags": ["binary_search", "sorting", "heap"],
    "difficulty": "easy",
    "time_complexity": "O(m * (log n + log m))",
    "space_complexity": "O(m)",
    "description": "Return the indices of the k weakest rows in a binary matrix.",
}


def solve(matrix: list[list[int]], k: int) -> list[int]:
    """Find the indices of the k weakest rows in a binary matrix.

    Each row of *matrix* consists of 1's (soldiers) followed by 0's (civilians).
    A row is weaker if it has fewer soldiers; ties are broken by the row index.

    Args:
        matrix: A list of rows, each row is a list of integers 0 or 1.
        k: The number of weakest rows to return.

    Returns:
        A list of length *k* containing the indices of the weakest rows ordered
        from weakest to strongest.

    Examples:
        >>> solve([[1,1,0,0],[1,0,0,0],[1,1,1,1],[1,1,0,0]], 2)
        [1, 0]
        >>> solve([[1,0,0],[1,1,1],[1,0,0],[1,0,0]], 3)
        [0, 2, 3]
    """
    def count_soldiers(row: list[int]) -> int:
        """Return the number of leading 1's in *row* using binary search."""
        left, right = 0, len(row)
        while left < right:
            mid = (left + right) // 2
            if row[mid] == 1:
                left = mid + 1
            else:
                right = mid
        return left

    # Compute (soldier_count, row_index) for each row.
    row_strengths: list[tuple[int, int]] = []
    for row_index, row in enumerate(matrix):
        soldier_count = count_soldiers(row)
        row_strengths.append((soldier_count, row_index))

    # Sort by soldier count then by row index.
    row_strengths.sort(key=lambda pair: (pair[0], pair[1]))

    # Extract the first k row indices.
    weakest_indices: list[int] = [pair[1] for pair in row_strengths[:k]]
    return weakest_indices