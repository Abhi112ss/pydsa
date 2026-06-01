METADATA = {
    "id": 507,
    "name": "Perfect Number",
    "slug": "perfect_number",
    "category": "Math",
    "aliases": [],
    "tags": ["math", "divisors"],
    "difficulty": "easy",
    "time_complexity": "O(sqrt(n))",
    "space_complexity": "O(1)",
    "description": "Determine whether a given integer is a perfect number.",
}


def solve(n: int) -> bool:
    """Determine if the given integer is a perfect number.

    Args:
        n: The integer to evaluate. Must be non‑negative.

    Returns:
        True if `n` is a perfect number, otherwise False.

    Examples:
        >>> solve(28)
        True
        >>> solve(6)
        True
        >>> solve(5)
        False
    """
    # Perfect numbers are greater than 1; 1 is not considered perfect.
    if n <= 1:
        return False

    import math

    sum_of_divisors = 1  # 1 is a proper divisor of any n > 1
    limit = int(math.isqrt(n))

    # Iterate up to sqrt(n) to find divisor pairs.
    for divisor in range(2, limit + 1):
        if n % divisor == 0:
            paired_divisor = n // divisor
            sum_of_divisors += divisor
            if paired_divisor != divisor:
                sum_of_divisors += paired_divisor
            # Early exit if sum already exceeds n
            if sum_of_divisors > n:
                return False

    return sum_of_divisors == n