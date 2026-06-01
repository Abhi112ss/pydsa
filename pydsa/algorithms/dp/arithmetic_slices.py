METADATA = {
    "id": 413,
    "name": "Arithmetic Slices",
    "slug": "arithmetic_slices",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dynamic_programming", "math", "array"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the total number of arithmetic subarrays of length at least 3.",
}

def solve(nums: list[int]) -> int:
    """
    Calculates the total number of arithmetic slices in the given array.
    
    An arithmetic slice is a subarray of at least length 3 where the 
    difference between consecutive elements is constant.

    Args:
        nums: A list of integers.

    Returns:
        The total count of arithmetic slices.

    Examples:
        >>> solve([1, 2, 3, 4])
        3
        >>> solve([1])
        0
        >>> solve([1, 3, 5, 7, 9])
        6
    """
    n = len(nums)
    if n < 3:
        return 0

    total_slices = 0
    current_streak_count = 0

    # Iterate from the third element to the end
    for i in range(2, n):
        # Check if the current element forms an arithmetic sequence with the previous two
        if nums[i] - nums[i - 1] == nums[i - 1] - nums[i - 2]:
            # If it does, the number of arithmetic slices ending at index i 
            # is 1 more than the number of slices ending at index i-1.
            # For example, in [1, 2, 3, 4], at index 2 (val 3), streak is 1 ([1,2,3]).
            # At index 3 (val 4), streak is 2 ([2,3,4] and [1,2,3,4]).
            current_streak_count += 1
            total_slices += current_streak_count
        else:
            # Reset the streak if the arithmetic property is broken
            current_streak_count = 0

    return total_slices
