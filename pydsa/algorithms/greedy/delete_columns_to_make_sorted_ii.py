METADATA = {
    "id": 955,
    "name": "Delete Columns to Make Sorted II",
    "slug": "delete-columns-to-make-sorted-ii",
    "category": "Greedy",
    "aliases": [],
    "tags": ["greedy", "string_traversal", "array"],
    "difficulty": "medium",
    "time_complexity": "O(N * M)",
    "space_complexity": "O(N)",
    "description": "Find the minimum number of columns to delete such that the remaining columns are in non-decreasing order and each column is strictly increasing relative to the previous one where necessary.",
}

def solve(columns: list[str]) -> int:
    """
    Finds the minimum number of columns to delete so that the remaining columns 
    are in lexicographical order.

    Args:
        columns: A list of strings representing the columns of a grid.

    Returns:
        The minimum number of columns to delete.

    Examples:
        >>> solve(["ca","bb","ac"])
        1
        >>> solve(["xc","zb","ya","ba","dc"])
        2
    """
    if not columns or not columns[0]:
        return 0

    num_rows = len(columns)
    num_cols = len(columns[0])
    
    # is_sorted_row[i] is True if the prefix of row i is already 
    # strictly lexicographically smaller than the prefix of row i+1.
    is_sorted_row = [False] * (num_rows - 1)
    deleted_count = 0

    for col_idx in range(num_cols):
        can_keep_column = True
        
        # Check if adding this column violates the non-decreasing order 
        # for rows that are not yet strictly sorted.
        for row_idx in range(num_rows - 1):
            if not is_sorted_row[row_idx]:
                if columns[row_idx][col_idx] > columns[row_idx + 1][col_idx]:
                    can_keep_column = False
                    break
        
        if can_keep_column:
            # If we keep the column, update the sorted status of rows.
            # A row pair becomes 'strictly sorted' if the current character 
            # in row i is strictly less than the character in row i+1.
            for row_idx in range(num_rows - 1):
                if columns[row_idx][col_idx] < columns[row_idx + 1][col_idx]:
                    is_sorted_row[row_idx] = True
        else:
            # If the column violates the order, we must delete it.
            deleted_count += 1

    return deleted_count
