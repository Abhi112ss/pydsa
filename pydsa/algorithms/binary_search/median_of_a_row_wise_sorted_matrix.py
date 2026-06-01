METADATA = {
    "id": 2387,
    "name": "Median of a Row Wise Sorted Matrix",
    "slug": "median_of_a_row_wise_sorted_matrix",
    "category": "Binary Search",
    "aliases": [],
    "tags": ["binary_search", "matrix"],
    "difficulty": "hard",
    "time_complexity": "O(rows * log(cols) * log(max_val - min_val))",
    "space_complexity": "O(1)",
    "description": "Find the median of a matrix where each row is sorted, using binary search on the value range.",
}

def solve(matrix: list[list[int]]) -> int:
    """
    Finds the median of a matrix where each row is sorted in non-decreasing order.

    The median is the middle element in the sorted list of all elements. 
    Since the total number of elements is always odd (per problem constraints), 
    the median is the element at index (total_elements // 2).

    Args:
        matrix: A 2D list of integers where each row is sorted.

    Returns:
        The median value of the matrix.

    Examples:
        >>> solve([[1, 3, 5], [2, 6, 9], [3, 6, 9]])
        3
        >>> solve([[1, 2], [3, 4], [5, 6], [7, 8]]) # Note: Problem implies odd total
        4
    """
    rows = len(matrix)
    cols = len(matrix[0])
    total_elements = rows * cols
    target_count = (total_elements // 2) + 1

    # Define the search range for binary search on values
    low = min(row[0] for row in matrix)
    high = max(row[-1] for row in matrix)

    def count_less_equal(mid_val: int) -> int:
        """Counts how many elements in the matrix are <= mid_val using binary search on each row."""
        count = 0
        for row in matrix:
            # Standard binary search (bisect_right) to find count of elements <= mid_val
            l, r = 0, cols - 1
            row_count = 0
            while l <= r:
                m = (l + r) // 2
                if row[m] <= mid_val:
                    row_count = m + 1
                    l = m + 1
                else:
                    r = m - 1
            count += row_count
        return count

    ans = low
    # Binary search on the range [low, high]
    while low <= high:
        mid = (low + high) // 2
        # If the number of elements <= mid is at least the required count for median
        if count_less_equal(mid) >= target_count:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1

    return ans
