METADATA = {
    "id": 3036,
    "name": "Number of Subarrays That Match a Pattern II",
    "slug": "number-of-subarrays-that-match-a-pattern-ii",
    "category": "Hash Table",
    "aliases": [],
    "tags": ["string_matching", "rolling_hash", "sliding_window"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Find the number of subarrays whose absolute differences between adjacent elements match a given pattern.",
}

def solve(nums: list[int], pattern: list[int]) -> int:
    """
    Counts the number of subarrays in nums such that the absolute differences 
    of adjacent elements match the given pattern.

    Args:
        nums: A list of integers.
        pattern: A list of integers representing the required absolute differences.

    Returns:
        The total count of subarrays that match the pattern.

    Examples:
        >>> solve([1, 4, 4, 4, 1], [3, 0, 0, 3])
        1
        >>> solve([1, 2, 3, 4, 5], [1, 1, 1, 1])
        1
    """
    n = len(nums)
    m = len(pattern)
    
    # The pattern length is m, which means the subarray must have m + 1 elements.
    # We transform the problem into matching the 'pattern' against the 
    # 'difference array' of nums.
    if n < m + 1:
        return 0

    # Precompute the difference array: diff[i] = abs(nums[i+1] - nums[i])
    # The length of diff will be n - 1.
    diffs = [abs(nums[i + 1] - nums[i]) for i in range(n - 1)]
    
    # We use Rabin-Karp rolling hash to find occurrences of 'pattern' in 'diffs'.
    # To avoid collisions, we use a large prime and a base.
    # Since pattern values can be up to 10^9, we use a large base.
    MOD = (1 << 61) - 1  # Mersenne prime for high collision resistance
    BASE = 10**9 + 7     # Large base
    
    target_hash = 0
    current_hash = 0
    power_m = 1  # This will store BASE^(m-1) % MOD
    
    # Calculate target hash and the initial window hash
    for i in range(m):
        target_hash = (target_hash * BASE + pattern[i]) % MOD
        current_hash = (current_hash * BASE + diffs[i]) % MOD
        if i < m - 1:
            power_m = (power_m * BASE) % MOD
            
    count = 0
    if current_hash == target_hash:
        count += 1
        
    # Slide the window across the diffs array
    # The diffs array has length n-1, pattern has length m.
    # Window size is m.
    for i in range(m, len(diffs)):
        # Remove the leftmost element of the previous window
        # current_hash = (current_hash - diffs[i-m] * BASE^(m-1)) * BASE + diffs[i]
        leading_val = (diffs[i - m] * power_m) % MOD
        current_hash = (current_hash - leading_val + MOD) % MOD
        current_hash = (current_hash * BASE + diffs[i]) % MOD
        
        if current_hash == target_hash:
            count += 1
            
    return count
