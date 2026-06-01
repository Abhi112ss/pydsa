METADATA = {
    "id": 1175,
    "name": "Prime Arrangements",
    "slug": "prime_arrangements",
    "category": "math",
    "aliases": [],
    "tags": ["combinatorics", "sieve_of_eratosthenes"],
    "difficulty": "easy",
    "time_complexity": "O(n log log n)",
    "space_complexity": "O(1)",
    "description": "Count permutations where prime numbers occupy prime indices.",
}


def solve() -> None:
    """Calculate the number of valid prime arrangements for a given n.

    Args:
        None (reads integer n from standard input).

    Returns:
        None (prints the result modulo 10**9 + 7).

    Example:
        >>> import sys, io
        >>> sys.stdin = io.StringIO('5')
        >>> solve()
        12
    """
    import sys
    MOD: int = 10**9 + 7

    data = sys.stdin.read().strip().split()
    if not data:
        return
    n: int = int(data[0])

    # Sieve of Eratosthenes to count primes up to n
    is_prime: list[bool] = [True] * (n + 1)
    if n >= 0:
        is_prime[0] = False
    if n >= 1:
        is_prime[1] = False
    limit: int = int(n**0.5) + 1
    for i in range(2, limit):
        if is_prime[i]:
            step: int = i
            start: int = i * i
            for multiple in range(start, n + 1, step):
                is_prime[multiple] = False
    prime_count: int = sum(is_prime)

    non_prime_count: int = n - prime_count

    # Compute factorial(prime_count) * factorial(non_prime_count) modulo MOD
    result: int = 1
    for i in range(2, prime_count + 1):
        result = (result * i) % MOD
    for i in range(2, non_prime_count + 1):
        result = (result * i) % MOD

    print(result)
