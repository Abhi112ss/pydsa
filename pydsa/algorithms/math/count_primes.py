METADATA = {
    "id": 204,
    "name": "Count Primes",
    "slug": "count_primes",
    "category": "Algorithms",
    "aliases": [],
    "tags": ["math", "sieve"],
    "difficulty": "medium",
    "time_complexity": "O(n log log n)",
    "space_complexity": "O(n)",
    "description": "Count the number of prime numbers less than a non-negative integer n.",
}

def solve(n: int) -> int:
    """Count the number of prime numbers less than n using the Sieve of Eratosthenes.

    Args:
        n: A non-negative integer representing the upper bound (exclusive).

    Returns:
        The count of prime numbers strictly less than n.

    Examples:
        >>> solve(10)
        4
        >>> solve(0)
        0
        >>> solve(1)
        0
        >>> solve(2)
        0
        >>> solve(3)
        1
        >>> solve(100)
        25
    """
    if n < 2:
        return 0

    # Initialize sieve: True means the index is a candidate prime
    is_prime = [True] * n
    is_prime[0] = False
    is_prime[1] = False

    # Sieve of Eratosthenes: mark multiples of each prime as composite
    candidate = 2
    while candidate * candidate < n:
        if is_prime[candidate]:
            # Mark all multiples of candidate starting from candidate^2
            for multiple in range(candidate * candidate, n, candidate):
                is_prime[multiple] = False
        candidate += 1

    # Count all indices still marked as True (primes)
    return sum(is_prime)