METADATA = {
    "id": 1492,
    "name": "The kth Factor of n",
    "slug": "the_kth_factor_of_n",
    "category": "math",
    "aliases": [],
    "tags": ["math"],
    "difficulty": "medium",
    "time_complexity": "O(sqrt(n))",
    "space_complexity": "O(1)",
    "description": "Return the kth factor of n in ascending order, or -1 if it does not exist.",
}


def solve(n: int, k: int) -> int:
    """Return the k-th factor of ``n`` in ascending order.

    Args:
        n: A positive integer whose factors are considered.
        k: The 1‑based index of the factor to retrieve.

    Returns:
        The k-th factor if it exists; otherwise -1.

    Examples:
        >>> solve(12, 3)
        3
        >>> solve(7, 2)
        7
        >>> solve(4, 2)
        2
        >>> solve(4, 5)
        -1
    """
    import math

    # First pass: count factors up to sqrt(n) in ascending order.
    limit = int(math.isqrt(n))
    count = 0
    for divisor in range(1, limit + 1):
        if n % divisor == 0:
            count += 1
            if count == k:
                return divisor

    # Second pass: consider the complementary large factors in descending order.
    for divisor in range(limit, 0, -1):
        if n % divisor == 0:
            large_factor = n // divisor
            if large_factor != divisor:  # avoid double‑counting a perfect square root
                count += 1
                if count == k:
                    return large_factor

    return -1