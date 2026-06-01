METADATA = {
    "id": 263,
    "name": "Ugly Number",
    "slug": "ugly_number",
    "category": "Math",
    "aliases": [],
    "tags": ["math", "prime factorization"],
    "difficulty": "easy",
    "time_complexity": "O(log n)",
    "space_complexity": "O(1)",
    "description": "Determine whether a given integer is an ugly number.",
}


def solve(num: int) -> bool:
    """Check if a positive integer is an ugly number.

    An ugly number is a positive integer whose prime factors are limited to
    2, 3, and 5. The function repeatedly divides the number by these primes
    until it can no longer be divided.

    Args:
        num: The integer to be evaluated.

    Returns:
        True if ``num`` is an ugly number, otherwise False.

    Examples:
        >>> solve(6)
        True
        >>> solve(14)
        False
        >>> solve(1)
        True
    """
    # Ugly numbers must be positive; non‑positive numbers are not considered ugly.
    if num <= 0:
        return False

    # Remove all factors of 2, 3, and 5.
    for prime in (2, 3, 5):
        while num % prime == 0:
            num //= prime

    # After removing allowed prime factors, the number should be reduced to 1.
    return num == 1