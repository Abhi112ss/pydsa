METADATA = {
    "id": 3115,
    "name": "Maximum Prime Difference",
    "slug": "maximum-prime-difference",
    "category": "Math",
    "aliases": [],
    "tags": ["sieve_of_eratosthenes", "math"],
    "difficulty": "easy",
    "time_complexity": "O(n log log n)",
    "space_complexity": "O(n)",
    "description": "Find the maximum difference between any two prime numbers in the range [2, n].",
}

def solve(n: int) -> int:
    """
    Calculates the maximum difference between two prime numbers in the range [2, n].

    The maximum difference is achieved by subtracting the smallest prime (2) 
    from the largest prime less than or equal to n.

    Args:
        n: The upper bound of the range.

    Returns:
        The maximum difference between two primes in the range [2, n].

    Examples:
        >>> solve(10)
        7  # Primes are 2, 3, 5, 7. Max diff: 7 - 2 = 5. Wait, 7-2=5.
        # Correction: Primes <= 10 are 2, 3, 5, 7. Max diff is 7 - 2 = 5.
        >>> solve(20)
        17 # Primes are 2, 3, 5, 7, 11, 13, 17, 19. Max diff: 19 - 2 = 17.
    """
    if n < 3:
        return 0

    # Sieve of Eratosthenes to find all primes up to n
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    
    for p in range(2, int(n**0.5) + 1):
        if is_prime[p]:
            # Mark multiples of p starting from p*p as not prime
            for multiple in range(p * p, n + 1, p):
                is_prime[multiple] = False

    # Find the smallest prime (which is always 2 if n >= 2)
    smallest_prime = 2
    
    # Find the largest prime by iterating backwards from n
    largest_prime = 2
    for i in range(n, 1, -1):
        if is_prime[i]:
            largest_prime = i
            break
            
    return largest_prime - smallest_prime
