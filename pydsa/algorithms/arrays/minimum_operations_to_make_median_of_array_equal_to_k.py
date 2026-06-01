METADATA = {
    "id": 3107,
    "name": "Minimum Operations to Make Median of Array Equal to K",
    "slug": "minimum-operations-to-make-median-of-array-equal-to-k",
    "category": "Greedy",
    "aliases": [],
    "tags": ["greedy", "sorting"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(1)",
    "description": "Find the minimum number of operations to make the median of an array equal to k, where an operation is incrementing or decrementing an element.",
}

def solve(nums: list[int], k: int) -> int:
    """
    Calculates the minimum number of operations to make the median of the array equal to k.
    
    The median of an array of size n is defined as the element at index n // 2 
    in the sorted version of the array. To make the median k, we must ensure 
    that nums[n // 2] == k and all elements to the right of the median are >= k.

    Args:
        nums: A list of integers.
        k: The target median value.

    Returns:
        The minimum number of operations (increments or decrements) required.

    Examples:
        >>> solve([1, 2, 3], 4)
        3
        >>> solve([1, 3], 3)
        0
        >>> solve([2, 1, 5, 6, 3], 5)
        2
    """
    nums.sort()
    n = len(nums)
    median_index = n // 2
    operations = 0

    # Step 1: Adjust the median element itself to be exactly k.
    # If nums[median_index] < k, we must increase it.
    # If nums[median_index] > k, we must decrease it.
    operations += abs(nums[median_index] - k)
    
    # We temporarily treat the median as k for the subsequent logic.
    current_median_val = k

    # Step 2: Ensure all elements to the right of the median are >= k.
    # Since the array is sorted, if an element to the right is smaller than k,
    # it violates the property that the median is the middle element of a sorted array.
    for i in range(median_index + 1, n):
        if nums[i] < current_median_val:
            # We must increase this element to at least k to maintain sorted order
            # relative to the new median.
            operations += (current_median_val - nums[i])
        else:
            # Since the array was sorted, if we encounter an element >= k,
            # all subsequent elements are also >= k.
            break

    return operations
