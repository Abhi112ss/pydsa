METADATA = {
    "id": 3795,
    "name": "Minimum Subarray Length With Distinct Sum At Least K",
    "slug": "minimum_subarray_length_with_distinct_sum_at_least_k",
    "category": "Sliding Window",
    "aliases": [],
    "tags": ["sliding_window", "hash_map", "two_pointers"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Find the minimum length of a contiguous subarray such that the sum of its distinct elements is at least k.",
}

def solve(nums: list[int], k: int) -> int:
    """
    Finds the minimum length of a contiguous subarray where the sum of 
    distinct elements in that subarray is at least k.

    Args:
        nums: A list of integers.
        k: The target sum of distinct elements.

    Returns:
        The minimum length of such a subarray, or -1 if no such subarray exists.

    Examples:
        >>> solve([1, 2, 1, 3, 2], 5)
        2
        >>> solve([1, 1, 1], 2)
        -1
    """
    n = len(nums)
    min_length = float('inf')
    current_distinct_sum = 0
    # frequency_map tracks the count of each number in the current window
    frequency_map = {}
    left = 0

    for right in range(n):
        right_val = nums[right]
        
        # If this is a new element in the current window, add to distinct sum
        if frequency_map.get(right_val, 0) == 0:
            current_distinct_sum += right_val
        
        frequency_map[right_val] = frequency_map.get(right_val, 0) + 1

        # Shrink the window from the left as long as the condition is met
        while current_distinct_sum >= k:
            min_length = min(min_length, right - left + 1)
            
            left_val = nums[left]
            frequency_map[left_val] -= 1
            
            # If the element count drops to zero, it's no longer in the window
            if frequency_map[left_val] == 0:
                current_distinct_sum -= left_val
                del frequency_map[left_val]
            
            left += 1

    return int(min_length) if min_length != float('inf') else -1
