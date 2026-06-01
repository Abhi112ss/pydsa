METADATA = {
    "id": 119,
    "name": "Pascal's Triangle II",
    "slug": "pascals-triangle-ii",
    "category": "Array",
    "aliases": [],
    "tags": ["arrays", "dynamic_programming"],
    "difficulty": "easy",
    "time_complexity": "O(n^2)",
    "space_complexity": "O(n)",
    "description": "Given an integer numRows, return the kth row of Pascal's triangle.",
}

def solve(num_rows: int) -> list[int]:
    """
    Returns the kth row of Pascal's triangle (where k is num_rows - 1).

    Args:
        num_rows: The number of rows in Pascal's triangle to consider.

    Returns:
        A list of integers representing the last row of Pascal's triangle.

    Examples:
        >>> solve(5)
        [1, 4, 6, 4, 1]
        >>> solve(1)
        [1]
    """
    if num_rows <= 0:
        return []

    # Initialize the row with 1s. The size of the nth row is n.
    # We use a 1-based index logic for the size to match num_rows.
    row = [1] * num_rows

    # We iterate from the 3rd row (index 2) up to num_rows.
    # The first two rows [1] and [1, 1] are already covered by the initialization.
    for current_row_idx in range(2, num_rows):
        # To update the row in-place using only O(n) space, 
        # we must iterate backwards. This ensures that when we calculate 
        # row[j], the value at row[j-1] is still from the previous row.
        for j in range(current_row_idx, 0, -1):
            row[j] = row[j] + row[j - 1]

    return row
