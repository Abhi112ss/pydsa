METADATA = {
    "id": 3918,
    "name": "Sum of Primes Between Number and Its Reverse",
    "slug": "sum_of_primes_between_number_and_its_reverse",
    "category": "Math",
    "aliases": [],
    "tags": ["sieve_of_eratosthenes", "math", "prefix_sum"],
    "difficulty": "medium",
    "time_complexity": "O(M log log M)",
    "space_complexity": "O(M)",
    "description": "Calculate the sum of all prime numbers in the range between a given number and its reverse.",
}

def solve(n: int) -> int:
    """
    Calculates the sum of all prime numbers between n and its reverse.

    The range is inclusive of both the number and its reverse. 
    The function handles the case where the reverse might be smaller than n.

    Args:
        n: The input integer.

    Returns:
        The sum of all prime numbers in the range [min(n, rev), max(n, rev)].

    Examples:
        >>> solve(12)
        # Reverse is 21. Primes in [12, 21] are 13, 17, 19. Sum = 49.
        >>> solve(10)
        # Reverse is 1. Primes in [1, 10] are 2, 3, 5, 7. Sum = 17.
    """
    # Calculate the reverse of the number
    reverse_n = int(str(n)[::-1])
    
    # Define the range boundaries
    lower_bound = min(n, reverse_n)
    upper_bound = max(n, reverse_n)

    if upper_bound < 2:
        return 0

    # Step 1: Sieve of Eratosthenes to find all primes up to upper_bound
    # is_prime[i] will be True if i is a prime number
    is_prime = [True] * (upper_bound + 1)
    is_prime[0] = is_prime[1] = False
    
    for p in range(2, int(upper_bound**0.5) + 1):
        if is_prime[p]:
            # Mark multiples of p as not prime starting from p*p
            for multiple in range(p * p, upper_bound + 1, p):
                is_prime[multiple] = False

    # Step 2: Sum the primes within the specified range
    prime_sum = 0
    for i in range(lower_bound, upper_bound + 1):
        if is_prime[i]:
            prime_sum += i

    return prime_sum
