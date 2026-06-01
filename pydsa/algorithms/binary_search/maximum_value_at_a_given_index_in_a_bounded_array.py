METADATA = {
    "id": 1802,
    "name": "Maximum Value at a Given Index in a Bounded Array",
    "slug": "maximum-value-at-a-given-index-in-a-bounded-array",
    "category": "Binary Search",
    "aliases": [],
    "tags": ["binary_search", "math"],
    "difficulty": "medium",
    "time_complexity": "O(log(max_val))",
    "space_complexity": "O(1)",
    "description": "Find the maximum possible value at a specific index in an array of size n where each element is at least 1 and the total sum is at most max_sum.",
}

def solve(n: int, index: int, max_sum: int) -> int:
    """
    Finds the maximum possible value at a given index in a bounded array.

    The array must satisfy:
    1. array[i] >= 1 for all i.
    2. sum(array) <= max_sum.
    3. |array[i] - array[i-1]| <= 1 for all i > 0.

    Args:
        n: The size of the array.
        index: The target index to maximize.
        max_sum: The maximum allowed sum of the array elements.

    Returns:
        The maximum possible value at the given index.

    Examples:
        >>> solve(4, 1, 6)
        2
        >>> solve(3, 2, 10)
        4
    """

    def calculate_sum(peak_value: int, count: int) -> int:
        """
        Calculates the minimum sum of a sequence of 'count' elements 
        that increases/decreases by at most 1, ending at 'peak_value'.
        
        Example: if peak_value=4 and count=3, sequence is [2, 3, 4].
        """
        if count <= 0:
            return 0
        
        # If the count is smaller than the peak value, the sequence 
        # will be [peak-count+1, ..., peak].
        # If count is larger, the sequence will be [1, 1, ..., 1, 2, ..., peak].
        
        # Case 1: The sequence reaches 1 before the count is exhausted.
        if peak_value >= count:
            # Arithmetic series: sum of [peak - count + 1, ..., peak]
            # Formula: (first + last) * num_elements / 2
            first_term = peak_value - count + 1
            return (first_term + peak_value) * count // 2
        else:
            # Case 2: The sequence hits 1 and stays 1 for the remaining elements.
            # Sum of [1, ..., peak] + (count - peak) * 1
            sum_to_peak = (1 + peak_value) * peak_value // 2
            remaining_ones = count - peak_value
            return sum_to_peak + remaining_ones

    def get_total_sum(peak_value: int) -> int:
        """Calculates the minimum total sum for a given peak value at 'index'."""
        # Sum of elements to the left of index (including index)
        # The sequence is: [..., peak-2, peak-1, peak]
        left_sum = calculate_sum(peak_value, index + 1)
        
        # Sum of elements to the right of index
        # The sequence is: [peak-1, peak-2, ..., 1, 1, ...]
        # The number of elements to the right is (n - 1 - index)
        right_count = n - 1 - index
        right_sum = calculate_sum(peak_value - 1, right_count)
        
        return left_sum + right_sum

    # Binary search for the maximum possible peak_value
    # Minimum possible value is 1, maximum is max_sum (though practically much less)
    low = 1
    high = max_sum
    ans = 1

    while low <= high:
        mid = (low + high) // 2
        if get_total_sum(mid) <= max_sum:
            ans = mid
            low = mid + 1
        else:
            high = mid - 1

    return ans
