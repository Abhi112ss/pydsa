METADATA = {
    "id": 363,
    "name": "Max Sum of Rectangle No Larger Than K",
    "slug": "max-sum-of-rectangle-no-larger-than-k",
    "category": "Matrix",
    "aliases": [],
    "tags": ["binary_search", "dynamic_programming", "matrix", "prefix_sum"],
    "difficulty": "hard",
    "time_complexity": "O(rows^2 * cols * log(cols))",
    "space_complexity": "O(cols)",
    "description": "Find the maximum sum of a rectangle in a 2D matrix such that the sum is no larger than a given integer k.",
}

import bisect

def solve(matrix: list[list[int]], k: int) -> int:
    """
    Finds the maximum sum of a rectangle in a 2D matrix that is <= k.

    Args:
        matrix: A 2D list of integers representing the matrix.
        k: The upper bound for the rectangle sum.

    Returns:
        The maximum sum found that is less than or equal to k. 
        Returns -float('inf') if no such rectangle exists (though problem constraints usually imply existence).

    Examples:
        >>> solve([[1, 0, 1], [0, -2, 3]], 2)
        2
        >>> solve([[1, 2], [3, 4]], 5)
        5
    """
    if not matrix or not matrix[0]:
        return 0

    rows = len(matrix)
    cols = len(matrix[0])
    max_sum = float('-inf')

    # We iterate through all possible pairs of row boundaries (top_row, bottom_row).
    # This reduces the 2D problem into a 1D problem of finding a subarray sum <= k.
    for top_row in range(rows):
        # column_sums stores the sum of elements between top_row and bottom_row for each column.
        column_sums = [0] * cols
        
        for bottom_row in range(top_row, rows):
            for col in range(cols):
                column_sums[col] += matrix[bottom_row][col]

            # Now solve the 1D problem: Find max subarray sum in column_sums <= k.
            # We use a sorted list of prefix sums to perform binary search.
            # In Python, bisect on a sorted list is the standard way to simulate a BST.
            prefix_sums = [0]
            current_prefix_sum = 0
            
            for val in column_sums:
                current_prefix_sum += val
                
                # We want: current_prefix_sum - previous_prefix_sum <= k
                # Which is: previous_prefix_sum >= current_prefix_sum - k
                # We search for the smallest prefix_sum in our sorted list that satisfies this.
                target = current_prefix_sum - k
                idx = bisect.bisect_left(prefix_sums, target)
                
                if idx < len(prefix_sums):
                    # A valid subarray sum was found.
                    max_sum = max(max_sum, current_prefix_sum - prefix_sums[idx])
                
                # If we already found k, we can't do better.
                if max_sum == k:
                    return k
                
                # Maintain the sorted order of prefix sums for the next iteration.
                bisect.insort(prefix_sums, current_prefix_sum)

    return int(max_sum)
