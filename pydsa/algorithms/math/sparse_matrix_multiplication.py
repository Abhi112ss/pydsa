METADATA = {
    "id": 311,
    "name": "Sparse Matrix Multiplication",
    "slug": "sparse-matrix-multiplication",
    "category": "Matrix",
    "aliases": [],
    "tags": ["matrix", "hash_map", "optimization"],
    "difficulty": "medium",
    "time_complexity": "O(m * k * n) in worst case, but significantly faster for sparse matrices",
    "space_complexity": "O(m * n) to store the result matrix",
    "description": "Multiply two sparse matrices by iterating only over non-zero elements to optimize performance.",
}

def solve(mat1: list[list[int]], mat2: list[list[int]]) -> list[list[int]]:
    """
    Multiplies two sparse matrices efficiently.

    Args:
        mat1: An m x k matrix.
        mat2: A k x n matrix.

    Returns:
        An m x n matrix representing the product of mat1 and mat2.

    Examples:
        >>> solve([[1, 0, 0], [-1, 0, 3]], [[7, 0, 0], [0, 0, 0], [0, 0, 1]])
        [[7, 0, 0], [-7, 0, 3]]
    """
    rows_mat1 = len(mat1)
    cols_mat1 = len(mat1[0])
    cols_mat2 = len(mat2[0])

    # Initialize the result matrix with zeros
    result = [[0 for _ in range(cols_mat2)] for _ in range(rows_mat1)]

    # Pre-process mat1 to store only non-zero elements to avoid redundant operations.
    # We store them as (row, col, value) tuples.
    non_zero_elements = []
    for r in range(rows_mat1):
        for c in range(cols_mat1):
            if mat1[r][c] != 0:
                non_zero_elements.append((r, c, mat1[r][c]))

    # Iterate through the non-zero elements of mat1.
    # For each non-zero element mat1[r][c], it contributes to the result 
    # at result[r][k] for all k where mat2[c][k] is non-zero.
    for r, c, val1 in non_zero_elements:
        # We only need to iterate through the row of mat2 that corresponds 
        # to the column index 'c' of the current non-zero element in mat1.
        for k in range(cols_mat2):
            if mat2[c][k] != 0:
                result[r][k] += val1 * mat2[c][k]

    return result
