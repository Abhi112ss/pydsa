METADATA = {
    "id": 1990,
    "name": "Count the Number of Experiments",
    "slug": "count-the-number-of-experiments",
    "category": "Math",
    "aliases": [],
    "tags": ["math", "combinatorics"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Calculate the number of ways to choose k elements from n elements such that the result is modulo 10^9 + 7.",
}

def solve(n: int, k: int) -> int:
    """
    Calculates the number of ways to choose k elements from n elements (nCk) 
    modulo 10^9 + 7 using modular inverse.

    Args:
        n (int): The total number of elements.
        k (int): The number of elements to choose.

    Returns:
        int: The value of nCr modulo 10^9 + 7.

    Examples:
        >>> solve(5, 2)
        10
        >>> solve(10, 3)
        120
    """
    MOD = 1_000_000_007

    if k < 0 or k > n:
        return 0
    
    # Optimization: nCr is symmetric, so nCk = nC(n-k)
    if k > n // 2:
        k = n - k

    # We calculate nCr = [n * (n-1) * ... * (n-k+1)] / [k * (k-1) * ... * 1]
    # To perform division under modulo, we use Fermat's Little Theorem:
    # a^(MOD-2) % MOD is the modular multiplicative inverse of a.
    
    numerator = 1
    denominator = 1
    
    for i in range(k):
        # Multiply numerator by (n - i)
        numerator = (numerator * (n - i)) % MOD
        # Multiply denominator by (i + 1)
        denominator = (denominator * (i + 1)) % MOD

    # Calculate modular inverse of denominator using pow(base, exp, mod)
    # which implements efficient modular exponentiation.
    denominator_inverse = pow(denominator, MOD - 2, MOD)

    return (numerator * denominator_inverse) % MOD
