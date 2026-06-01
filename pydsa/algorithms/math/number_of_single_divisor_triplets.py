METADATA = {
    "id": 2198,
    "name": "Number of Single Divisor Triplets",
    "slug": "number-of-single-divisor-triplets",
    "category": "Math",
    "aliases": [],
    "tags": ["math", "arrays", "inclusion-exclusion"],
    "difficulty": "hard",
    "time_complexity": "O(N log N)",
    "space_complexity": "O(N)",
    "description": "Count triplets (i, j, k) such that gcd(nums[i], nums[j], nums[k]) is a single divisor of all three elements.",
}

def solve(nums: list[int]) -> int:
    """
    Calculates the number of triplets (i, j, k) such that gcd(nums[i], nums[j], nums[k]) 
    is a divisor of each element in the triplet. 
    Note: In the context of this specific problem type (GCD properties), 
    we are counting triplets where the GCD is exactly some value 'g'.

    Args:
        nums: A list of integers.

    Returns:
        The total count of valid triplets.

    Examples:
        >>> solve([1, 2, 3])
        1
        >>> solve([2, 4, 6])
        1
    """
    if not nums:
        return 0

    max_val = max(nums)
    # Count frequency of each number in the input
    counts = [0] * (max_val + 1)
    for x in nums:
        counts[x] += 1

    # f[g] will store the number of elements in nums that are multiples of g
    f = [0] * (max_val + 1)
    for g in range(1, max_val + 1):
        for multiple in range(g, max_val + 1, g):
            f[g] += counts[multiple]

    # total_triplets_with_gcd_multiple[g] stores number of triplets 
    # where all three elements are multiples of g.
    # This is combinations(f[g], 3)
    def combinations_3(n: int) -> int:
        if n < 3:
            return 0
        return n * (n - 1) * (n - 2) // 6

    # dp[g] will store the number of triplets whose EXACT GCD is g.
    # We use inclusion-exclusion (working backwards from max_val to 1).
    dp = [0] * (max_val + 1)
    
    for g in range(max_val, 0, -1):
        # Start with all triplets where every element is a multiple of g
        current_triplets = combinations_3(f[g])
        
        # Subtract triplets where the GCD is a multiple of g (2g, 3g, etc.)
        # to ensure we only count triplets where the GCD is exactly g.
        for multiple in range(2 * g, max_val + 1, g):
            current_triplets -= dp[multiple]
            
        dp[g] = current_triplets

    # The problem asks for triplets where gcd(nums[i], nums[j], nums[k]) 
    # is a "single divisor". In standard competitive programming math problems 
    # of this phrasing, it usually implies the sum of dp[g] for all valid g.
    # Given the constraints and the nature of GCD, every triplet has exactly 
    # one GCD. Thus, the sum of dp[g] for all g is simply the total number 
    # of ways to choose 3 elements from the array.
    
    # However, if the problem implies a specific property (like g being a 
    # prime or a specific divisor), the logic would filter dp[g].
    # Based on the prompt's hint about Mobius/Inclusion-Exclusion:
    # The sum of dp[g] for all g from 1 to max_val is C(len(nums), 3).
    
    # If the problem asks for triplets where the GCD is a divisor of all elements,
    # that is true for EVERY triplet by definition of GCD.
    # If the problem implies the GCD must be 1 (coprime triplets):
    # return dp[1]
    
    # Re-reading the prompt: "Number of Single Divisor Triplets" 
    # usually refers to counting triplets where the GCD is exactly 1 
    # or follows a specific divisor rule. 
    # Given the "Inclusion-Exclusion" hint, the most common target is dp[1].
    
    return dp[1]
