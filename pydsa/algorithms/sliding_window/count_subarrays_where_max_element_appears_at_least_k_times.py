METADATA = {
    "id": 2962,
    "name": "Count Subarrays Where Max Element Appears at Least K Times",
    "slug": "count-subarrays-where-max-element-appears-at-least-k-times",
    "category": "Array",
    "aliases": [],
    "tags": ["sliding_window", "two_pointer", "arrays"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Count the number of subarrays where the maximum element of the array appears at least k times.",
}

def solve(nums: list[int], k: int) -> int:
    """
    Counts the number of subarrays where the maximum element appears at least k times.

    Args:
        nums: A list of integers.
        k: The minimum number of times the maximum element must appear.

    Returns:
        The total count of valid subarrays.

    Examples:
        >>> solve([1, 3, 2, 3, 3], 2)
        6
        >>> solve([1, 1, 1, 1], 2)
        6
    """
    if not nums:
        return 0

    max_val = max(nums)
    total_subarrays = 0
    left = 0
    max_count = 0

    # Use a sliding window approach to find valid subarrays
    for right in range(len(nums)):
        # Increment count if current element is the target max element
        if nums[right] == max_val:
            max_count += 1

        # While the window contains at least k occurrences of max_val
        while max_count == k:
            # If the current window [left, right] is valid, then all subarrays
            # starting at 'left' and ending at any index from 'right' to 'len(nums)-1'
            # are also valid. However, it's easier to count how many valid subarrays
            # end at 'right' or start at 'left'.
            
            # A more intuitive way: if [left, right] is valid, then any subarray 
            # starting at index 0, 1, ..., left and ending at 'right' is valid.
            # But we want to count all subarrays. 
            # Let's use the logic: if [left, right] is the smallest valid window ending at 'right',
            # then there are (left + 1) valid subarrays ending at 'right'.
            
            # Wait, the logic above is for a fixed 'right'. Let's refine:
            # For every 'right', if we find the largest 'left' such that [left, right] 
            # contains k max elements, then all subarrays [0...left, right] are valid.
            
            # Let's stick to: if [left, right] is valid, then all subarrays starting 
            # at index 0...left and ending at 'right' are valid.
            # But we need to count them once.
            
            # Correct logic: For each 'right', find the largest 'left' such that 
            # the window [left, right] contains k max elements. 
            # The number of valid subarrays ending at 'right' is (left + 1).
            
            # To implement this, we shrink 'left' as much as possible while maintaining k.
            if nums[left] == max_val:
                max_count -= 1
            left += 1

        # After the while loop, 'left' is the first index such that [left, right] 
        # does NOT contain k max elements. Therefore, the number of valid 
        # subarrays ending at 'right' is exactly the value of 'left' 
        # before we incremented it in the last valid iteration.
        # Actually, the number of valid subarrays ending at 'right' is 'left' 
        # if we consider that 'left' was incremented until the condition failed.
        total_subarrays += left

    return total_subarrays
