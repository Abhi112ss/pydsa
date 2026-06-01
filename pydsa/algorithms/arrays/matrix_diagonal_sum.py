METADATA = {
    "id": 1572,
    "name": "Matrix Diagonal Sum",
    "slug": "matrix-diagonal-sum",
    "category": "Array",
    "aliases": [],
    "tags": ["array", "matrix"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Calculate the sum of elements on the primary and secondary diagonals of a square matrix.",
}

def solve(mat: list[list[int]]) -> int:
    """
    Calculates the sum of the primary and secondary diagonals of a square matrix.
    
    If the matrix has an odd dimension, the center element is part of both 
    diagonals and should only be counted once.

    Args:
        mat: A square 2D list of integers.

    Returns:
        The total sum of the diagonal elements.

    Examples:
        >>> solve([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        25
        >>> solve([[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]])
        8
    """
    n = len(mat)
    total_sum = 0

    for i in range(n):
        # Add element from the primary diagonal (row index == col index)
        total_sum += mat[i][i]
        
        # Add element from the secondary diagonal (row index + col index == n - 1)
        # The secondary diagonal index is calculated as (n - 1 - i)
        secondary_col_index = n - 1 - i
        
        # Avoid double-counting the center element in odd-sized matrices
        if secondary_col_index != i:
            total_sum += mat[i][secondary_col_index]

    return total_sum
