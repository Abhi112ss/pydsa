METADATA = {
    "id": 2661,
    "name": "First Completely Painted Row or Column",
    "slug": "first-completely-painted-row-or-column",
    "category": "Array",
    "aliases": [],
    "tags": ["array", "prefix_sum", "hash table"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Find the index of the first row or column that is completely painted given a sequence of cell coordinates.",
}

def solve(n: int, queries: list[list[int]]) -> list[int]:
    """
    Finds the index of the first row or column that becomes fully painted.

    Args:
        n (int): The size of the n x n grid.
        queries (list[list[int]]): A list of queries where queries[i] = [row_i, col_i].

    Returns:
        list[int]: A list containing two integers: [first_row_index, first_col_index].
                   If a row/column is never fully painted, return -1 for that index.

    Examples:
        >>> solve(3, [[0,0], [0,1], [1,0], [0,2], [2,0], [1,1], [1,2], [2,1], [2,2]])
        [0, 0]
        >>> solve(3, [[0,0], [1,1], [2,2], [0,1], [1,0], [0,2], [1,2], [2,0], [2,1]])
        [-1, -1]
    """
    # row_counts[i] stores how many cells in row i have been painted
    # col_counts[j] stores how many cells in column j have been painted
    row_counts = [0] * n
    col_counts = [0] * n
    
    # To handle duplicate queries (painting the same cell twice), 
    # we need to track which cells are already painted.
    # However, the problem constraints usually imply unique cells or 
    # we must ensure we only increment counts for new cells.
    # Using a set of tuples for visited cells.
    visited = set()
    
    first_row = -1
    first_col = -1
    
    for r, c in queries:
        # If the cell is already painted, skip to avoid double counting
        if (r, c) in visited:
            continue
        visited.add((r, c))
        
        # Increment the count for the current row and column
        row_counts[r] += 1
        col_counts[c] += 1
        
        # Check if the current row or column has just become fully painted
        # We only care about the first occurrence, so check if they are still -1
        if first_row == -1 and row_counts[r] == n:
            first_row = r
            
        if first_col == -1 and col_counts[c] == n:
            first_col = c
            
        # If both are found, we can stop early
        if first_row != -1 and first_col != -1:
            break
            
    return [first_row, first_col]
