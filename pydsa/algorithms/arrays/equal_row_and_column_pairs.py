METADATA = {
    "id": 2352,
    "name": "Equal Row and Column Pairs",
    "slug": "equal-row-and-column-pairs",
    "category": "Matrix",
    "aliases": [],
    "tags": ["hash_map", "matrix"],
    "difficulty": "medium",
    "time_complexity": "O(n^2)",
    "space_complexity": "O(n^2)",
    "description": "Count the number of pairs (r, c) such that row r and column c are equal.",
}

def solve(grid: list[list[int]]) -> int:
    """
    Counts the number of pairs (r, c) such that row r and column c are equal.

    Args:
        grid: An n x n integer matrix.

    Returns:
        The total number of equal row and column pairs.

    Examples:
        >>> solve([[e1, e1, e1], [e1, e1, e1], [e1, e1, e1]]) # where e1 is 1
        6
        >>> solve([[3, 2, 1], [1, 7, 6], [2, 7, 7]])
        0
    """
    n = len(grid)
    row_counts: dict[tuple[int, ...], int] = {}

    # Step 1: Convert each row into a tuple and store its frequency in a hash map
    for row_index in range(n):
        row_tuple = tuple(grid[row_index])
        row_counts[row_tuple] = row_counts.get(row_tuple, 0) + 1

    pair_count = 0

    # Step 2: Construct each column as a tuple and check its existence in the hash map
    for col_index in range(n):
        # Extract column elements into a tuple
        column_tuple = tuple(grid[row_index][col_index] for row_index in range(n))
        
        # If this column matches any rows, add the number of occurrences to the total
        if column_tuple in row_counts:
            pair_count += row_counts[column_tuple]

    return pair_count
