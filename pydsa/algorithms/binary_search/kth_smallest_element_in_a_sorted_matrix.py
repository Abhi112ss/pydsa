METADATA = {
    "id": 378,
    "name": "Kth Smallest Element in a Sorted Matrix",
    "slug": "kth-smallest-element-in-a-sorted-matrix",
    "category": "Matrix",
    "aliases": [],
    "tags": ["binary_search", "heap", "matrix"],
    "difficulty": "medium",
    "time_complexity": "O(n * log(max_val - min_val))",
    "space_complexity": "O(1)",
    "description": "Find the kth smallest element in an n x n matrix where each row and column is sorted in ascending order.",
}

def solve(matrix: list[list[int]], k: int) -> int:
    """
    Finds the kth smallest element in an n x n matrix using binary search on the value range.

    Args:
        matrix: An n x n matrix where each row and column is sorted in ascending order.
        k: The rank of the element to find (1-indexed).

    Returns:
        The kth smallest element in the matrix.

    Examples:
        >>> solve([[1, 5, 9], [10, 11, 13], [12, 13, 15]], 8)
        13
        >>> solve([[-5]], 1)
        -5
    """
    n = len(matrix)
    low = matrix[0][0]
    high = matrix[n - 1][n - 1]

    def count_less_equal(target: int) -> int:
        """
        Counts how many elements in the matrix are less than or equal to the target.
        Uses a staircase walk starting from the bottom-left corner.
        """
        count = 0
        row = n - 1
        col = 0
        
        # Start from bottom-left and move up or right
        while row >= 0 and col < n:
            if matrix[row][col] <= target:
                # If current element is <= target, all elements above it in this column are also <= target
                count += (row + 1)
                col += 1
            else:
                # If current element is > target, move up to find smaller elements
                row -= 1
        return count

    # Binary search on the range of values [low, high]
    while low < high:
        mid = low + (high - low) // 2
        
        # If the number of elements <= mid is at least k, the answer is in [low, mid]
        if count_less_equal(mid) >= k:
            high = mid
        else:
            # Otherwise, the answer must be in [mid + 1, high]
            low = mid + 1

    return low
