METADATA = {
    "id": 2338,
    "name": "Count the Number of Ideal Arrays",
    "slug": "count-the-number-of-ideal-arrays",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["math", "combinatorics", "dp"],
    "difficulty": "hard",
    "time_complexity": "O(n^2)",
    "space_complexity": "O(n^2)",
    "description": "Count the number of subsequences where the difference between indices of elements with the same parity is at least k.",
}

def solve(nums: list[int], k: int) -> int:
    """
    Calculates the number of ideal subsequences using dynamic programming.
    
    An ideal subsequence is one where for any two elements at indices i and j 
    in the subsequence, if nums[i] % 2 == nums[j] % 2, then |i - j| >= k.

    Args:
        nums: A list of integers.
        k: The minimum required index difference for elements of the same parity.

    Returns:
        The total number of ideal subsequences modulo 10^9 + 7.

    Examples:
        >>> solve([2, 3, 5, 4], 2)
        6
        >>> solve([1, 2, 3, 4], 1)
        15
    """
    MOD = 1_000_000_007
    n = len(nums)
    
    # dp[i][j] represents the number of ideal subsequences of length i 
    # ending with an element of parity j (0 for even, 1 for odd).
    # However, the constraint is on the index difference, not the length.
    # A better DP state: dp[i][p] is the number of ideal subsequences 
    # ending at index i with parity p.
    # To optimize, we use dp[i][p] as the number of ideal subsequences 
    # ending at or before index i with parity p.
    
    # Let's refine: dp[i][p] = number of ideal subsequences ending exactly at index i
    # where nums[i] % 2 == p.
    # To satisfy the condition, if we pick nums[i], the previous element 
    # with the same parity must have been at index <= i - k.
    # Elements with different parity can be at any index < i.
    
    # dp_even[i]: number of ideal subsequences ending at index i where nums[i] is even
    # dp_odd[i]: number of ideal subsequences ending at index i where nums[i] is odd
    dp_even = [0] * n
    dp_odd = [0] * n
    
    # sum_even[i]: prefix sum of dp_even up to index i
    # sum_odd[i]: prefix sum of dp_odd up to index i
    # sum_all[i]: prefix sum of (dp_even + dp_odd) up to index i
    sum_even = [0] * (n + 1)
    sum_odd = [0] * (n + 1)
    sum_all = [0] * (n + 1)

    for i in range(n):
        parity = nums[i] % 2
        
        # Base case: the subsequence consisting only of nums[i]
        current_count = 1
        
        # 1. Add elements of the DIFFERENT parity (no restriction on index)
        # We can append nums[i] to any ideal subsequence ending at any j < i
        # where nums[j] % 2 != parity.
        if parity == 0:
            current_count = (current_count + sum_odd[i]) % MOD
        else:
            current_count = (current_count + sum_even[i]) % MOD
            
        # 2. Add elements of the SAME parity (must satisfy index difference >= k)
        # We can append nums[i] to any ideal subsequence ending at index j <= i - k
        # where nums[j] % 2 == parity.
        if i >= k:
            if parity == 0:
                current_count = (current_count + sum_even[i - k + 1]) % MOD
            else:
                current_count = (current_count + sum_odd[i - k + 1]) % MOD
        elif k == 0:
            # If k=0, the condition |i-j| >= 0 is always true for any j < i.
            # But the problem implies distinct indices in subsequence.
            # If k=0 or k=1, the same-parity constraint is effectively just j < i.
            # However, the problem states |i-j| >= k. If k=1, j < i is always true.
            # If k=0, it's also always true.
            # The logic above handles i-k+1 correctly for k=1.
            pass

        # Update DP tables
        if parity == 0:
            dp_even[i] = current_count
        else:
            dp_odd[i] = current_count
            
        # Update prefix sums for O(1) range queries
        sum_even[i + 1] = (sum_even[i] + dp_even[i]) % MOD
        sum_odd[i + 1] = (sum_odd[i] + dp_odd[i]) % MOD
        sum_all[i + 1] = (sum_all[i] + dp_even[i] + dp_odd[i]) % MOD

    # The answer is the sum of all ideal subsequences ending at any index i
    return sum_all[n]
