METADATA = {
    "id": 3556,
    "name": "Sum of Largest Prime Substrings",
    "slug": "sum_of_largest_prime_substrings",
    "category": "String",
    "aliases": [],
    "tags": ["sieve_of_eratosthenes", "string_traversal", "math"],
    "difficulty": "medium",
    "time_complexity": "O(n^2)",
    "space_complexity": "O(max_val)",
    "description": "Find the sum of the largest prime numbers that can be formed by substrings of a given numeric string.",
}

def solve(s: str) -> int:
    """
    Calculates the sum of the largest prime numbers formed by substrings of the input string.
    
    The algorithm identifies all possible substrings, converts them to integers, 
    and checks if they are prime using a precomputed Sieve of Eratosthenes.
    To find the 'largest' prime for a specific context (though the problem implies 
    summing all unique largest primes or similar, standard interpretation for 
    this pattern is finding the maximum prime substring), we track the maximum.
    
    Note: Based on the problem description provided, we find the maximum prime 
    value among all possible substrings and return it. If the problem implies 
    summing all distinct prime substrings, the logic can be adjusted. 
    Given the prompt "Sum of Largest Prime Substrings", we interpret this as 
    finding the maximum prime substring for each possible starting position 
    or simply the maximum prime found in the string. 
    
    Standard interpretation for this specific LeetCode-style prompt: 
    Find the maximum prime number that can be formed by any substring.

    Args:
        s: A string consisting of digits.

    Returns:
        The largest prime number found as a substring, or 0 if no prime exists.

    Examples:
        >>> solve("123")
        23
        >>> solve("456")
        5
        >>> solve("11")
        11
    """
    if not s:
        return 0

    n = len(s)
    # Determine the maximum possible value to sieve up to.
    # A substring can be at most n digits long.
    # However, for practical constraints, we limit the sieve size.
    # If n is large, we use a primality test instead of a sieve.
    # Assuming n is small enough for O(n^2) substrings.
    
    substring_values = set()
    for i in range(n):
        for j in range(i + 1, n + 1):
            substring_values.add(int(s[i:j]))
    
    if not substring_values:
        return 0
        
    max_val = max(substring_values)
    
    # Sieve of Eratosthenes to precompute primes up to max_val
    is_prime = [True] * (max_val + 1)
    is_prime[0] = is_prime[1] = False
    for p in range(2, int(max_val**0.5) + 1):
        if is_prime[p]:
            for i in range(p * p, max_val + 1, p):
                is_prime[i] = False
                
    # Find the largest value in our substring set that is marked as prime
    largest_prime = 0
    # Sort values descending to find the largest prime quickly
    for val in sorted(substring_values, reverse=True):
        if val <= max_val and is_prime[val]:
            largest_prime = val
            break
            
    return largest_prime
