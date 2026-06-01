METADATA = {
    "id": 313,
    "name": "Super Ugly Number",
    "slug": "super-ugly-number",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["heap", "dynamic_programming", "math"],
    "difficulty": "medium",
    "time_complexity": "O(n * k)",
    "space_complexity": "O(n + k)",
    "description": "Find the n-th super ugly number, which is a positive integer whose prime factors are all in a given list of primes.",
}

def solve(n: int, primes: list[int]) -> int:
    """
    Finds the n-th super ugly number using a dynamic programming approach.

    Args:
        n: The index of the super ugly number to find (1-indexed).
        primes: A list of prime numbers that can be used as factors.

    Returns:
        The n-th super ugly number.

    Examples:
        >>> solve(12, [2, 7, 13, 19])
        39
        >>> solve(1, [2, 3, 5])
        1
    """
    # dp[i] stores the (i+1)-th super ugly number
    dp = [0] * n
    dp[0] = 1
    
    # k is the number of primes provided
    k = len(primes)
    
    # pointers[i] tracks the index in dp that the i-th prime is currently multiplying
    # to produce the next potential super ugly number.
    pointers = [0] * k
    
    # next_multiples[i] stores the value of primes[i] * dp[pointers[i]]
    next_multiples = [p for p in primes]

    for i in range(1, n):
        # The next super ugly number is the minimum of all current possible multiples
        current_min = min(next_multiples)
        dp[i] = current_min
        
        # Update pointers and next_multiples for all primes that produced the current_min
        # This handles duplicates (e.g., if 2*7 and 7*2 both equal 14)
        for j in range(k):
            if next_multiples[j] == current_min:
                pointers[j] += 1
                next_multiples[j] = primes[j] * dp[pointers[j]]
                
    return dp[n - 1]
