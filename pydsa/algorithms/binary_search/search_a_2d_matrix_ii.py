METADATA = {
    "id": 240,
    "name": "Search a 2D Matrix II",
    "slug": "search-a-2d-matrix-ii",
    "category": "Matrix",
    "aliases": [],
    "tags": ["binary_search", "matrix", "two_pointer"],
    "difficulty": "medium",
    "time_complexity": "O(m + n)",
    "space_complexity": "O(1)",
    "description": "Search for a target value in an m x n integer matrix where rows and columns are sorted in ascending order.",
}

def solve(matrix: list[list[int]], target: int) -> bool:
    """
    Searches for a target value in a 2D matrix where each row and column is sorted.

    The algorithm starts from the top-right corner. If the current element is 
    greater than the target, we move left (decreasing the value). If the 
    current element is smaller than the target, we move down (increasing the value).

    Args:
        matrix: A list of lists of integers representing the m x n matrix.
        target: The integer value to search for.

    Returns:
        True if the target is found, False otherwise.

    Examples:
        >>> solve([[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24]], 5)
        True
        >>> solve([[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24]], 20)
        False
    """
    if not matrix or not matrix[0]:
        return False

    rows = len(matrix)
    cols = len(matrix[0])

    # Start from the top-right corner
    current_row = 0
    current_col = cols - 1

    while current_row < rows and current_col >= 0:
        current_val = matrix[current_row][current_col]

        if current_val == target:
            return True
        
        # If current value is too large, the entire column below it 
        # will also be too large, so move left.
        if current_val > target:
            current_col -= 1
        # If current value is too small, the entire row to the left 
        # will also be too small, so move down.
        else:
            current_row += 1

    return False
