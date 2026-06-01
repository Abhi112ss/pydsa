METADATA = {
    "id": 2438,
    "name": "Range Product Queries of Powers",
    "slug": "range-product-queries-of-powers",
    "category": "Math",
    "aliases": [],
    "tags": ["bit_manipulation", "arrays", "math"],
    "difficulty": "medium",
    "time_complexity": "O(log n + q * log n)",
    "space_complexity": "O(log n)",
    "description": "Given an integer n, construct an array of powers of 2 that sum to n, then answer queries for the product of elements in specific ranges.",
}

def solve(n: int, queries: list[list[int]]) -> list[int]:
    """
    Constructs the powers of 2 array from n and calculates range products modulo 10^9 + 7.

    Args:
        n: The target integer to decompose into powers of 2.
        queries: A list of [left, right] indices representing ranges.

    Returns:
        A list of integers representing the product of elements in each range modulo 10^9 + 7.

    Examples:
        >>> solve(15, [[0, 1], [2, 2], [0, 3]])
        [20, 4, 120]
        >>> solve(5, [[0, 0], [0, 1]])
        [1, 5]
    """
    MOD = 1_000_000_007

    # Step 1: Decompose n into its constituent powers of 2.
    # Since n is decomposed into powers of 2, we can just find the set bits.
    powers = []
    current_bit = 0
    temp_n = n
    while temp_n > 0:
        if temp_n & 1:
            powers.append(1 << current_bit)
        temp_n >>= 1
        current_bit += 1

    # Step 2: To avoid large number multiplications, we work with the exponents.
    # The product of 2^a * 2^b * 2^c is 2^(a + b + c).
    # We convert the 'powers' array into an array of their exponents.
    exponents = []
    for p in powers:
        # Find the exponent such that 2^exponent = p
        # Since p is a power of 2, we can use bit_length() - 1
        exponents.append(p.bit_length() - 1)

    # Step 3: Precompute prefix sums of exponents to answer range queries in O(1) exponent sum.
    prefix_exponents = [0] * (len(exponents) + 1)
    for i in range(len(exponents)):
        prefix_exponents[i + 1] = prefix_exponents[i] + exponents[i]

    results = []
    for left, right in queries:
        # Calculate the sum of exponents in the range [left, right]
        # sum(exponents[left...right]) = prefix[right+1] - prefix[left]
        total_exponent = prefix_exponents[right + 1] - prefix_exponents[left]
        
        # Step 4: Compute 2^total_exponent % MOD using modular exponentiation.
        # pow(base, exp, mod) is efficient O(log exp).
        results.append(pow(2, total_exponent, MOD))

    return results
