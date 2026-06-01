METADATA = {
    "id": 74,
    "name": "Search a 2D Matrix",
    "slug": "search-a-2d-matrix",
    "category": "Binary Search",
    "aliases": [],
    "tags": ["binary_search", "matrix"],
    "difficulty": "medium",
    "time_complexity": "O(log(m * n))",
    "space_complexity": "O(1)",
    "description": "Determine if a target value exists in an m x n integer matrix where each row is sorted and the first integer of each row is greater than the last integer of the previous row.",
}

def solve(matrix: list[list[int]], target: int) -> bool:
    """
    Searches for a target value in a 2D matrix using binary search.

    The matrix is treated as a single sorted 1D array by mapping a 1D index 
    to 2D coordinates using row = index // cols and col = index % cols.

    Args:
        matrix: A list of lists of integers representing the m x n matrix.
        target: The integer value to search for.

    Returns:
        True if the target is found in the matrix, False otherwise.

    Examples:
        >>> solve([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3)
        True
        >>> solve([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13)
        False
    """
    if not matrix or not matrix[0]:
        return False

    rows = len(matrix)
    cols = len(matrix[0])
    
    # Treat the 2D matrix as a virtual 1D array of length rows * cols
    low = 0
    high = (rows * cols) - 1

    while low <= high:
        mid = (low + high) // 2
        
        # Map the 1D index back to 2D row and column indices
        # row = index // total_columns
        # col = index % total_columns
        current_row = mid // cols
        current_col = mid % cols
        current_value = matrix[current_row][current_col]

        if current_value == target:
            return True
        elif current_value < target:
            # Target is in the right half
            low = mid + 1
        else:
            # Target is in the left half
            high = mid - 1

    return False
