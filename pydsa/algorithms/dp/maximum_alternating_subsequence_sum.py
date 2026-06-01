METADATA = {
    "id": 1911,
    "name": "Maximum Alternating Subsequence Sum",
    "slug": "maximum-alternating-subsequence-sum",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dynamic_programming", "greedy"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the maximum alternating sum of a subsequence where elements at even indices are added and elements at odd indices are subtracted.",
}

def solve(nums: list[int]) -> int:
    """
    Calculates the maximum alternating subsequence sum using dynamic programming.

    The alternating sum is defined as: nums[i0] - nums[i1] + nums[i2] - nums[i3] ...
    where i0 < i1 < i2 < i3 ...

    Args:
        nums: A list of integers representing the sequence.

    Returns:
        The maximum possible alternating sum.

    Examples:
        >>> solve([4, 2, 5, 3])
        7
        >>> solve([6, 2, 1, 2, 4, 5])
        10
    """
    # max_even represents the maximum sum of an alternating subsequence 
    # where the last element added was at an even index (i.e., it was added).
    # max_odd represents the maximum sum where the last element was at an odd index (i.e., it was subtracted).
    
    # Initial state: 
    # We haven't picked any numbers, so max_even is 0.
    # max_odd is effectively 0 because we can't subtract before we add.
    max_even = 0
    max_odd = 0

    for num in nums:
        # To end with an 'even' index (addition), we either:
        # 1. Keep the previous max_even.
        # 2. Take the previous max_odd and add the current number.
        # 3. Start a new subsequence with the current number (handled by max_even = max(max_even, max_odd + num)).
        new_max_even = max(max_even, max_odd + num)

        # To end with an 'odd' index (subtraction), we either:
        # 1. Keep the previous max_odd.
        # 2. Take the previous max_even and subtract the current number.
        new_max_odd = max(max_odd, max_even - num)

        max_even = new_max_even
        max_odd = new_max_odd

    # The maximum sum will always end on an addition to maximize the value.
    return max_even
