METADATA = {
    "id": 2173,
    "name": "Longest Winning Streak",
    "slug": "longest-winning-streak",
    "category": "Array",
    "aliases": [],
    "tags": ["array", "greedy", "simulation"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the length of the longest consecutive sequence of increasing elements in an array.",
}

def solve(nums: list[int]) -> int:
    """
    Finds the length of the longest winning streak in a sequence of numbers.
    A winning streak is defined as a sequence of consecutive elements where 
    each element is strictly greater than the previous one.

    Args:
        nums: A list of integers representing the sequence of scores/values.

    Returns:
        The length of the longest strictly increasing contiguous subarray.

    Examples:
        >>> solve([1, 2, 3, 2, 5])
        3
        >>> solve([1, 1, 1, 1])
        1
        >>> solve([5, 4, 3, 2, 1])
        1
    """
    if not nums:
        return 0

    max_streak = 1
    current_streak = 1

    # Iterate through the array starting from the second element
    for index in range(1, len(nums)):
        # Check if the current element continues the increasing trend
        if nums[index] > nums[index - 1]:
            current_streak += 1
        else:
            # Reset the streak if the trend is broken
            current_streak = 1
        
        # Update the global maximum streak found so far
        if current_streak > max_streak:
            max_streak = current_streak

    return max_streak
