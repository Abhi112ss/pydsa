METADATA = {
    "id": 2572,
    "name": "Count the Number of Square-Free Subsets",
    "slug": "count-the-number-of-square-free-subsets",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dp", "math", "bit_manipulation"],
    "difficulty": "hard",
    "time_complexity": "O(n * 2^k) where k is the number of primes up to 50",
    "space_complexity": "O(2^k)",
    "description": "Count the number of subsets whose product is square-free using bitmasking to track prime factors.",
}

def solve(nums: list[int]) -> int:
    """
    Counts the number of non-empty subsets of nums such that the product of 
    elements in each subset is square-free.

    A number is square-free if its prime factorization contains no repeated primes.
    Since the maximum value in nums is 50, we only care about primes up to 50.

    Args:
        nums: A list of integers where 1 <= nums[i] <= 50.

    Returns:
        The number of square-free subsets modulo 10^9 + 7.

    Examples:
        >>> solve([1, 2, 2, 3])
        7
        >>> solve([1, 1, 1])
        7
    """
    MOD = 10**9 + 7
    PRIMES = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
    num_primes = len(PRIMES)
    
    # Pre-calculate the bitmask for each number from 1 to 50.
    # If a number is not square-free (e.g., 4, 8, 9, 12...), we mark it as -1.
    val_to_mask = {}
    for i in range(1, 51):
        mask = 0
        temp = i
        is_square_free = True
        for idx, p in enumerate(PRIMES):
            if temp % (p * p) == 0:
                is_square_free = False
                break
            if temp % p == 0:
                mask |= (1 << idx)
        
        if is_square_free:
            val_to_mask[i] = mask
        else:
            val_to_mask[i] = -1

    # Count occurrences of each number in the input.
    counts = {}
    for x in nums:
        counts[x] = counts.get(x, 0) + 1

    # dp[mask] stores the number of ways to form a square-free product 
    # using a subset of numbers processed so far, where 'mask' represents 
    # the set of prime factors used.
    dp = [0] * (1 << num_primes)
    dp[0] = 1

    # Handle the number 1 separately. 
    # Any subset of 1s is square-free. If there are 'c' ones, 
    # there are 2^c - 1 non-empty subsets of 1s.
    # However, it's easier to treat 1 as a special case in the DP or 
    # multiply the final result by 2^(count of 1s).
    ones_count = counts.get(1, 0)
    
    # Iterate through all possible values from 2 to 50.
    for val in range(2, 51):
        if val not in counts or val_to_mask[val] == -1:
            continue
        
        mask_val = val_to_mask[val]
        count_val = counts[val]
        
        # We iterate backwards through the DP table to avoid using the 
        # same number multiple times in the same subset (standard 0/1 knapsack logic).
        # But since we can have multiple instances of the same 'val', 
        # and 'val' is square-free, we can only pick AT MOST one instance 
        # of 'val' to keep the product square-free.
        # Wait, if we pick two 2s, the product is 4 (not square-free).
        # So for any val > 1, we can pick either 0 or 1 instance of it.
        # If we have 'count_val' instances, there are 'count_val' ways to pick 1 instance.
        for current_mask in range((1 << num_primes) - 1, -1, -1):
            if (current_mask & mask_val) == 0:
                # If the prime factors of 'val' don't overlap with 'current_mask',
                # we can add 'val' to the subsets represented by 'current_mask'.
                new_mask = current_mask | mask_val
                dp[new_mask] = (dp[new_mask] + dp[current_mask] * count_val) % MOD

    # Sum all possible square-free combinations.
    total_subsets = sum(dp) % MOD
    
    # Account for the number 1. 
    # Each existing square-free subset can be combined with any of the 2^ones_count 
    # subsets of 1s.
    # The formula: (Total subsets from 2-50) * (2^ones_count)
    # But we must subtract 1 at the very end to exclude the empty subset.
    # However, the DP already includes the "empty" subset (dp[0]=1).
    # So: (Sum of dp) * 2^ones_count - 1
    multiplier = pow(2, ones_count, MOD)
    result = (total_subsets * multiplier - 1) % MOD
    
    return result
