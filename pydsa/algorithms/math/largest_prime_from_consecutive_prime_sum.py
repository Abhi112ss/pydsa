METADATA = {
    "id": 3770,
    "name": "Largest Prime from Consecutive Prime Sum",
    "slug": "largest_prime_from_consecutive_prime_sum",
    "category": "Math",
    "aliases": [],
    "tags": ["math", "sliding_window", "sieve"],
    "difficulty": "medium",
    "time_complexity": "O(N log log N)",
    "space_complexity": "O(N)",
    "description": "Find the largest prime number that can be represented as a sum of consecutive prime numbers.",
}

def solve(n: int) -> int:
    """
    Finds the largest prime number that is a sum of consecutive prime numbers.

    Args:
        n: The upper bound limit for the prime numbers and their sums.

    Returns:
        The largest prime number <= n that is a sum of consecutive primes.
        Returns 0 if no such prime exists (though 2 is always a prime).

    Examples:
        >>> solve(10)
        5
        >>> solve(20)
        5
        >>> solve(100)
        41
    """
    if n < 2:
        return 0

    # Step 1: Sieve of Eratosthenes to find all primes up to n
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    for p in range(2, int(n**0.5) + 1):
        if is_prime[p]:
            for i in range(p * p, n + 1, p):
                is_prime[i] = False
    
    primes = [i for i, val in enumerate(is_prime) if val]
    num_primes = len(primes)
    
    # We want the largest prime, so we check sums and verify if they are prime.
    # However, the problem asks for the largest prime that IS a sum.
    # We can iterate through all possible consecutive sums.
    
    max_prime_sum = 0

    # Step 2: Use a sliding window/two-pointer approach to find consecutive sums
    # Since we want the LARGEST prime sum <= n, we can iterate through all 
    # possible lengths of consecutive sequences.
    for length in range(num_primes, 0, -1):
        # Optimization: if the smallest possible sum of this length is > n, skip
        # But we don't know the length beforehand, so we iterate lengths.
        # Actually, a more efficient way is to use a sliding window for each length.
        
        # Calculate initial window sum for current length
        current_sum = sum(primes[:length])
        
        # If the smallest sum of this length is already smaller than our best found,
        # and we are decreasing length, we might still find a larger prime.
        # But if current_sum > n, we need to slide the window.
        
        for start_idx in range(num_primes - length + 1):
            if start_idx > 0:
                # Slide the window: subtract the element leaving and add the new one
                current_sum = current_sum - primes[start_idx - 1] + primes[start_idx + length - 1]
            
            if current_sum <= n:
                if is_prime[current_sum]:
                    if current_sum > max_prime_sum:
                        max_prime_sum = current_sum
            else:
                # Since primes are increasing, if current_sum > n, 
                # moving the window right will only increase the sum.
                break
        
        # If we found a prime sum and the current length's smallest sum 
        # is already less than max_prime_sum, we can't do better with smaller lengths?
        # No, that's not true. A smaller length could result in a larger prime.
        # However, if max_prime_sum is already very close to n, we can prune.
        if max_prime_sum == n:
            return n

    return max_prime_sum
