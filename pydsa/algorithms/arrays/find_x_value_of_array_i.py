METADATA = {
    "id": 3524,
    "name": "Find X Value of Array I",
    "slug": "find_x_value_of_array_i",
    "category": "Array",
    "aliases": [],
    "tags": ["counting", "arrays", "sorting"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(1)",
    "description": "Find the largest integer x such that the number of elements in the array strictly greater than x is equal to x.",
}

def solve(nums: list[int]) -> int:
    """
    Finds the largest integer x such that the number of elements in the array 
    strictly greater than x is equal to x.

    Args:
        nums: A list of integers.

    Returns:
        The largest integer x satisfying the condition, or -1 if no such x exists.

    Examples:
        >>> solve([1, 2, 3])
        1
        >>> solve([0, 0, 0])
        -1
        >>> solve([1, 1, 1])
        0
    """
    # Sort the array to easily count elements greater than a specific value
    # Sorting allows us to use the index to determine how many elements are to the right
    nums.sort()
    n = len(nums)

    # We want to find the largest x. 
    # Since x is the count of elements > x, x can range from 0 to n.
    # We iterate through possible values of x.
    # However, a more efficient way is to check the condition based on the sorted array.
    # For a sorted array, if we pick an index i, the number of elements strictly 
    # greater than nums[i] is (n - 1 - i) if nums[i] < nums[i+1].
    
    # Let's check every possible value of x from n down to 0.
    # The condition is: count(nums[i] > x) == x.
    # Note that x must be an integer.
    
    # We can iterate through all possible counts 'count' from n down to 0.
    # If 'count' elements are strictly greater than 'count', then x = count is a candidate.
    # For 'count' elements to be strictly greater than 'count', 
    # the element at index (n - 1 - count) must be less than or equal to 'count',
    # AND the element at index (n - count) must be strictly greater than 'count'.
    
    # Actually, a simpler approach:
    # For any x, the number of elements > x is the number of elements in the suffix.
    # Let's test all possible values of x that could be valid.
    # The possible values of x are 0, 1, ..., n.
    
    for x in range(n, -1, -1):
        # Count how many elements are strictly greater than x
        # Since the array is sorted, we can use binary search or a simple pointer.
        # But since we are iterating x, we can just find the first index i where nums[i] > x.
        
        # Binary search for the first index i such that nums[i] > x
        import bisect
        idx = bisect.bisect_right(nums, x)
        count_greater = n - idx
        
        if count_greater == x:
            return x
            
    return -1
