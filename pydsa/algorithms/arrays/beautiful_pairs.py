METADATA = {
    "id": 2613,
    "name": "Beautiful Pairs",
    "slug": "beautiful_pairs",
    "category": "Math",
    "aliases": [],
    "tags": ["math", "hash_map", "gcd"],
    "difficulty": "medium",
    "time_complexity": "O(n^2)",
    "space_complexity": "O(1)",
    "description": "Count pairs (i, j) such that 0 <= i < j < n and gcd(nums[i], nums[j]) is a prime number.",
}

import math

def solve(nums: list[int]) -> int:
    """
    Counts the number of beautiful pairs in the given list.
    A pair (nums[i], nums[j]) is beautiful if 0 <= i < j < n and 
    gcd(nums[i], nums[j]) is a prime number.

    Args:
        nums: A list of integers.

    Returns:
        The total count of beautiful pairs.

    Examples:
        >>> solve([2, 3, 5])
        3
        >>> solve([1, 1, 1])
        0
    """
    n = len(nums)
    beautiful_count = 0

    def is_prime(num: int) -> bool:
        """Helper to check if a number is prime."""
        if num < 2:
            return False
        for i in range(2, int(math.isqrt(num)) + 1):
            if num % i == 0:
                return False
        return True

    # Iterate through all possible pairs (i, j) where i < j
    for i in range(n):
        for j in range(i + 1, n):
            # Calculate the Greatest Common Divisor of the pair
            current_gcd = math.gcd(nums[i], nums[j])
            
            # Check if the GCD is a prime number
            if is_prime(current_gcd):
                beautiful_count += 1
                
    return beautiful_count
