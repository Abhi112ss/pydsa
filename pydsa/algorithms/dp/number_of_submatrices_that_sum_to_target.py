METADATA = {
    "id": 1074,
    "name": "Number of Submatrices That Sum to Target",
    "slug": "number-of-submatrices-that-sum-to-target",
    "category": "Matrix",
    "aliases": [],
    "tags": ["prefix_sum", "hash_map", "matrix"],
    "difficulty": "medium",
    "time_complexity": "O(rows^2 * cols)",
    "space_complexity": "O(cols)",
    "description": "Find the total number of non-empty submatrices that sum up to a given target value.",
}

def solve(matrix: list[list[int]], target: int) -> int:
    """
    Calculates the number of submatrices that sum up to the target value.

    The algorithm reduces the 2D problem into a 1D problem by fixing the 
    top and bottom row boundaries and calculating the column-wise sums 
    between them. This transforms the problem into finding subarrays 
    that sum to a target, which is solved efficiently using a hash map.

    Args:
        matrix: A 2D list of integers representing the matrix.
        target: The target sum to search for.

    Returns:
        The total count of submatrices whose elements sum to target.

    Examples:
        >>> solve([[0,1,0],[1,1,1],[0,1,0]], 0)
        4
        >>> solve([[1,-1],[-1,1]], 0)
        4
    """
    rows = len(matrix)
    cols = len(matrix[0])

    # Step 1: Precompute prefix sums for each row to allow O(1) 
    # calculation of row segments.
    # row_prefix_sums[r][c] will store the sum of matrix[r][0...c-1]
    row_prefix_sums = [[0] * (cols + 1) for _ in range(rows)]
    for r in range(rows):
        for c in range(cols):
            row_prefix_sums[r][c + 1] = row_prefix_sums[r][c] + matrix[r][c]

    count = 0

    # Step 2: Iterate through all possible pairs of column boundaries (left and right).
    # This reduces the 2D problem to a 1D problem on the rows.
    for col_start in range(cols):
        for col_end in range(col_start, cols):
            # map_sums stores the frequency of prefix sums encountered so far
            # in the current column range.
            map_sums = {0: 1}
            current_running_sum = 0
            
            for r in range(rows):
                # Calculate the sum of the current row segment between col_start and col_end.
                # Using the precomputed row prefix sums.
                row_segment_sum = row_prefix_sums[r][col_end + 1] - row_prefix_sums[r][col_start]
                current_running_sum += row_segment_sum
                
                # Step 3: Use the 'Subarray Sum Equals K' logic.
                # If (current_running_sum - target) exists in the map, it means 
                # there is a submatrix ending at row 'r' that sums to target.
                diff = current_running_sum - target
                if diff in map_sums:
                    count += map_sums[diff]
                
                # Update the map with the current running sum.
                map_sums[current_running_sum] = map_sums.get(current_running_sum, 0) + 1
                
    return count
