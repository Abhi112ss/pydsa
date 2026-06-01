METADATA = {
    "id": 1027,
    "name": "Longest Arithmetic Subsequence",
    "slug": "longest_arithmetic_subsequence",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dynamic_programming", "hash_map"],
    "difficulty": "medium",
    "time_complexity": "O(n^2)",
    "space_complexity": "O(n^2)",
    "description": "Find the length of the longest subsequence of a given array that forms an arithmetic progression.",
}

def solve(nums: list[int]) -> int:
    """
    Finds the length of the longest arithmetic subsequence in the given list.

    Args:
        nums: A list of integers.

    Returns:
        The length of the longest arithmetic subsequence.

    Examples:
        >>> solve([3, 6, 9, 12])
        4
        >>> solve([9, 4, 7, 2, 10])
        3
        >>> solve([20, 1, 15, 3, 10, 5, 8])
        4
    """
    n = len(nums)
    if n <= 2:
        return n

    # dp[i] is a dictionary where dp[i][diff] stores the length of the 
    # longest arithmetic subsequence ending at index i with common difference 'diff'.
    dp: list[dict[int, int]] = [{} for _ in range(n)]
    max_length = 0

    for i in range(n):
        for j in range(i):
            # Calculate the common difference between elements at index i and j
            diff = nums[i] - nums[j]
            
            # If a sequence with this difference already ended at index j,
            # extend it by 1. Otherwise, the sequence length is 2 (nums[j] and nums[i]).
            current_len = dp[j].get(diff, 1) + 1
            
            # Update the DP table for index i and the specific difference
            dp[i][diff] = current_len
            
            # Track the global maximum length found so far
            if current_len > max_length:
                max_length = current_len

    return max_length
