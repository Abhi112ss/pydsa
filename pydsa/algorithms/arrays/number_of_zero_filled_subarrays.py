METADATA = {
    "id": 2348,
    "name": "Number of Zero-Filled Subarrays",
    "slug": "number-of-zero-filled-subarrays",
    "category": "Array",
    "aliases": [],
    "tags": ["arrays", "math"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Count the total number of subarrays that consist entirely of zeros.",
}

def solve(nums: list[int]) -> int:
    """
    Calculates the total number of subarrays consisting only of zeros.

    The algorithm uses a single pass to identify contiguous blocks of zeros.
    For a block of length 'k', the number of zero-filled subarrays is the 
    sum of integers from 1 to k, which is (k * (k + 1)) // 2.
    Alternatively, we can increment a running count of current consecutive 
    zeros and add that count to the total at each step.

    Args:
        nums: A list of integers.

    Returns:
        The total number of zero-filled subarrays.

    Examples:
        >>> solve([1, 3, 0, 0, 2, 0, 0, 4])
        6
        >>> solve([0, 0, 0, 2, 0, 0])
        9
    """
    total_subarrays = 0
    current_zero_streak = 0

    for num in nums:
        if num == 0:
            # If we encounter a zero, increment the current streak.
            # Adding the current streak length to the total is equivalent 
            # to adding 1, then 2, ..., up to k for a block of size k.
            current_zero_streak += 1
            total_subarrays += current_zero_streak
        else:
            # If the number is not zero, the current streak of zeros is broken.
            current_zero_streak = 0

    return total_subarrays
