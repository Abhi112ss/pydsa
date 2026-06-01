METADATA = {
    "id": 650,
    "name": "2 Keys Keyboard",
    "slug": "2-keys-keyboard",
    "category": "Math",
    "aliases": [],
    "tags": ["dynamic_programming", "math", "prime_factorization"],
    "difficulty": "medium",
    "time_complexity": "O(sqrt(n))",
    "space_complexity": "O(1)",
    "description": "Find the maximum number of characters that can be obtained using only 'Ctrl-A' and 'Ctrl-C' operations starting from a single 'A'.",
}

def solve(n: int) -> int:
    """
    Calculates the maximum number of characters possible using Ctrl-A and Ctrl-C.
    
    The problem is equivalent to finding the sum of the prime factors of n. 
    For every prime factor p of n, we can perform 1 'Ctrl-A' and (p-1) 'Ctrl-V' 
    operations to multiply the current count by p.

    Args:
        n: The target number of characters.

    Returns:
        The maximum number of characters that can be obtained.

    Examples:
        >>> solve(3)
        3
        >>> solve(9)
        5
        >>> solve(10)
        7
    """
    if n <= 1:
        return 0

    total_steps = 0
    divisor = 2
    remaining_n = n

    # We iterate up to the square root of n to find prime factors.
    # This is the standard efficient prime factorization approach.
    while divisor * divisor <= remaining_n:
        while remaining_n % divisor == 0:
            # If 'divisor' is a factor, it means we can multiply our 
            # current buffer by 'divisor' using 1 Select and (divisor-1) Pastes.
            total_steps += divisor
            remaining_n //= divisor
        divisor += 1

    # If remaining_n > 1, the leftover value is itself a prime factor.
    if remaining_n > 1:
        total_steps += remaining_n

    return total_steps
