METADATA = {
    "id": 2946,
    "name": "Matrix Similarity After Cyclic Shifts",
    "slug": "matrix-similarity-after-cyclic-shifts",
    "category": "Matrix",
    "aliases": [],
    "tags": ["matrix", "simulation", "array"],
    "difficulty": "medium",
    "time_complexity": "O(n^2)",
    "space_complexity": "O(1)",
    "description": "Determine if a matrix can be made similar to another by performing cyclic shifts on each row and column.",
}

def solve(matrix: list[list[int]], target: list[list[int]]) -> bool:
    """
    Determines if 'matrix' can be transformed into 'target' using cyclic shifts.
    
    The problem allows cyclic shifts on rows and columns. However, a key property 
    of cyclic shifts is that they preserve the multiset of elements in each row 
    and each column. For a matrix to be transformable, the multiset of elements 
    in row i of 'matrix' must match row i of 'target', and similarly for columns.
    
    Args:
        matrix: The initial n x n matrix.
        target: The target n x n matrix.
        
    Returns:
        True if the matrix can be transformed into the target, False otherwise.
        
    Examples:
        >>> solve([[1, 2], [3, 4]], [[2, 1], [4, 3]])
        True
        >>> solve([[1, 2], [3, 4]], [[1, 3], [2, 4]])
        True
        >>> solve([[1, 2], [3, 4]], [[1, 2], [4, 3]])
        False
    """
    n = len(matrix)
    
    # 1. Check if each row in 'matrix' is a cyclic shift of the corresponding row in 'target'
    for r in range(n):
        row_matrix = matrix[r]
        row_target = target[r]
        
        # To check cyclic shift, we can use the property that row_target 
        # must be a substring of (row_matrix + row_matrix)
        # Since we need to handle multisets and exact cyclic shifts:
        if sorted(row_matrix) != sorted(row_target):
            return False
        
        # Find the shift offset by finding where the first element of row_target appears in row_matrix
        # Note: There might be multiple occurrences, so we must verify the actual cyclic shift
        found_shift = False
        first_val = row_target[0]
        for shift in range(n):
            if row_matrix[shift] == first_val:
                # Check if this specific shift works
                match = True
                for i in range(n):
                    if row_matrix[(shift + i) % n] != row_target[i]:
                        match = False
                        break
                if match:
                    found_shift = True
                    break
        if not found_shift:
            return False

    # 2. Check if each column in 'matrix' is a cyclic shift of the corresponding column in 'target'
    for c in range(n):
        col_matrix = [matrix[r][c] for r in range(n)]
        col_target = [target[r][c] for r in range(n)]
        
        if sorted(col_matrix) != sorted(col_target):
            return False
            
        found_shift = False
        first_val = col_target[0]
        for shift in range(n):
            if col_matrix[shift] == first_val:
                match = True
                for i in range(n):
                    if col_matrix[(shift + i) % n] != col_target[i]:
                        match = False
                        break
                if match:
                    found_shift = True
                    break
        if not found_shift:
            return False

    return True
