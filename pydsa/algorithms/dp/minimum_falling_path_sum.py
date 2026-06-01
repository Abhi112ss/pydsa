METADATA = {
    "id": 931,
    "name": "Minimum Falling Path Sum",
    "slug": "minimum-falling-path-sum",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dynamic_programming", "matrix"],
    "difficulty": "medium",
    "time_complexity": "O(n^2)",
    "space_complexity": "O(1)",
    "description": "Find the minimum sum of a falling path in a square matrix.",
}

def solve(matrix: list[list[int]]) -> int:
    """
    Calculates the minimum sum of a falling path in an n x n matrix.
    
    A falling path starts at any element in the first row and chooses one element 
    from each subsequent row such that the next element is in the same column 
    or adjacent columns.

    Args:
        matrix: A square matrix of integers.

    Returns:
        The minimum sum of a falling path.

    Examples:
        >>> solve([[2,1,3],[6,5,4],[7,8,9]])
        11
        >>> solve([[10,-2,-10],[-1, -4, -5],[-1, -1, -1]])
        -13
    """
    if not matrix or not matrix[0]:
        return 0

    rows = len(matrix)
    cols = len(matrix[0])

    # We iterate from the second row to the bottom row.
    # We update the matrix in-place to achieve O(1) extra space complexity.
    for row in range(1, rows):
        for col in range(cols):
            # Identify the possible predecessors from the previous row:
            # (row-1, col-1), (row-1, col), (row-1, col+1)
            
            # The direct predecessor in the same column
            prev_min = matrix[row - 1][col]
            
            # Check the diagonal left predecessor
            if col > 0:
                prev_min = min(prev_min, matrix[row - 1][col - 1])
                
            # Check the diagonal right predecessor
            if col < cols - 1:
                prev_min = min(prev_min, matrix[row - 1][col + 1])
            
            # Update the current cell with the minimum path sum ending here
            matrix[row][col] += prev_min

    # The answer is the minimum value found in the last row
    return min(matrix[-1])
