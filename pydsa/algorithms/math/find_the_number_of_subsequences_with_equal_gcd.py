METADATA = {
    "id": 3336,
    "name": "Find the Number of Subsequences With Equal GCD",
    "slug": "find-the-number-of-subsequences-with-equal-gcd",
    "category": "Math",
    "aliases": [],
    "tags": ["math", "inclusion-exclusion", "number-theory"],
    "difficulty": "hard",
    "time_complexity": "O(max_val * log(max_val))",
    "space_complexity": "O(max_val)",
    "description": "Count the number of non-empty subsequences of a given array that have a specific greatest common divisor.",
}

def solve(nums: list[int], target: int) -> int:
    """
    Calculates the number of subsequences whose greatest common divisor (GCD) is exactly equal to target.

    The algorithm uses the principle of inclusion-exclusion. Instead of counting subsequences 
    with GCD exactly 'g' directly, we first count how many elements in the array are multiples 
    of 'g'. If there are 'count' such elements, there are (2^count - 1) non-empty subsequences 
    where every element is a multiple of 'g'. This means the GCD of such a subsequence 
    is at least 'g' (specifically, it is some multiple of 'g'). 
    We then subtract the counts for all multiples of 'g' (2g, 3g, ...) to isolate 
    the count for exactly 'g'.

    Args:
        nums: A list of integers.
        target: The target GCD value.

    Returns:
        The number of subsequences with GCD equal to target, modulo 10^9 + 7.

    Examples:
        >>> solve([1, 2, 3, 4, 5], 1)
        30
        >>> solve([2, 4, 6], 2)
        7
    """
    MOD = 1_000_000_007
    if not nums:
        return 0

    max_val = max(nums)
    # Frequency array to count occurrences of each number
    counts = [0] * (max_val + 1)
    for num in nums:
        counts[num] += 1

    # Precompute powers of 2 to avoid repeated exponentiation
    # pow2[i] = (2^i - 1) % MOD
    pow2 = [0] * (len(nums) + 1)
    current_pow = 1
    for i in range(1, len(nums) + 1):
        current_pow = (current_pow * 2) % MOD
        pow2[i] = (current_pow - 1 + MOD) % MOD

    # dp[i] will store the number of subsequences whose GCD is exactly i
    dp = [0] * (max_val + 1)

    # Iterate backwards from max_val to 1 to use inclusion-exclusion
    for i in range(max_val, 0, -1):
        # Count how many numbers in the input are multiples of i
        multiples_count = 0
        for multiple in range(i, max_val + 1, i):
            multiples_count += counts[multiple]

        if multiples_count == 0:
            continue

        # Total non-empty subsequences where all elements are multiples of i
        # The GCD of these subsequences is guaranteed to be a multiple of i
        total_subsequences_with_multiple_gcd = pow2[multiples_count]

        # Subtract subsequences whose GCD is a strict multiple of i (2i, 3i, ...)
        # to ensure the remaining count is for GCD exactly equal to i
        subtracted_sum = 0
        for multiple in range(2 * i, max_val + 1, i):
            subtracted_sum = (subtracted_sum + dp[multiple]) % MOD
        
        dp[i] = (total_subsequences_with_multiple_gcd - subtracted_sum + MOD) % MOD

    return dp[target] if target <= max_val else 0
