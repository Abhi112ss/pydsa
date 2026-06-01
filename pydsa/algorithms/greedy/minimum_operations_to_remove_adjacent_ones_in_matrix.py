METADATA = {
    "id": 2123,
    "name": "Minimum Operations to Remove Adjacent Ones in Matrix",
    "slug": "minimum-operations-to-remove-adjacent-ones-in-matrix",
    "category": "Greedy",
    "aliases": [],
    "tags": ["greedy", "matrix", "array"],
    "difficulty": "medium",
    "time_complexity": "O(m * n)",
    "space_complexity": "O(1)",
    "description": "Find the minimum number of operations to remove all adjacent ones in a matrix by treating rows and columns independently.",
}

def solve(matrix: list[list[int]]) -> int:
    """
    Calculates the minimum number of operations to remove all adjacent ones.
    
    The problem can be decomposed into two independent subproblems:
    1. Minimum operations to remove adjacent ones in each row.
    2. Minimum operations to remove adjacent ones in each column.
    
    The total minimum operations is the sum of the minimum operations 
    required for each row and each column.
    
    Args:
        matrix: A 2D list of integers (0 or 1).

    Returns:
        The minimum number of operations required.

    Examples:
        >>> solve([[1, 1, 0], [1, 1, 0], [0, 0, 0]])
        2
        >>> solve([[1, 0, 1], [0, 1, 0], [1, 0, 1]])
        0
    """
    if not matrix or not matrix[0]:
        return 0

    rows = len(matrix)
    cols = len(matrix[0])
    total_operations = 0

    # Process each row independently
    for r in range(rows):
        total_operations += _count_min_ops_for_line(matrix[r])

    # Process each column independently
    for c in range(cols):
        # Extract column as a list to reuse the same logic
        column_data = [matrix[r][c] for r in range(rows)]
        total_operations += _count_min_ops_for_line(column_data)

    return total_operations

def _count_min_ops_for_line(line: list[int]) -> int:
    """
    Helper function to calculate minimum operations for a 1D array.
    
    An operation consists of picking a contiguous segment of 1s and flipping them to 0s.
    The minimum number of operations is equal to the number of contiguous blocks of 1s.
    
    Args:
        line: A list of integers (0 or 1).

    Returns:
        The number of contiguous segments of 1s.
    """
    operations = 0
    in_segment = False

    for value in line:
        if value == 1:
            # If we encounter a 1 and we weren't already in a segment, 
            # it's the start of a new segment.
            if not in_segment:
                operations += 1
                in_segment = True
        else:
            # If we encounter a 0, the current segment of 1s ends.
            in_segment = False
            
    return operations
