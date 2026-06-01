METADATA = {
    "id": 2401,
    "name": "Longest Nice Subarray",
    "slug": "longest-nice-subarray",
    "category": "Sliding Window",
    "aliases": [],
    "tags": ["sliding_window", "bit_manipulation"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the length of the longest subarray where every pair of elements has a bitwise AND equal to zero.",
}

def solve(nums: list[int]) -> int:
    """
    Finds the length of the longest subarray where all elements are 'nice'.
    A subarray is nice if the bitwise AND of every pair of elements in it is 0.
    This is equivalent to saying that for any bit position, at most one number 
    in the subarray has that bit set.

    Args:
        nums: A list of integers.

    Returns:
        The length of the longest nice subarray.

    Examples:
        >>> solve([1, 3])
        2
        >>> solve([1, 2, 4, 8])
        4
        >>> solve([1, 2, 3, 4])
        3
    """
    max_length = 0
    current_window_mask = 0
    left = 0

    for right in range(len(nums)):
        # If the current number shares any set bits with the existing window,
        # it violates the 'nice' property. We must shrink the window from the left.
        while (current_window_mask & nums[right]) != 0:
            # Remove the bits of the element at the 'left' pointer from the mask
            current_window_mask ^= nums[left]
            left += 1
        
        # Add the current number's bits to the mask and update the max length
        current_window_mask |= nums[right]
        max_length = max(max_length, right - left + 1)

    return max_length
