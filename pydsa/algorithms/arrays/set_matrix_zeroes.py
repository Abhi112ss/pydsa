METADATA = {
    "id": 73,
    "name": "Set Matrix Zeroes",
    "slug": "set-matrix-zeroes",
    "category": "Array",
    "aliases": [],
    "tags": ["matrix", "array"],
    "difficulty": "medium",
    "time_complexity": "O(m*n)",
    "space_complexity": "O(1)",
    "description": "Given an m x n integer matrix, if an element is 0, set its entire row and column to 0's in place.",
}

def solve(matrix: list[list[int]]) -> None:
    """
    Modifies the input matrix in-place to set rows and columns to zero 
    if they contain a zero.

    Args:
        matrix: A list of lists of integers representing the m x n matrix.

    Returns:
        None. The matrix is modified in-place.

    Examples:
        >>> mat = [[1,1,1],[1,0,1],[1,1,1]]
        >>> solve(mat)
        >>> mat
        [[1, 0, 1], [0, 0, 0], [1, 0, 1]]
    """
    if not matrix or not matrix[0]:
        return

    rows_count = len(matrix)
    cols_count = len(matrix[0])
    
    # Flags to determine if the first row or first column should be zeroed
    first_row_has_zero = False
    first_col_has_zero = False

    # Step 1: Check if the first row or first column contains any zeros
    for col_idx in range(cols_count):
        if matrix[0][col_idx] == 0:
            first_row_has_zero = True
            break

    for row_idx in range(rows_count):
        if matrix[row_idx][0] == 0:
            first_col_has_zero = True
            break

    # Step 2: Use the first row and first column as markers
    # If matrix[i][j] is 0, mark matrix[i][0] and matrix[0][j] as 0
    for row_idx in range(1, rows_count):
        for col_idx in range(1, cols_count):
            if matrix[row_idx][col_idx] == 0:
                matrix[row_idx][0] = 0
                matrix[0][col_idx] = 0

    # Step 3: Iterate through the matrix (excluding first row/col) 
    # and zero out cells based on the markers set in Step 2
    for row_idx in range(1, rows_count):
        for col_idx in range(1, cols_count):
            if matrix[row_idx][0] == 0 or matrix[0][col_idx] == 0:
                matrix[row_idx][col_idx] = 0

    # Step 4: Finally, zero out the first row and first column if needed
    if first_row_has_zero:
        for col_idx in range(cols_count):
            matrix[0][col_idx] = 0

    if first_col_has_zero:
        for row_idx in range(rows_count):
            matrix[row_idx][0] = 0