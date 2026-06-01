METADATA = {
    "id": 1218,
    "name": "Longest Arithmetic Subsequence of Given Difference",
    "slug": "longest_arithmetic_subsequence_of_given_difference",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dp", "hash_map"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Find the length of the longest subsequence where the difference between consecutive elements is equal to a given value.",
}

def solve(arr: list[int], difference: int) -> int:
    """
    Finds the length of the longest arithmetic subsequence with a specific difference.

    Args:
        arr: A list of integers.
        difference: The required difference between consecutive elements in the subsequence.

    Returns:
        The length of the longest arithmetic subsequence.

    Examples:
        >>> solve([1, 2, 3, 4], 1)
        4
        >>> solve([1, 5, 7, 8, 5, 3, 4, 2, 1], -2)
        3
    """
    # dp maps a value to the length of the longest arithmetic subsequence ending with that value.
    # dp[x] = length of subsequence ending at x with the given difference.
    dp: dict[int, int] = {}
    max_length = 0

    for num in arr:
        # The previous element in the arithmetic sequence would be (num - difference).
        # If that element exists in our dp map, we extend its sequence length.
        # Otherwise, we start a new sequence of length 1.
        prev_val = num - difference
        current_len = dp.get(prev_val, 0) + 1
        
        # Update the dp map for the current number.
        # Note: We overwrite because we are processing elements left-to-right,
        # ensuring we always use the most recent/optimal length for the current number.
        dp[num] = current_len
        
        # Track the global maximum length found so far.
        if current_len > max_length:
            max_length = current_len

    return max_length
