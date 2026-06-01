METADATA = {
    "id": 2643,
    "name": "Row With Maximum Ones",
    "slug": "row-with-maximum-ones",
    "category": "Matrix",
    "aliases": [],
    "tags": ["matrix", "array_traversal"],
    "difficulty": "easy",
    "time_complexity": "O(m * n)",
    "space_complexity": "O(1)",
    "description": "Find the index of the row in a binary matrix that contains the maximum number of ones.",
}

def solve(mat: list[list[int]]) -> int:
    """
    Finds the index of the row with the maximum number of ones in a binary matrix.

    Args:
        mat: A 2D list of integers where each element is either 0 or 1.

    Returns:
        The zero-based index of the row containing the most ones. 
        If multiple rows have the same maximum number of ones, the smallest index is returned.

    Examples:
        >>> solve([[0, 1], [1, 1]])
        1
        >>> solve([[1, 0], [0, 1]])
        0
        >>> solve([[0, 0, 0], [1, 1, 1], [1, 0, 1]])
        1
    """
    max_ones_count = -1
    best_row_index = 0
    
    # Iterate through each row in the matrix
    for row_index, row in enumerate(mat):
        # Count the number of 1s in the current row
        # Since it's a binary matrix, sum() is an efficient way to count 1s
        current_ones_count = sum(row)
        
        # If the current row has more ones than any previous row, update the tracker
        # Using '>' ensures we keep the smallest index in case of ties
        if current_ones_count > max_ones_count:
            max_ones_count = current_ones_count
            best_row_index = row_index
            
    return best_row_index
