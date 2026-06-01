METADATA = {
    "id": 3212,
    "name": "Count Submatrices With Equal Frequency of X and Y",
    "slug": "count-submatrices-with-equal-frequency-of-x-and-y",
    "category": "Dynamic Programming / Prefix Sum",
    "aliases": [],
    "tags": ["prefix_sum", "hash_map", "matrix"],
    "difficulty": "medium",
    "time_complexity": "O(rows^2 * cols)",
    "space_complexity": "O(cols)",
    "description": "Count the number of submatrices where the frequency of character 'X' equals the frequency of character 'Y'.",
}

def solve(grid: list[list[str]]) -> int:
    """
    Counts the number of submatrices where the frequency of 'X' equals the frequency of 'Y'.

    The problem is transformed by treating 'X' as +1 and 'Y' as -1. A submatrix has 
    equal frequencies if the sum of these values within the submatrix is zero.

    Args:
        grid: A 2D list of strings representing the matrix.

    Returns:
        The total count of submatrices with equal frequency of 'X' and 'Y'.

    Examples:
        >>> solve([["X", "Y"], ["Y", "X"]])
        4
        >>> solve([["X", "X"], ["Y", "Y"]])
        2
    """
    rows = len(grid)
    cols = len(grid[0])
    
    # Transform grid into numerical values: X -> 1, Y -> -1, others -> 0
    # This allows us to use prefix sums to check for equal frequency (sum == 0)
    val_grid = [[0] * cols for _ in range(rows)]
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "X":
                val_grid[r][c] = 1
            elif grid[r][c] == "Y":
                val_grid[r][c] = -1

    total_count = 0

    # Iterate over all possible pairs of top and bottom row boundaries
    for top_row in range(rows):
        # column_sums stores the sum of elements in each column between top_row and bottom_row
        column_sums = [0] * cols
        
        for bottom_row in range(top_row, rows):
            # Update column_sums for the current bottom_row
            for c in range(cols):
                column_sums[c] += val_grid[bottom_row][c]
            
            # Now the problem reduces to finding subarrays in column_sums that sum to 0
            # We use a hash map to store the frequency of prefix sums encountered
            prefix_sum_counts = {0: 1}
            current_running_sum = 0
            
            for val in column_sums:
                current_running_sum += val
                
                # If current_running_sum has been seen before, it means the subarray 
                # between the previous occurrence and now sums to 0
                if current_running_sum in prefix_sum_counts:
                    total_count += prefix_sum_counts[current_running_sum]
                    prefix_sum_counts[current_running_sum] += 1
                else:
                    prefix_sum_counts[current_running_sum] = 1
                    
    return total_count
