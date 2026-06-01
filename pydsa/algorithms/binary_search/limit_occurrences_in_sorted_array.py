METADATA = {
    "id": 3940,
    "name": "Limit Occurrences in Sorted Array",
    "slug": "limit_occurrences_in_sorted_array",
    "category": "Binary Search",
    "aliases": [],
    "tags": ["binary_search", "arrays", "sorted_array"],
    "difficulty": "medium",
    "time_complexity": "O(log n)",
    "space_complexity": "O(1)",
    "description": "Find the first index where an element's occurrence exceeds a given limit in a sorted array.",
}

def solve(nums: list[int], limit: int) -> int:
    """
    Finds the smallest index 'i' such that the number of occurrences of nums[i] 
    in the prefix nums[0...i] is greater than the specified limit.

    Since the array is sorted, all identical elements are contiguous. 
    The problem asks for the first index where the count of a specific value 
    reaches (limit + 1).

    Args:
        nums: A sorted list of integers.
        limit: The maximum allowed consecutive occurrences of any element.

    Returns:
        The smallest index 'i' where the count of nums[i] exceeds 'limit'.
        Returns -1 if no such index exists.

    Examples:
        >>> solve([1, 1, 2, 2, 2, 3], 2)
        4
        >>> solve([1, 2, 3], 1)
        -1
        >>> solve([1, 1, 1, 1], 1)
        2
    """
    n = len(nums)
    if n == 0:
        return -1

    # The problem asks for the first index 'i' such that nums[i] has appeared 
    # more than 'limit' times. In a sorted array, this is equivalent to 
    # finding the first index 'i' where nums[i] == nums[i - limit].
    
    # We can use binary search to find the smallest index 'i' in the range [limit, n-1]
    # that satisfies the condition nums[i] == nums[i - limit].
    
    low = limit
    high = n - 1
    result = -1

    while low <= high:
        mid = (low + high) // 2
        
        # Check if the element at 'mid' is the (limit + 1)-th occurrence 
        # of that value by looking back 'limit' steps.
        if nums[mid] == nums[mid - limit]:
            # This index satisfies the condition, but we want the *first* such index.
            # So we record this index and search the left half.
            result = mid
            high = mid - 1
        else:
            # If nums[mid] != nums[mid - limit], then the violation must occur 
            # at an index greater than 'mid'.
            low = mid + 1

    return result
