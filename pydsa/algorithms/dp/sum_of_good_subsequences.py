METADATA = {
    "id": 3351,
    "name": "Sum of Good Subsequences",
    "slug": "sum_of_good_subsequences",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dp", "math", "combinatorics"],
    "difficulty": "hard",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Calculate the sum of all elements in all 'good' subsequences where all elements in a subsequence are equal.",
}

def solve(nums: list[int]) -> int:
    """
    Calculates the sum of all elements in all 'good' subsequences.
    A subsequence is 'good' if all its elements are equal.
    
    The problem asks for the sum of all elements in all subsequences where 
    every element in the subsequence is the same. This is equivalent to 
    summing (value * number of subsequences containing that value) for 
    each unique value in the array.
    
    For a value 'v' that appears 'k' times in the array:
    The number of non-empty subsequences consisting only of 'v' is (2^k - 1).
    Each such subsequence contributes to the total sum.
    However, the problem asks for the sum of elements. 
    In a subsequence of length 'L' consisting of value 'v', the sum is L * v.
    
    Total sum for a specific value 'v' appearing 'k' times:
    Sum = sum_{L=1 to k} [ (number of ways to choose L elements) * (L * v) ]
    Sum = v * sum_{L=1 to k} [ C(k, L) * L ]
    Using the identity: sum_{L=1 to k} [ C(k, L) * L ] = k * 2^(k-1)
    
    Args:
        nums: A list of integers.

    Returns:
        The total sum of all elements in all good subsequences modulo 10^9 + 7.

    Examples:
        >>> solve([1, 2, 1])
        5
        # Good subsequences: [1], [2], [1], [1, 1]
        # Sums: 1 + 2 + 1 + (1 + 1) = 5
    """
    MOD = 10**9 + 7
    
    # Count frequencies of each number
    counts = {}
    for num in nums:
        counts[num] = counts.get(num, 0) + 1
        
    total_sum = 0
    
    # Precompute powers of 2 to keep complexity O(n)
    # max_k is the maximum frequency found
    max_k = max(counts.values()) if counts else 0
    pow2 = [1] * (max_k + 1)
    for i in range(1, max_k + 1):
        pow2[i] = (pow2[i - 1] * 2) % MOD
        
    for val, k in counts.items():
        # The contribution of value 'val' appearing 'k' times is:
        # val * k * 2^(k-1)
        # This comes from the combinatorial identity sum_{i=1}^k i * binom(k, i) = k * 2^(k-1)
        
        # Handle the k=0 case (though counts won't have 0)
        if k == 0:
            continue
            
        # Calculate contribution: val * k * 2^(k-1)
        # We use pow2[k-1] for 2^(k-1)
        contribution = (val * k) % MOD
        contribution = (contribution * pow2[k - 1]) % MOD
        
        total_sum = (total_sum + contribution) % MOD
        
    return total_sum
