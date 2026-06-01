METADATA = {
    "id": 1708,
    "name": "Count Number of Complete Subarrays in an Array",
    "slug": "count-number-of-complete-subarrays",
    "category": "Array",
    "aliases": [],
    "tags": ["sliding_window", "array"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(k)",
    "description": "Find the number of subarrays that contain all the elements of the given array.",
}

def solve(nums: list[int], k: int) -> int:
    """
    Counts the number of subarrays that contain all k distinct elements.

    Args:
        nums: A list of integers.
        k: The number of distinct elements required to be in the subarray.

    Returns:
        The total count of subarrays containing all k distinct elements.

    Examples:
        >>> solve([1, 3, 2, 2, 2, 3, 1], 3)
        10
        >>> solve([1, 2, 1, 2, 3], 3)
        3
    """
    # The problem asks for subarrays containing all k distinct elements.
    # We use a sliding window [left, right] and a frequency map.
    
    n = len(nums)
    count = 0
    left = 0
    distinct_map = {}
    
    for right in range(n):
        # Expand the window by adding the current element
        current_val = nums[right]
        distinct_map[current_val] = distinct_map.get(current_val, 0) + 1
        
        # While the window contains all k distinct elements
        while len(distinct_map) == k:
            # If the current window [left, right] is valid, 
            # then all subarrays starting at 'left' and ending at 
            # any index from 'right' to 'n-1' are also valid.
            count += (n - right)
            
            # Shrink the window from the left to find the next smallest valid window
            left_val = nums[left]
            distinct_map[left_val] -= 1
            if distinct_map[left_val] == 0:
                del distinct_map[left_val]
            left += 1
            
    return count
