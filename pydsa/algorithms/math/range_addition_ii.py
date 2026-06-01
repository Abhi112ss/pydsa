METADATA = {
    "id": 598,
    "name": "Range Addition II",
    "slug": "range_addition_ii",
    "category": "array",
    "aliases": [],
    "tags": ["array", "math", "greedy"],
    "difficulty": "easy",
    "time_complexity": "O(m)",
    "space_complexity": "O(1)",
    "description": "Return the maximum integer value after applying all range addition operations.",
}


def solve(m: int, n: int, ops: list[list[int]]) -> int:
    """Calculate the maximum value in an m x n matrix after applying range addition operations.

    Args:
        m: Number of rows in the matrix.
        n: Number of columns in the matrix.
        ops: A list of operations where each operation is a list [a, b] meaning
            increment all cells in the submatrix from (0, 0) to (a‑1, b‑1) by 1.

    Returns:
        The maximum integer present in the matrix after all operations.

    Examples:
        >>> solve(3, 3, [[2,2],[3,3]])
        2
        >>> solve(3, 3, [])
        9
    """
    # If there are no operations, every cell is incremented zero times;
    # the maximum value equals the total number of cells.
    if not ops:
        return m * n

    # Determine the smallest row and column bounds among all operations.
    min_rows = m
    min_cols = n
    for operation in ops:
        # operation[0] and operation[1] are the dimensions of the increment region.
        if operation[0] < min_rows:
            min_rows = operation[0]
        if operation[1] < min_cols:
            min_cols = operation[1]

    # The intersection of all increment regions defines the area where the
    # maximum value occurs; its size is min_rows * min_cols.
    return min_rows * min_cols