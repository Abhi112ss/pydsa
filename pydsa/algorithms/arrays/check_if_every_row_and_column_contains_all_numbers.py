METADATA = {
    "id": 2133,
    "name": "Check if Every Row and Column Contains All Numbers",
    "slug": "check-if-every-row-and-column-contains-all-numbers",
    "category": "Matrix",
    "aliases": [],
    "tags": ["matrix", "hash_set"],
    "difficulty": "medium",
    "time_complexity": "O(m * n)",
    "space_complexity": "O(max(m, n))",
    "description": "Determine if every row and every column in an m x n matrix contains all integers from 1 to min(m, n).",
}

def solve(matrix: list[list[int]]) -> bool:
    """
    Checks if every row and every column in the matrix contains all numbers from 1 to min(m, n).

    Args:
        matrix: A 2D list of integers representing the m x n matrix.

    Returns:
        True if every row and column contains all numbers from 1 to min(m, n), False otherwise.

    Examples:
        >>> solve([[1, 2, 3], [2, 3, 1], [3, 1, 2]])
        True
        >>> solve([[1, 2, 3], [2, 3, 1], [3, 2, 1]])
        False
    """
    rows = len(matrix)
    cols = len(matrix[0])
    target_count = min(rows, cols)
    
    # The set of required numbers: {1, 2, ..., target_count}
    # We can optimize by checking if the size of the set of unique elements 
    # in a row/col equals target_count, assuming elements are within range.
    # However, the problem implies elements are within [1, n].
    
    # Check rows
    for r in range(rows):
        row_set = set()
        for c in range(cols):
            val = matrix[r][c]
            # Only add if it's within the valid range [1, target_count]
            if 1 <= val <= target_count:
                row_set.add(val)
        
        # If the number of unique valid elements is not target_count, row is invalid
        if len(row_set) != target_count:
            return False

    # Check columns
    for c in range(cols):
        col_set = set()
        for r in range(rows):
            val = matrix[r][c]
            # Only add if it's within the valid range [1, target_count]
            if 1 <= val <= target_count:
                col_set.add(val)
                
        # If the number of unique valid elements is not target_count, column is invalid
        if len(col_set) != target_count:
            return False

    return True
