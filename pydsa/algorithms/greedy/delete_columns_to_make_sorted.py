METADATA = {
    "id": 944,
    "name": "Delete Columns to Make Sorted",
    "slug": "delete-columns-to-make-sorted",
    "category": "String",
    "aliases": [],
    "tags": ["greedy", "string_traversal"],
    "difficulty": "easy",
    "time_complexity": "O(N * M)",
    "space_complexity": "O(1)",
    "description": "Determine the number of columns in a 2D array of characters that are not sorted in non-decreasing order.",
}

def solve(strs: list[str]) -> int:
    """
    Calculates the number of columns that are not sorted lexicographically.

    Args:
        strs: A list of strings representing a 2D grid of characters.

    Returns:
        The count of columns where characters are not in non-decreasing order.

    Examples:
        >>> solve(["cba", "daf", "ghi"])
        1
        >>> solve(["abc", "bce", "cae"])
        0
        >>> solve(["zyx", "wvu", "tsr"])
        3
    """
    if not strs or not strs[0]:
        return 0

    num_rows = len(strs)
    num_cols = len(strs[0])
    unsorted_columns_count = 0

    # Iterate through each column index
    for col_index in range(num_cols):
        # Check if the current column is sorted by comparing adjacent rows
        for row_index in range(num_rows - 1):
            # If a character in a row is greater than the character in the next row
            # for the same column, the column is not sorted.
            if strs[row_index][col_index] > strs[row_index + 1][col_index]:
                unsorted_columns_count += 1
                # Once we find one violation, we don't need to check the rest of this column
                break

    return unsorted_columns_count
