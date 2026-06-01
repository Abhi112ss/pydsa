METADATA = {
    "id": 1060,
    "name": "Missing Element in Sorted Array",
    "slug": "missing_element_in_sorted_array",
    "category": "Binary Search",
    "aliases": [],
    "tags": ["binary_search", "array"],
    "difficulty": "medium",
    "time_complexity": "O(log n)",
    "space_complexity": "O(1)",
    "description": "Find the k-th missing number in a sorted array where the sequence is expected to be consecutive.",
}

def solve(arr: list[int], k: int) -> int:
    """
    Finds the k-th missing number in a sorted array.

    The algorithm uses binary search to find the largest index 'low' such that 
    the number of missing elements before arr[low] is less than k.

    Args:
        arr: A sorted list of integers.
        k: The k-th missing number to find.

    Returns:
        The k-th missing integer.

    Examples:
        >>> solve([4, 7, 9, 10], 1)
        5
        >>> solve([4, 7, 9, 10], 3)
        8
        >>> solve([1, 2, 3, 4], 1)
        5
    """
    n = len(arr)

    def count_missing(index: int) -> int:
        """Helper to calculate how many numbers are missing up to arr[index]."""
        # The number of elements that should exist between arr[0] and arr[index]
        # is (arr[index] - arr[0] + 1). The actual count is (index + 1).
        return (arr[index] - arr[0]) - index

    # If k is greater than the total missing numbers in the entire array
    if k > count_missing(n - 1):
        return arr[n - 1] + (k - count_missing(n - 1))

    low = 0
    high = n - 1
    
    # Binary search to find the rightmost index where count_missing(index) < k
    while low < high:
        mid = (low + high + 1) // 2
        if count_missing(mid) < k:
            low = mid
        else:
            high = mid - 1

    # After the loop, 'low' is the largest index such that count_missing(low) < k.
    # The k-th missing number is between arr[low] and arr[low + 1].
    # Formula: arr[low] + (k - count_missing(low))
    return arr[low] + (k - count_missing(low))
