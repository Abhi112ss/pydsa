METADATA = {
    "id": 3878,
    "name": "Count Good Subarrays",
    "slug": "count_good_subarrays",
    "category": "Sliding Window",
    "aliases": [],
    "tags": ["sliding_window", "hash_map", "two_pointers"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Count the number of subarrays that satisfy a specific frequency-based 'good' property using a sliding window.",
}

def solve(nums: list[int], k: int) -> int:
    """
    Counts the number of subarrays where the frequency of at least one element 
    is at least k.

    Note: The problem description provided in the prompt implies a standard 
    'at least k' frequency condition often found in sliding window problems.
    If the 'good' property is defined as 'at least one element appears k times',
    we use a sliding window to find the smallest window ending at 'right' 
    that satisfies the condition.

    Args:
        nums: A list of integers.
        k: The threshold frequency.

    Returns:
        The total count of 'good' subarrays.

    Examples:
        >>> solve([1, 2, 1, 2, 1], 2)
        6
        # Good subarrays: [1,2,1], [2,1,2], [1,2,1], [1,2,1,2], [2,1,2,1], [1,2,1,2,1]
        # Wait, if k=2, [1,2,1] is good. [1,2] is not.
        # Subarrays with at least one element appearing 2 times:
        # [1,2,1], [1,2,1,2], [1,2,1,2,1], [2,1,2], [2,1,2,1], [1,2,1] (from index 2)
    """
    n = len(nums)
    if k <= 1:
        # If k is 1, every non-empty subarray is good.
        # Total subarrays = n * (n + 1) // 2
        return n * (n + 1) // 2

    count = 0
    left = 0
    frequency_map = {}
    
    # We track how many elements currently satisfy the 'at least k' condition
    elements_meeting_k = 0

    for right in range(n):
        val = nums[right]
        frequency_map[val] = frequency_map.get(val, 0) + 1
        
        # If this element just reached the threshold k, increment our tracker
        if frequency_map[val] == k:
            elements_meeting_k += 1
            
        # While the current window [left, right] is 'good'
        while elements_meeting_k > 0:
            # If the window [left, right] is good, then all windows 
            # starting at 'left' and ending at any index from 'right' to 'n-1'
            # are also good. However, the standard sliding window approach 
            # for "count subarrays" is: if [left, right] is good, 
            # then [left, right...n-1] are all good.
            # To avoid double counting and use O(n), we add (n - right) 
            # to the total and move 'left' to find the next minimal window.
            
            count += (n - right)
            
            # Shrink the window from the left
            left_val = nums[left]
            if frequency_map[left_val] == k:
                elements_meeting_k -= 1
            frequency_map[left_val] -= 1
            left += 1
            
    return count
