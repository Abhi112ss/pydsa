METADATA = {
    "id": 2521,
    "name": "Distinct Prime Factors of Product of Array",
    "slug": "distinct-prime-factors-of-product-of-array",
    "category": "Math",
    "aliases": [],
    "tags": ["math", "prime_factorization", "hash_set"],
    "difficulty": "medium",
    "time_complexity": "O(n * sqrt(max_val))",
    "space_complexity": "O(number_of_unique_primes)",
    "description": "Find the number of distinct prime factors of the product of all elements in an array.",
}

def solve(nums: list[int]) -> int:
    """
    Calculates the number of distinct prime factors of the product of all elements in nums.

    Instead of computing the product (which could lead to overflow), we find the 
    prime factors of each individual number and store them in a set to ensure uniqueness.

    Args:
        nums: A list of positive integers.

    Returns:
        The count of distinct prime factors found across all elements.

    Examples:
        >>> solve([2, 3, 6, 10])
        3  # Prime factors: 2, 3, 5
        >>> solve([15, 51, 23, 127])
        5  # Prime factors: 3, 5, 17, 23, 127
    """
    distinct_primes = set()

    for num in nums:
        # Standard prime factorization algorithm
        # We iterate up to the square root of the current number
        d = 2
        temp = num
        while d * d <= temp:
            if temp % d == 0:
                distinct_primes.add(d)
                # Divide out all occurrences of this prime factor
                while temp % d == 0:
                    temp //= d
            d += 1
        
        # If temp > 1 after the loop, the remaining temp is a prime factor
        if temp > 1:
            distinct_primes.add(temp)

    return len(distinct_primes)
