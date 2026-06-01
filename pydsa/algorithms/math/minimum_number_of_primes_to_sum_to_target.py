METADATA = {
    "id": 3610,
    "name": "Minimum Number of Primes to Sum to Target",
    "slug": "minimum-number-of-primes-to-sum-to-target",
    "category": "Math",
    "aliases": [],
    "tags": ["math", "number-theory"],
    "difficulty": "medium",
    "time_complexity": "O(sqrt(n))",
    "space_complexity": "O(1)",
    "description": "Find the minimum number of prime numbers that sum up to a given target integer using Goldbach's conjectures.",
}

def is_prime(n: int) -> bool:
    """Checks if a number is prime using trial division up to sqrt(n)."""
    if n < 2:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def solve(target: int) -> int:
    """
    Calculates the minimum number of primes required to sum to the target.
    
    Based on Goldbach's conjectures:
    1. If target is prime, result is 1.
    2. If target is even and > 2, result is 2 (Goldbach's strong conjecture).
    3. If target is odd:
       a. If target - 2 is prime, result is 2 (2 + prime).
       b. Otherwise, result is 3 (Goldbach's weak conjecture).
    Note: The problem assumes target >= 2.

    Args:
        target: The integer to represent as a sum of primes.

    Returns:
        The minimum number of primes needed.

    Examples:
        >>> solve(2)
        1
        >>> solve(4)
        2
        >>> solve(7)
        1
        >>> solve(11)
        1
        >>> solve(27)
        2
    """
    if target < 2:
        return 0 # Should not happen based on problem constraints
    
    # Case 1: The number itself is prime
    if is_prime(target):
        return 1
    
    # Case 2: Target is even
    # Goldbach's strong conjecture: every even integer > 2 is the sum of two primes.
    # Since we already checked if target is prime (and 2 is the only even prime),
    # any even target > 2 that isn't prime (which is all even > 2) will be 2.
    if target % 2 == 0:
        return 2
    
    # Case 3: Target is odd
    # An odd number can be a sum of 2 primes if (target - 2) is prime (since 2 is the only even prime).
    if is_prime(target - 2):
        return 2
    
    # Case 4: Target is odd and (target - 2) is not prime.
    # According to Goldbach's weak conjecture, every odd number > 5 is the sum of three primes.
    return 3
