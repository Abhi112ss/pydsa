METADATA = {
    "id": 2711,
    "name": "Difference of Number of Distinct Values on Diagonals",
    "slug": "difference_of_number_of_distinct_values_on_diagonals",
    "category": "array",
    "aliases": [],
    "tags": ["arrays", "hash_map"],
    "difficulty": "medium",
    "time_complexity": "O(m * n)",
    "space_complexity": "O(m * n)",
    "description": "Computes for each cell the absolute difference between distinct values on its top‑left and bottom‑right diagonals.",
}


def solve(grid: list[list[int]]) -> list[list[int]]:
    """Return a matrix where each element is the absolute difference between the
    number of distinct values on its top‑left diagonal and its bottom‑right
    diagonal.

    Args:
        grid: A 2‑dimensional list of integers representing the input matrix.

    Returns:
        A 2‑dimensional list of integers where result[i][j] is
        |distinct_top_left(i, j) – distinct_bottom_right(i, j)|.

    Examples:
        >>> solve([[1,2,3],[3,1,5],[3,2,1]])
        [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
        >>> solve([[1,2],[3,4]])
        [[0, 0], [0, 0]]
    """
    row_count = len(grid)
    col_count = len(grid[0]) if row_count else 0

    # Matrices to store distinct counts for the two diagonal directions.
    top_left_counts: list[list[int]] = [[0] * col_count for _ in range(row_count)]
    bottom_right_counts: list[list[int]] = [[0] * col_count for _ in range(row_count)]

    # Forward pass: compute distinct values on the top‑left diagonal for each cell.
    diagonal_sets: dict[int, set[int]] = {}
    for i in range(row_count):
        for j in range(col_count):
            diagonal_key = i - j
            if diagonal_key not in diagonal_sets:
                diagonal_sets[diagonal_key] = set()
            diagonal_sets[diagonal_key].add(grid[i][j])
            top_left_counts[i][j] = len(diagonal_sets[diagonal_key])

    # Backward pass: compute distinct values on the bottom‑right diagonal for each cell.
    diagonal_sets_rev: dict[int, set[int]] = {}
    for i in range(row_count - 1, -1, -1):
        for j in range(col_count - 1, -1, -1):
            diagonal_key = i - j
            if diagonal_key not in diagonal_sets_rev:
                diagonal_sets_rev[diagonal_key] = set()
            diagonal_sets_rev[diagonal_key].add(grid[i][j])
            bottom_right_counts[i][j] = len(diagonal_sets_rev[diagonal_key])

    # Combine the two counts to produce the final answer.
    result: list[list[int]] = [[0] * col_count for _ in range(row_count)]
    for i in range(row_count):
        for j in range(col_count):
            result[i][j] = abs(top_left_counts[i][j] - bottom_right_counts[i][j])

    return result