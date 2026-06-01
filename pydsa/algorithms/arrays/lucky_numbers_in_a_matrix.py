METADATA = {
    "id": 1380,
    "name": "Lucky Numbers in a Matrix",
    "slug": "lucky-numbers-in-a-matrix",
    "category": "Array",
    "aliases": [],
    "tags": ["arrays", "math"],
    "difficulty": "medium",
    "time_complexity": "O(m * n)",
    "space_complexity": "O(m + n)",
    "description": "Find elements in a matrix that are the minimum in their row and the maximum in their column.",
}

def solve(matrix: list[list[int]]) -> list[int]:
    """
    Finds the lucky numbers in a given 2D matrix.
    
    A lucky number is an element that is the minimum in its row 
    and the maximum in its column.

    Args:
        matrix: A 2D list of integers representing the matrix.

    Returns:
        A list of integers containing all lucky numbers found in the matrix.

    Examples:
        >>> solve([[3, 7, 8], [9, 11, 13], [15, 16, 17]])
        [3]
        >>> solve([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        [7]
        >>> solve([[1, 1, 1], [1, 1, 1], [1, 1, 1]])
        [1]
    """
    if not matrix or not matrix[0]:
        return []

    rows = len(matrix)
    cols = len(matrix[0])

    # Step 1: Find the minimum element in each row
    row_minimums = []
    for row in matrix:
        row_minimums.append(min(row))

    # Step 2: Find the maximum element in each column
    col_maximums = []
    for col_idx in range(cols):
        current_max = matrix[0][col_idx]
        for row_idx in range(1, rows):
            if matrix[row_idx][col_idx] > current_max:
                current_max = matrix[row_idx][col_idx]
        col_maximums.append(current_max)

    # Step 3: The intersection of row minimums and column maximums are the lucky numbers
    # We use a set for O(1) average lookup time
    col_max_set = set(col_maximums)
    lucky_numbers = []
    
    for val in row_minimums:
        if val in col_max_set:
            lucky_numbers.append(val)

    return lucky_numbers
