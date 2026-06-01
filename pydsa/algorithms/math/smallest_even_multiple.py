METADATA = {
    "id": 2413,
    "name": "Smallest Even Multiple",
    "slug": "smallest-even-multiple",
    "category": "Math",
    "aliases": [],
    "tags": ["math"],
    "difficulty": "easy",
    "time_complexity": "O(1)",
    "space_complexity": "O(1)",
    "description": "Given a positive integer n, return the smallest positive integer that is divisible by both 2 and n.",
}

def solve(n: int) -> int:
    """
    Finds the smallest positive integer that is divisible by both 2 and n.

    Args:
        n: A positive integer.

    Returns:
        The smallest positive integer divisible by both 2 and n.

    Examples:
        >>> solve(2)
        2
        >>> solve(3)
        6
        >>> solve(5)
        10
    """
    # If n is already even, it is already a multiple of 2.
    # Therefore, the smallest multiple of both 2 and n is n itself.
    if n % 2 == 0:
        return n
    
    # If n is odd, the smallest multiple of both 2 and n is 2 * n.
    # This is because 2 is prime and does not share any factors with an odd n.
    return 2 * n
