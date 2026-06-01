METADATA = {
    "id": 2732,
    "name": "Find a Good Subset of the Matrix",
    "slug": "find-a-good-subset-of-the-matrix",
    "category": "Greedy",
    "aliases": [],
    "tags": ["arrays", "greedy"],
    "difficulty": "medium",
    "time_complexity": "O(m * n)",
    "space_complexity": "O(m * n)",
    "description": "Find a subset of matrix elements such that the sum of elements in each row is equal and the sum of elements in each column is equal, maximizing the subset size.",
}

def solve(matrix: list[list[int]]) -> int:
    """
    Finds the maximum size of a subset of matrix elements such that the sum 
    of elements in each row is equal and the sum of elements in each column is equal.

    Args:
        matrix: A 2D list of integers representing the matrix.

    Returns:
        The maximum number of elements in a 'good' subset.

    Examples:
        >>> solve([[1, 2], [3, 4]])
        1
        >>> solve([[1, 1], [1, 1]])
        4
    """
    rows = len(matrix)
    cols = len(matrix[0])

    # Step 1: Calculate the frequency of each sum possible for rows and columns.
    # A 'good' subset requires all chosen rows to have the same sum 'r_sum'
    # and all chosen columns to have the same sum 'c_sum'.
    # However, the problem implies we pick a subset of indices (rows and columns).
    # If we pick a subset of rows R and a subset of columns C, the elements 
    # in the intersection must satisfy the condition.
    # Actually, the problem asks for a subset of elements. 
    # A subset of elements forms a 'good' subset if we can pick a set of rows 
    # and a set of columns such that we only pick elements at the intersections.
    # Wait, the problem definition: "a subset of elements is good if the sum of 
    # elements in each row is equal and the sum of elements in each column is equal."
    # This is satisfied if we pick a subset of rows and a subset of columns 
    # and take all elements at their intersections.
    
    # Let's find all possible row sums and their frequencies.
    row_sum_counts: dict[int, int] = {}
    for r in range(rows):
        current_row_sum = sum(matrix[r])
        row_sum_counts[current_row_sum] = row_sum_counts.get(current_row_sum, 0) + 1

    # Let's find all possible column sums and their frequencies.
    col_sum_counts: dict[int, int] = {}
    for c in range(cols):
        current_col_sum = 0
        for r in range(rows):
            current_col_sum += matrix[r][c]
        col_sum_counts[current_col_sum] = col_sum_counts.get(current_col_sum, 0) + 1

    # Step 2: The size of the subset formed by picking 'num_rows' rows 
    # and 'num_cols' columns is 'num_rows * num_cols'.
    # To maximize this, we find the maximum frequency of any row sum 
    # and the maximum frequency of any column sum.
    
    max_row_freq = 0
    for count in row_sum_counts.values():
        if count > max_row_freq:
            max_row_freq = count
            
    max_col_freq = 0
    for count in col_sum_counts.values():
        if count > max_col_freq:
            max_col_freq = count

    # The maximum size is the product of the highest frequencies.
    return max_row_freq * max_col_freq
