METADATA = {
    "id": 2145,
    "name": "Count the Hidden Sequences",
    "slug": "count-the-hidden-sequences",
    "category": "Math",
    "aliases": [],
    "tags": ["math", "combinatorics"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Count the number of subsequences where every element appears at least as many times as its value.",
}

def solve(nums: list[int]) -> int:
    """
    Counts the number of subsequences where each element x appears at least x times.

    The problem asks for the number of subsequences such that for every element x 
    present in the subsequence, its frequency is >= x. 
    
    Algorithm:
    1. Count the frequency of each number in the input array.
    2. For each unique number 'x' with frequency 'f':
       - If f < x, this number cannot be part of any valid subsequence (it would violate the rule).
       - If f >= x, we can choose to include 'x' in our subsequence.
       - To satisfy the condition, we must pick at least 'x' occurrences of 'x'.
       - The number of ways to pick at least 'x' elements from 'f' available elements is:
         Sum_{i=x}^{f} (f choose i).
       - Alternatively, using the property of combinations: 
         Total ways to pick any number of 'x's is 2^f.
         Ways to pick fewer than 'x' elements is Sum_{i=0}^{x-1} (f choose i).
         However, the problem implies that if we pick 'x', it must appear >= x times. 
         If we pick 0 'x's, it doesn't violate the rule for 'x' because 'x' isn't in the subsequence.
         So for each number 'x', we have (Ways to pick >= x elements) + (1 way to pick zero elements).
    3. Multiply the possibilities for all unique numbers together.

    Args:
        nums: A list of integers.

    Returns:
        The total number of valid subsequences modulo 10^9 + 7.

    Examples:
        >>> solve([1, 2, 2])
        2
        >>> solve([1, 1, 2, 2, 2])
        4
    """
    MOD = 10**9 + 7
    
    # Step 1: Count frequencies of each number
    counts = {}
    for num in nums:
        counts[num] = counts.get(num, 0) + 1
        
    # Precompute factorials and inverse factorials for combinations if needed,
    # but since we only need combinations for specific f and x, 
    # and the sum of f is N, we can use a more direct approach.
    # Given N is up to 10^5, we use a standard combination approach.
    
    # To handle large N, we precompute factorials for O(1) combinations
    max_f = max(counts.values()) if counts else 0
    fact = [1] * (max_f + 1)
    inv_fact = [1] * (max_f + 1)
    
    for i in range(1, max_f + 1):
        fact[i] = (fact[i - 1] * i) % MOD
        
    inv_fact[max_f] = pow(fact[max_f], MOD - 2, MOD)
    for i in range(max_f - 1, -1, -1):
        inv_fact[i] = (inv_fact[i + 1] * (i + 1)) % MOD

    def nCr(n: int, r: int) -> int:
        if r < 0 or r > n:
            return 0
        num = fact[n]
        den = (inv_fact[r] * inv_fact[n - r]) % MOD
        return (num * den) % MOD

    total_ways = 1
    
    # Step 2: Calculate ways for each unique number
    for x, f in counts.items():
        if f < x:
            # If we can't even pick x elements, we can only pick 0 elements.
            # This contributes a multiplier of 1 (the "pick zero" option).
            ways_for_x = 1
        else:
            # Ways to pick at least x elements: Sum_{i=x}^{f} (f choose i)
            # Plus 1 way to pick zero elements.
            # Total ways = 1 + sum(nCr(f, i) for i in range(x, f + 1))
            current_sum = 0
            for i in range(x, f + 1):
                current_sum = (current_sum + nCr(f, i)) % MOD
            ways_for_x = (1 + current_sum) % MOD
            
        total_ways = (total_ways * ways_for_x) % MOD
        
    # Subtract 1 to exclude the empty subsequence
    return (total_ways - 1 + MOD) % MOD
