METADATA = {
    "id": 2761,
    "name": "Prime Pairs With Target Sum",
    "slug": "prime-pairs-with-target-sum",
    "category": "Math",
    "aliases": [],
    "tags": ["sieve_of_eratosthenes", "math", "two_pointer"],
    "difficulty": "medium",
    "time_complexity": "O(n log log n)",
    "space_complexity": "O(n)",
    "description": "Find all pairs of prime numbers that sum up to a given target value.",
}

def solve(target: int) -> list[list[int]]:
    """
    Finds all pairs of prime numbers (p1, p2) such that p1 + p2 == target and p1 <= p2.

    Args:
        target: The target sum of the prime pairs.

    Returns:
        A list of lists, where each inner list contains a pair of primes [p1, p2].

    Examples:
        >>> solve(10)
        [[3, 7], [5, 5]]
        >>> solve(4)
        [[2, 2]]
    """
    if target < 4:
        return []

    # Step 1: Sieve of Eratosthenes to find all primes up to target
    # is_prime[i] will be True if i is a prime number
    is_prime = [True] * (target + 1)
    is_prime[0] = is_prime[1] = False
    
    for p in range(2, int(target**0.5) + 1):
        if is_prime[p]:
            # Mark multiples of p starting from p*p as not prime
            for multiple in range(p * p, target + 1, p):
                is_prime[multiple] = False

    # Step 2: Collect all primes into a sorted list for efficient iteration
    primes = [p for p, prime_status in enumerate(is_prime) if prime_status]

    results: list[list[int]] = []
    
    # Step 3: Use two pointers to find pairs that sum to target
    # Since the primes list is sorted, we can use the two-pointer approach
    left = 0
    right = len(primes) - 1

    while left <= right:
        current_sum = primes[left] + primes[right]
        
        if current_sum == target:
            results.append([primes[left], primes[right]])
            left += 1
            right -= 1
        elif current_sum < target:
            left += 1
        else:
            right -= 1

    return results
