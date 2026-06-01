METADATA = {
    "id": 2718,
    "name": "Sum of Matrix After Queries",
    "slug": "sum-of-matrix-after-queries",
    "category": "Array",
    "aliases": [],
    "tags": ["arrays", "greedy"],
    "difficulty": "medium",
    "time_complexity": "O(q)",
    "space_complexity": "O(m + n)",
    "description": "Calculate the sum of a matrix after a series of row and column update queries by processing them in reverse order.",
}

def solve(n: int, queries: list[list[int]]) -> int:
    """
    Calculates the sum of an n x n matrix after applying a series of queries.
    
    Each query is [type, index, val], where type 0 is a row update and 
    type 1 is a column update. Since later queries overwrite earlier ones,
    we process queries in reverse to ensure each row/column is only 
    accounted for by its most recent update.

    Args:
        n: The dimension of the n x n matrix.
        queries: A list of queries where each query is [type, index, val].

    Returns:
        The total sum of the matrix after all queries are applied.

    Examples:
        >>> solve(3, [[0, 0, 1], [1, 2, 2], [0, 2, 3], [1, 0, 4]])
        21
    """
    # Track which rows and columns have already been updated by a later query
    row_visited = [False] * n
    col_visited = [False] * n
    
    # Track the number of rows and columns that have been "fixed" by a query
    rows_remaining = n
    cols_remaining = n
    
    total_sum = 0

    # Process queries from last to first (reverse order)
    for query_type, index, val in reversed(queries):
        # If all rows or columns are already covered, no need to process further
        if rows_remaining == 0 or cols_remaining == 0:
            break

        if query_type == 0:  # Row update
            if not row_visited[index]:
                # This row's value will apply to all currently unvisited columns
                total_sum += val * cols_remaining
                row_visited[index] = True
                rows_remaining -= 1
        else:  # Column update
            if not col_visited[index]:
                # This column's value will apply to all currently unvisited rows
                total_sum += val * rows_remaining
                col_visited[index] = True
                cols_remaining -= 1

    return total_sum
