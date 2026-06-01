METADATA = {
    "id": 498,
    "name": "Diagonal Traverse",
    "slug": "diagonal-traverse",
    "category": "Matrix",
    "aliases": [],
    "tags": ["matrix", "simulation"],
    "difficulty": "medium",
    "time_complexity": "O(m*n)",
    "space_complexity": "O(1)",
    "description": "Return an array of elements in a 2D matrix in a diagonal zigzag order.",
}

def solve(matrix: list[list[int]]) -> list[int]:
    """
    Traverses a 2D matrix in a diagonal zigzag pattern.

    The traversal follows the sum of indices (i + j). For a given sum 's', 
    all elements (i, j) such that i + j = s belong to the same diagonal.
    The direction of traversal flips between even and odd sums.

    Args:
        matrix: A 2D list of integers representing the input matrix.

    Returns:
        A 1D list of integers containing the elements in diagonal order.

    Examples:
        >>> solve([[1,2,3],[4,5,6],[7,8,9]])
        [1, 2, 4, 7, 5, 3, 6, 8, 9]
    """
    if not matrix or not matrix[0]:
        return []

    rows = len(matrix)
    cols = len(matrix[0])
    result = []
    
    # The total number of diagonals is (rows + cols - 1)
    # Each diagonal is characterized by the sum of its indices (i + j)
    for diagonal_sum in range(rows + cols - 1):
        # Temporary list to hold elements of the current diagonal
        current_diagonal = []
        
        # Determine the starting row for this diagonal sum.
        # i + j = diagonal_sum => j = diagonal_sum - i
        # Constraints: 0 <= i < rows AND 0 <= j < cols
        # Therefore: 0 <= diagonal_sum - i < cols  =>  i <= diagonal_sum AND i > diagonal_sum - cols
        start_row = max(0, diagonal_sum - (cols - 1))
        end_row = min(rows - 1, diagonal_sum)
        
        for r in range(start_row, end_row + 1):
            c = diagonal_sum - r
            current_diagonal.append(matrix[r][c])
            
        # If the diagonal index is even, we traverse "upwards" (bottom-left to top-right).
        # In our loop, we collected them from top-row to bottom-row, 
        # so we reverse the list for even sums to simulate the upward movement.
        if diagonal_sum % 2 == 0:
            result.extend(current_diagonal[::-1])
        else:
            result.extend(current_diagonal)
            
    return result
