METADATA = {
    "id": 3202,
    "name": "Find the Maximum Length of Valid Subsequence II",
    "slug": "find-the-maximum-length-of-valid-subsequence-ii",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dynamic_programming", "math"],
    "difficulty": "medium",
    "time_complexity": "O(n * k)",
    "space_complexity": "O(k^2)",
    "description": "Find the maximum length of a subsequence where the sum of every two adjacent elements has the same remainder modulo k.",
}

def solve(nums: list[int], k: int) -> int:
    """
    Finds the maximum length of a subsequence where (sub[i] + sub[i+1]) % k is constant.

    Args:
        nums: A list of integers.
        k: The modulus value.

    Returns:
        The maximum length of a valid subsequence.

    Examples:
        >>> solve([1, 2, 3, 4, 5], 2)
        5
        >>> solve([1, 4, 2, 3, 1, 4], 3)
        4
    """
    # dp[rem][last_val_mod] stores the length of the longest subsequence 
    # where (a + b) % k == rem and the last element in the subsequence % k == last_val_mod.
    # Since we only care about the remainder of the elements, we use a 2D array.
    # dp[target_remainder][last_element_remainder]
    dp = [[0] * k for _ in range(k)]
    max_length = 0

    for num in nums:
        current_rem = num % k
        
        # For every possible target remainder 'r' that (x + y) % k could be:
        for target_rem in range(k):
            # If (prev_rem + current_rem) % k == target_rem,
            # then prev_rem = (target_rem - current_rem) % k.
            prev_rem = (target_rem - current_rem) % k
            
            # Update the DP state: the length ending in current_rem for this target_rem
            # is the length of the subsequence ending in prev_rem plus one.
            dp[target_rem][current_rem] = dp[target_rem][prev_rem] + 1
            
            # Track the global maximum length found so far.
            if dp[target_rem][current_rem] > max_length:
                max_length = dp[target_rem][current_rem]

    return max_length
