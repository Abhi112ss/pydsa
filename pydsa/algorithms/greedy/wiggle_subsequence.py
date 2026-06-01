METADATA = {
    "id": 376,
    "name": "Wiggle Subsequence",
    "slug": "wiggle-subsequence",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["greedy", "dynamic_programming"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the length of the longest subsequence where the differences between successive elements strictly alternate between positive and negative.",
}

def solve(nums: list[int]) -> int:
    """
    Finds the length of the longest wiggle subsequence using a greedy approach.
    
    A wiggle subsequence is a subsequence where the differences between adjacent 
    elements strictly alternate between positive and negative.

    Args:
        nums: A list of integers.

    Returns:
        The length of the longest wiggle subsequence.

    Examples:
        >>> solve([1, 7, 4, 9, 2, 5])
        6
        >>> solve([1, 17, 5, 10, 13, 15, 10, 5, 16, 8])
        7
        >>> solve([1, 2, 3, 4, 5, 6, 7, 8, 9])
        2
    """
    n = len(nums)
    if n < 2:
        return n

    # prev_diff tracks the direction of the last wiggle (positive or negative)
    # 0 indicates we haven't established a direction yet.
    prev_diff = 0
    # We always count the first element.
    count = 1

    for i in range(1, n):
        current_diff = nums[i] - nums[i - 1]

        # Check if we found a new peak or valley.
        # A peak/valley occurs if the current direction is different from the previous direction.
        # We must also ensure current_diff is not 0 to avoid counting plateaus.
        if (current_diff > 0 and prev_diff <= 0) or (current_diff < 0 and prev_diff >= 0):
            count += 1
            # Update prev_diff to the current direction to look for the next extremum.
            prev_diff = current_diff

    return count
