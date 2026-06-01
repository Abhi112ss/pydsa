METADATA = {
    "id": 2523,
    "name": "Closest Prime Numbers in Range",
    "slug": "closest-prime-numbers-in-range",
    "category": "Math",
    "aliases": [],
    "tags": ["math", "sieve_of_eratosthenes", "binary_search"],
    "difficulty": "medium",
    "time_complexity": "O(n log log n)",
    "space_complexity": "O(n)",
    "description": "Find two prime numbers in a given range [left, right] such that the difference between them is minimized.",
}

def solve(left: int, right: int) -> list[int]:
    """
    Finds the two closest prime numbers within the inclusive range [left, right].

    Args:
        left (int): The lower bound of the range.
        right (int): The upper bound of the range.

    Returns:
        list[int]: A list containing the two closest primes in ascending order.
                   If multiple pairs exist, any such pair is acceptable.

    Examples:
        >>> solve(10, 20)
        [11, 13]
        >>> solve(1, 10)
        [2, 3]
    """
    if right < 2:
        return []

    # Step 1: Sieve of Eratosthenes to find all primes up to 'right'
    # is_prime[i] will be True if i is a prime number
    is_prime = [True] * (right + 1)
    is_prime[0] = is_prime[1] = False
    
    for p in range(2, int(right**0.5) + 1):
        if is_prime[p]:
            # Mark multiples of p starting from p*p as not prime
            for multiple in range(p * p, right + 1, p):
                is_prime[multiple] = False

    # Step 2: Collect all primes that fall within the [left, right] range
    primes_in_range = []
    for num in range(left, right + 1):
        if is_prime[num]:
            primes_in_range.append(num)

    # If fewer than two primes are found, no pair exists
    if len(primes_in_range) < 2:
        return []

    # Step 3: Iterate through the collected primes to find the minimum gap
    min_diff = float('inf')
    result_pair = []

    for i in range(len(primes_in_range) - 1):
        current_diff = primes_in_range[i + 1] - primes_in_range[i]
        if current_diff < min_diff:
            min_diff = current_diff
            result_pair = [primes_in_range[i], primes_in_range[i + 1]]
            
            # Optimization: The smallest possible gap between primes > 2 is 2
            if min_diff == 2:
                return result_pair

    return result_pair
