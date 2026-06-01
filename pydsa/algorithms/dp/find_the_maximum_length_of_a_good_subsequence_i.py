METADATA = {
    "id": 3176,
    "name": "Find the Maximum Length of a Good Subsequence I",
    "slug": "find-the-maximum-length-of-a-good-subsequence-i",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dp", "arrays"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the maximum length of a subsequence where the absolute difference between adjacent elements is exactly 1.",
}

def solve(nums: list[int]) -> int:
    """
    Finds the maximum length of a 'good' subsequence where the absolute 
    difference between any two consecutive elements in the subsequence is exactly 1.

    Args:
        nums: A list of integers.

    Returns:
        The length of the longest good subsequence.

    Examples:
        >>> solve([1, 2, 3, 4, 5])
        5
        >>> solve([1, 3, 5, 7, 9])
        1
        >>> solve([1, 2, 1, 2, 1])
        5
    """
    # We use a hash map (dictionary) to store the length of the longest 
    # good subsequence ending with a specific number.
    # dp[x] = length of the longest good subsequence ending with value x.
    dp: dict[int, int] = {}
    max_length = 0

    for num in nums:
        # A good subsequence ending in 'num' can be formed by appending 'num'
        # to a good subsequence ending in 'num - 1' or 'num + 1'.
        # We take the maximum of these two possibilities.
        prev_minus = dp.get(num - 1, 0)
        prev_plus = dp.get(num + 1, 0)
        
        # The new length for the current number is 1 + max(neighbors).
        # If no neighbors exist, it starts a new subsequence of length 1.
        current_len = max(prev_minus, prev_plus) + 1
        
        # Update the DP table for the current number.
        # Note: If multiple instances of 'num' exist, we want the longest one.
        dp[num] = current_len
        
        # Track the global maximum length found so far.
        if current_len > max_length:
            max_length = current_len

    return max_length
