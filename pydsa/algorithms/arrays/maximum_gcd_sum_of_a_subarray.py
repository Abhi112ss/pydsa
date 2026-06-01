METADATA = {
    "id": 2941,
    "name": "Maximum GCD-Sum of a Subarray",
    "slug": "maximum-gcd-sum-of-a-subarray",
    "category": "Array",
    "aliases": [],
    "tags": ["prefix_sum", "gcd", "sliding_window"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Find the maximum sum of a subarray where the greatest common divisor of all elements in the subarray is greater than 1.",
}

import math

def solve(nums: list[int]) -> int:
    """
    Finds the maximum sum of a subarray such that the GCD of all elements 
    in that subarray is greater than 1.

    Args:
        nums: A list of integers.

    Returns:
        The maximum sum of a subarray with GCD > 1. Returns 0 if no such subarray exists.

    Examples:
        >>> solve([2, 4, 6, 3, 9])
        12  # Subarray [2, 4, 6] has GCD 2, sum 12. [3, 9] has GCD 3, sum 12.
        >>> solve([1, 1, 1])
        0
        >>> solve([10, 5, 15, 7])
        30  # Subarray [10, 5, 15] has GCD 5, sum 30.
    """
    n = len(nums)
    max_sum = 0

    # We iterate through all possible prime factors that could be the GCD.
    # However, a more efficient way is to group contiguous elements 
    # that share a common prime factor.
    
    # To handle this efficiently, we can find all prime factors for each number.
    # Since we want the maximum sum for a subarray where GCD > 1, 
    # it means all elements in that subarray must be divisible by some prime p.
    
    # Step 1: Identify all unique prime factors present in the array.
    # Step 2: For each prime factor, find the maximum sum of a contiguous 
    # subarray where every element is divisible by that prime.
    
    prime_to_max_sum = {}
    
    # We use a dictionary to track the current running sum for each prime factor.
    # current_sums[p] stores the sum of the current contiguous segment divisible by p.
    current_sums = {}

    for x in nums:
        # Find prime factors of x
        factors = set()
        temp = x
        d = 2
        while d * d <= temp:
            if temp % d == 0:
                factors.add(d)
                while temp % d == 0:
                    temp //= d
            d += 1
        if temp > 1:
            factors.add(temp)
            
        # Update current contiguous sums for each prime factor found in x
        # If x is divisible by p, add x to the current running sum for p.
        # If x is not divisible by p, the contiguous segment for p is broken.
        
        # We need to track which primes were "active" in the previous step.
        # To do this efficiently, we can iterate through all primes seen so far,
        # but that's slow. Instead, we only care about primes that divide x.
        
        # We'll use a dictionary to keep track of the 'current' sum for every prime.
        # If a prime is not in the current x's factors, its current sum resets to 0.
        
        # To implement this correctly:
        # 1. Get all primes that have been seen before.
        # 2. If a prime is in 'factors', current_sums[p] += x.
        # 3. If a prime is NOT in 'factors', current_sums[p] = 0.
        
        # Optimization: Instead of iterating all primes, we only update primes 
        # that are actually in the current number and reset others.
        # But we don't know which others to reset without a list.
        
        # Let's use a different approach: 
        # For each prime factor p, find the max sum of contiguous elements divisible by p.
        pass

    # Re-implementing with a more robust approach:
    # We will map each prime to the sum of its current contiguous segment.
    prime_current_segment_sum = {}
    max_total_sum = 0
    
    # To handle the "reset" logic, we track which primes were active in the last element.
    active_primes = set()

    for x in nums:
        # Find prime factors of x
        factors = set()
        temp = x
        d = 2
        while d * d <= temp:
            if temp % d == 0:
                factors.add(d)
                while temp % d == 0:
                    temp //= d
            d += 1
        if temp > 1:
            factors.add(temp)
            
        # Primes that were active but are not in the current x's factors must be reset.
        # Primes that are in x's factors will have their sum increased.
        # Primes that are new will start with sum x.
        
        # 1. Reset primes that are no longer contiguous
        for p in active_primes:
            if p not in factors:
                prime_current_segment_sum[p] = 0
        
        # 2. Update sums for current factors
        for p in factors:
            prime_current_segment_sum[p] = prime_current_segment_sum.get(p, 0) + x
            # Update global max
            if prime_current_segment_sum[p] > max_total_sum:
                max_total_sum = prime_current_segment_sum[p]
        
        # 3. Update active primes set
        active_primes = factors

    return max_total_sum
