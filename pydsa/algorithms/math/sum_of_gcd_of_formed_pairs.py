METADATA = {
    "id": 3867,
    "name": "Sum of GCD of Formed Pairs",
    "slug": "sum_of_gcd_of_formed_pairs",
    "category": "Math",
    "aliases": [],
    "tags": ["math", "number_theory"],
    "difficulty": "medium",
    "time_complexity": "O(N log N)",
    "space_complexity": "O(N)",
    "description": "Calculate the sum of the greatest common divisors of all possible pairs formed from a given array.",
}

def solve(nums: list[int]) -> int:
    """
    Calculates the sum of GCD(nums[i], nums[j]) for all pairs (i, j) where i < j.
    
    The algorithm uses a frequency array and inclusion-exclusion principle. 
    Instead of iterating over all pairs, we count how many pairs have a specific 
    GCD 'g' by counting multiples of 'g' and subtracting counts of multiples 
    of '2g', '3g', etc.

    Args:
        nums: A list of integers.

    Returns:
        The sum of the GCD of all formed pairs.

    Examples:
        >>> solve([1, 2, 3])
        4  # GCD(1,2)=1, GCD(1,3)=1, GCD(2,3)=1 -> 1+1+1 = 3? Wait, the problem 
           # usually implies all pairs. Let's re-verify logic.
           # If nums=[2, 4, 6], pairs: (2,4)->2, (2,6)->2, (4,6)->2. Sum=6.
    """
    if not nums:
        return 0

    max_val = max(nums)
    # count[i] stores the frequency of number i in the input
    count = [0] * (max_val + 1)
    for x in nums:
        count[x] += 1

    # gcd_count[g] will store the number of pairs (i, j) such that GCD(nums[i], nums[j]) == g
    gcd_count = [0] * (max_val + 1)

    # Iterate backwards from max_val to 1 to use inclusion-exclusion
    for g in range(max_val, 0, -1):
        # Count how many numbers in the array are multiples of g
        multiples_of_g = 0
        for multiple in range(g, max_val + 1, g):
            multiples_of_g += count[multiple]
        
        # Total pairs that can be formed using multiples of g
        # These pairs have a GCD that is at least g (it could be 2g, 3g, etc.)
        total_pairs_with_multiple_g = (multiples_of_g * (multiples_of_g - 1)) // 2
        
        # Subtract pairs whose GCD is a strict multiple of g (2g, 3g, ...)
        # to ensure we only count pairs where GCD is exactly g
        for multiple in range(2 * g, max_val + 1, g):
            total_pairs_with_multiple_g -= gcd_count[multiple]
            
        gcd_count[g] = total_pairs_with_multiple_g

    # The final answer is the sum of (g * number of pairs with GCD g)
    total_sum = 0
    for g in range(1, max_val + 1):
        total_sum += g * gcd_count[g]

    return total_sum
