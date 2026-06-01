METADATA = {
    "id": 3842,
    "name": "Toggle Light Bulbs",
    "slug": "toggle-light-bulbs",
    "category": "Math",
    "aliases": [],
    "tags": ["math", "number_theory"],
    "difficulty": "easy",
    "time_complexity": "O(1)",
    "space_complexity": "O(1)",
    "description": "Determine the number of light bulbs that remain on after toggling bulbs in a specific pattern.",
}

import math

def solve(n: int) -> int:
    """
    Calculates the number of light bulbs that remain on after n toggling rounds.

    In this problem, a bulb at position 'i' is toggled during round 'd' if 'd' is a divisor of 'i'.
    A bulb remains 'on' if it is toggled an odd number of times.
    A number has an odd number of divisors if and only if it is a perfect square.
    Therefore, the problem reduces to counting the number of perfect squares between 1 and n.

    Args:
        n (int): The total number of light bulbs.

    Returns:
        int: The count of bulbs that remain on.

    Examples:
        >>> solve(10)
        3
        >>> solve(1)
        1
        >>> solve(0)
        0
    """
    if n <= 0:
        return 0

    # The number of perfect squares up to n is the floor of the square root of n.
    # For example, if n = 10, perfect squares are 1, 4, 9. floor(sqrt(10)) = 3.
    return int(math.isqrt(n))
