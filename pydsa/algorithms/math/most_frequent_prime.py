METADATA = {
    "id": 3044,
    "name": "Most Frequent Prime",
    "slug": "most-frequent-prime",
    "category": "Math",
    "aliases": [],
    "tags": ["sieve_of_eratosthenes", "math", "hash-table"],
    "difficulty": "medium",
    "time_complexity": "O(max_val log log max_val + n)",
    "space_complexity": "O(max_val)",
    "description": "Find the smallest prime number that appears most frequently in a given array.",
}

def solve(nums: list[int]) -> int:
    """
    Finds the smallest prime number that appears most frequently in the input array.

    Args:
        nums: A list of integers.

    Returns:
        The smallest prime number with the maximum frequency.

    Examples:
        >>> solve([1, 2, 3, 3, 5, 5, 5])
        5
        >>> solve([2, 3, 5, 7, 11])
        2
    """
    if not nums:
        return -1

    max_val = max(nums)
    
    # Step 1: Sieve of Eratosthenes to find all primes up to max_val
    # is_prime[i] will be True if i is a prime number
    is_prime = [True] * (max_val + 1)
    is_prime[0] = is_prime[1] = False
    
    for p in range(2, int(max_val**0.5) + 1):
        if is_prime[p]:
            # Mark multiples of p starting from p*p as not prime
            for multiple in range(p * p, max_val + 1, p):
                is_prime[multiple] = False

    # Step 2: Count frequencies of prime numbers present in the input array
    prime_counts = {}
    for num in nums:
        if is_prime[num]:
            prime_counts[num] = prime_counts.get(num, 0) + 1

    # Step 3: Find the prime with the highest frequency. 
    # If frequencies are tied, pick the smallest prime.
    max_frequency = 0
    result_prime = -1

    # Sorting keys ensures we encounter smaller primes first for tie-breaking
    # However, iterating through sorted keys is O(P log P). 
    # A more efficient way is to track max_frequency and update result_prime.
    for prime in sorted(prime_counts.keys()):
        count = prime_counts[prime]
        if count > max_frequency:
            max_frequency = count
            result_prime = prime
            
    return result_prime
