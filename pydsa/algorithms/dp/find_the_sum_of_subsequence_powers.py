METADATA = {
    "id": 3098,
    "name": "Find the Sum of Subsequence Powers",
    "slug": "find-the-sum-of-subsequence-powers",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dp", "math", "bit_manipulation"],
    "difficulty": "hard",
    "time_complexity": "O(n * 1024)",
    "space_complexity": "O(1024)",
    "description": "Calculate the sum of (subsequence_or ^ subsequence_and) for all non-empty subsequences modulo 10^9 + 7.",
}

def solve(nums: list[int], k: int) -> int:
    """
    Calculates the sum of (OR ^ AND) for all subsequences of length k.

    Args:
        nums: A list of integers.
        k: The required length of the subsequences.

    Returns:
        The sum of (bitwise OR ^ bitwise AND) for all subsequences of length k, 
        modulo 10^9 + 7.

    Examples:
        >>> solve([1, 2, 3], 2)
        2
    """
    MOD = 1_000_000_007
    # The maximum possible value for OR/AND is 1023 (since nums[i] < 1024)
    MAX_VAL = 1024
    
    # dp[count][current_or][current_and] would be too large.
    # However, we only need to track (count, current_or, current_and).
    # Since we need exactly k elements, we use dp[count][or_val][and_val].
    # Given the constraints and the nature of the problem, we can optimize.
    # Let's use dp[i][j] where i is the number of elements picked and j is the OR value.
    # But we need AND too. Let's use dp[count][or_val][and_val].
    # Wait, the constraints are n=1000, k=1000, but the values are small (0-1023).
    # A better DP state: dp[count][or_val][and_val] is too slow.
    # Let's use: dp[count][or_val][and_val] where count is elements picked.
    # Actually, we can use dp[count][or_val][and_val] but only for existing states.
    # Given the time limit and the bitwise nature, we use a dictionary or a 3D array.
    # Since we need to find sum of (OR ^ AND), we can track the counts of (or, and) pairs.
    
    # dp[count][or_val][and_val] = number of subsequences
    # To save space, we use dp[count][or_val][and_val] and iterate through nums.
    # But even better: dp[count][or_val][and_val] is still too big.
    # Let's observe: we only care about the sum of (or ^ and).
    # We can use dp[count][or_val][and_val] where count is 1 to k.
    
    # Optimization: Use a dictionary to store only reachable (or_val, and_val) for each count.
    # dp[count] = {(or_val, and_val): frequency}
    dp = [{} for _ in range(k + 1)]
    
    for num in nums:
        # Iterate backwards through counts to avoid using the same element twice for the same subsequence
        for count in range(k - 1, -1, -1):
            for (curr_or, curr_and), freq in dp[count].items():
                new_or = curr_or | num
                new_and = curr_and & num
                state = (new_or, new_and)
                dp[count + 1][state] = (dp[count + 1].get(state, 0) + freq) % MOD
            
            # Base case: starting a new subsequence with the current number
            if count == 0:
                state = (num, num)
                dp[1][state] = (dp[1].get(state, 0) + 1) % MOD
                
    # Note: The above dictionary approach might be slow in Python for n=1000.
    # Let's refine the DP. The problem asks for sum of (OR ^ AND).
    # Since we need exactly k elements, we can use dp[count][or_val][and_val].
    # However, the number of (or, and) pairs is at most 1024 * 1024, but many are unreachable.
    # Let's use a more efficient approach: dp[count][or_val][and_val]
    # Actually, the constraints on nums[i] are small (up to 1023).
    
    # Re-implementing with a more efficient structure:
    # dp[count][or_val][and_val]
    # Since we only need the previous count, we can use dp[or_val][and_val]
    
    # Let's use a 2D array for the current count to speed up access.
    # dp[count][or_val * 1024 + and_val]
    
    dp = [{} for _ in range(k + 1)]
    
    for num in nums:
        for c in range(k, 0, -1):
            # If we are adding 'num' to a subsequence of length c-1
            if c == 1:
                state = (num, num)
                dp[1][state] = (dp[1].get(state, 0) + 1) % MOD
            else:
                for (prev_or, prev_and), freq in dp[c-1].items():
                    new_or = prev_or | num
                    new_and = prev_and & num
                    state = (new_or, new_and)
                    dp[c][state] = (dp[c].get(state, 0) + freq) % MOD
                    
    total_sum = 0
    for (final_or, final_and), freq in dp[k].items():
        total_sum = (total_sum + (final_or ^ final_and) * freq) % MOD
        
    return total_sum

# The dictionary approach is still potentially O(N * K * 1024). 
# With N, K = 1000, this is too slow.
# Let's reconsider. The values are small.
# We can use the property that OR and AND are bitwise.
# We can use DP: dp[count][or_val][and_val]
# But we can also use the fact that we only need the sum of (OR ^ AND).
# (OR ^ AND) = (OR - AND) because AND is a subset of OR bits.
# Sum (OR ^ AND) = Sum (OR) - Sum (AND).
# To find Sum (OR), we can use inclusion-exclusion or bit-by-bit.
# For a specific bit, it is 1 in OR if at least one element has that bit.
# For a specific bit, it is 1 in AND if all elements have that bit.
# But we need the sum of (OR ^ AND) for subsequences of length EXACTLY k.
# This is not simply Sum(OR) - Sum(AND) because the OR and AND are tied to the same subsequence.
# Actually, (OR ^ AND) is indeed (OR - AND) because AND bits are always a subset of OR bits.
# So Sum (OR ^ AND) = Sum (OR) - Sum (AND).
# Let's verify: if OR = 101 (5) and AND = 001 (1), OR ^ AND = 100 (4). 5 - 1 = 4. Correct.
# So we need:
# 1. Sum of OR of all subsequences of length k.
# 2. Sum of AND of all subsequences of length k.

def solve(nums: list[int], k: int) -> int:
    """
    Calculates the sum of (OR ^ AND) for all subsequences of length k.
    Uses the property: (OR ^ AND) = (OR - AND) for bitwise operations where AND is a subset of OR.
    Sum (OR ^ AND) = Sum (OR) - Sum (AND).
    
    Args:
        nums: A list of integers.
        k: The required length of the subsequences.

    Returns:
        The sum of (bitwise OR ^ bitwise AND) for all subsequences of length k, 
        modulo 10^9 + 7.
    """
    MOD = 1_000_000_007
    n = len(nums)
    
    # Precompute combinations C(n, k) mod MOD
    # Since n is up to 1000, we can use Pascal's triangle
    C = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        C[i][0] = 1
        for j in range(1, i + 1):
            C[i][j] = (C[i-1][j-1] + C[i-1][j]) % MOD

    # Sum of OR:
    # For each bit 'b', count how many subsequences of length k have bit 'b' set in their OR.
    # A subsequence has bit 'b' set in OR if NOT all elements have bit 'b' as 0.
    # Total subsequences of length k: C(n, k)
    # Subsequences where bit 'b' is 0 in OR: C(count_of_elements_with_bit_b_as_0, k)
    # Subsequences where bit 'b' is 1 in OR: C(n, k) - C(count_of_elements_with_bit_b_as_0, k)
    
    sum_or = 0
    sum_and = 0
    
    for b in range(10):  # nums[i] < 1024, so 10 bits are enough
        bit_val = 1 << b
        count_with_bit = 0
        count_without_bit = 0
        for x in nums:
            if x & bit_val:
                count_with_bit += 1
            else:
                count_without_bit += 1
        
        # OR contribution
        # Ways to have bit 'b' in OR = Total ways - ways where bit 'b' is 0 in all k elements
        ways_or = (C[n][k] - (C[count_without_bit][k] if count_without_bit >= k else 0)) % MOD
        sum_or = (sum_or + ways_or * bit_val) % MOD
        
        # AND contribution
        # Ways to have bit 'b' in AND = ways where bit 'b' is 1 in all k elements
        ways_and = C[count_with_bit][k] if count_with_bit >= k else 0
        sum_and = (sum_and + ways_and * bit_val) % MOD
        
    return (sum_or - sum_and + MOD) % MOD

# Wait, the logic (OR ^ AND) = (OR - AND) is only true if AND is a subset of OR.
# In bitwise operations, (A & B) is always a subset of A and a subset of B.
# Therefore, (A | B) always contains all bits of (A & B).
# So (A | B) ^ (A & B) is indeed (A | B) - (A & B).
# However, the problem is about the OR and AND of the *entire* subsequence.
# Let OR_sub = bitwise OR of subsequence.
# Let AND_sub = bitwise AND of subsequence.
# Is AND_sub a subset of OR_sub? 
# Yes, because if a bit is 1 in AND_sub, it must be 1 in every element of the subsequence.
# If it is 1 in every element, it must be 1 in the OR_sub.
# Thus, (OR_sub ^ AND_sub) == (OR_sub - AND_sub).
# The logic holds.

# Final check on complexity:
# Precomputing C(n, k): O(n^2)
# Iterating bits: 10 * O(n)
# Total: O(n^2), which is well within limits for n=1000.
