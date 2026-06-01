METADATA = {
    "id": 1952,
    "name": "Three Divisors",
    "slug": "three_divisors",
    "category": "math",
    "aliases": [],
    "tags": ["math", "prime_number"],
    "difficulty": "easy",
    "time_complexity": "O(sqrt(n))",
    "space_complexity": "O(1)",
    "description": "Check if a number has exactly three divisors.",
}


def solve(num: int) -> bool:
    """Determine whether the given integer has exactly three divisors.

    A number has exactly three divisors iff it is the square of a prime number.

    Args:
        num: The integer to evaluate.

    Returns:
        True if `num` has exactly three divisors, otherwise False.

    Examples:
        >>> solve(4)
        True
        >>> solve(5)
        False
        >>> solve(9)
        True
        >>> solve(1)
        False
    """
    # A number with three divisors must be a perfect square.
    root = int(num ** 0.5)
    if root * root != num:
        return False

    # Check if the square root is a prime number.
    if root < 2:
        return False
    divisor = 2
    while divisor * divisor <= root:
        if root % divisor == 0:
            return False
        divisor += 1
    return True