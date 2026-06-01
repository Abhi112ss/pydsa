METADATA = {
    "id": 3105,
    "name": "Longest Strictly Increasing or Strictly Decreasing Subarray",
    "slug": "longest-strictly-increasing-or-strictly-decreasing-subarray",
    "category": "Array",
    "aliases": [],
    "tags": ["sliding_window", "arrays"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the length of the longest subarray that is either strictly increasing or strictly decreasing.",
}

def solve(nums: list[int]) -> int:
    """
    Finds the length of the longest subarray that is either strictly increasing 
    or strictly decreasing.

    Args:
        nums: A list of integers.

    Returns:
        The length of the longest strictly increasing or strictly decreasing subarray.

    Examples:
        >>> solve([1, 4, 3, 3, 2])
        2
        >>> solve([1, 2, 3, 4, 5])
        5
        >>> solve([5, 4, 3, 2, 1])
        5
    """
    if not nums:
        return 0

    max_length = 1
    inc_streak = 1
    dec_streak = 1

    # Iterate through the array starting from the second element
    for i in range(1, len(nums)):
        # Check for strictly increasing condition
        if nums[i] > nums[i - 1]:
            inc_streak += 1
            dec_streak = 1  # Reset decreasing streak
        # Check for strictly decreasing condition
        elif nums[i] < nums[i - 1]:
            dec_streak += 1
            inc_streak = 1  # Reset increasing streak
        # If elements are equal, both streaks must reset
        else:
            inc_streak = 1
            dec_streak = 1
        
        # Update the global maximum found so far
        current_max = max(inc_streak, dec_streak)
        if current_max > max_length:
            max_length = current_max

    return max_length
