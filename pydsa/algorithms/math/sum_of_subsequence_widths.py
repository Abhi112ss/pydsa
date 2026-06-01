METADATA = {
    "id": 891,
    "name": "Sum of Subsequence Widths",
    "slug": "sum-of-subsequence-widths",
    "category": "Math",
    "aliases": [],
    "tags": ["sorting", "combinatorics"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(1)",
    "description": "Calculate the sum of the widths of all possible subsequences of a given array.",
}

def solve(nums: list[int]) -> int:
    """
    Calculates the sum of the widths of all possible subsequences.
    The width of a subsequence is the difference between its maximum and minimum elements.

    Args:
        nums: A list of integers.

    Returns:
        The sum of widths of all subsequences modulo 10^9 + 7.

    Examples:
        >>> solve([1, 2, 3])
        4
        >>> solve([10, 1, 2, 7])
        151
    """
    MOD = 10**9 + 7
    n = len(nums)
    
    # Sorting allows us to treat the element at index i as the max or min 
    # of specific subsets based on its position.
    nums.sort()
    
    total_width_sum = 0
    
    # For a sorted array, an element at index i:
    # 1. Acts as the maximum in 2^i subsequences (all elements to its left can be in or out).
    # 2. Acts as the minimum in 2^(n - 1 - i) subsequences (all elements to its right can be in or out).
    # The contribution of nums[i] to the total sum is:
    # nums[i] * (count_as_max - count_as_min)
    
    # Precompute powers of 2 to avoid repeated exponentiation
    # or use pow(2, exp, MOD) for efficiency.
    for i in range(n):
        # Number of subsequences where nums[i] is the maximum
        count_as_max = pow(2, i, MOD)
        
        # Number of subsequences where nums[i] is the minimum
        count_as_min = pow(2, n - 1 - i, MOD)
        
        # Contribution to the total sum
        contribution = (nums[i] * (count_as_max - count_as_min)) % MOD
        total_width_sum = (total_width_sum + contribution) % MOD
        
    return total_width_sum
