METADATA = {
    "id": 3021,
    "name": "Alice and Bob Playing Flower Game",
    "slug": "alice-and-bob-playing-flower-game",
    "category": "Math",
    "aliases": [],
    "tags": ["math", "combinatorics"],
    "difficulty": "medium",
    "time_complexity": "O(1)",
    "space_complexity": "O(1)",
    "description": "Count pairs (x, y) such that 1 <= x <= n, 1 <= y <= m, and x + y is odd.",
}

def solve(n: int, m: int) -> int:
    """
    Calculates the number of pairs (x, y) such that 1 <= x <= n, 1 <= y <= m,
    and the sum x + y is odd.

    A sum x + y is odd if and only if one number is even and the other is odd.
    There are two possible scenarios:
    1. x is odd and y is even.
    2. x is even and y is odd.

    Args:
        n (int): The upper bound for the first number x.
        m (int): The upper bound for the second number y.

    Returns:
        int: The total number of valid pairs (x, y).

    Examples:
        >>> solve(3, 2)
        3
        # Pairs: (1, 2), (2, 1), (3, 2)
        >>> solve(1, 1)
        0
    """
    # Count odd and even numbers in range [1, n]
    # For any range [1, k], there are (k + 1) // 2 odd numbers
    # and k // 2 even numbers.
    n_odd = (n + 1) // 2
    n_even = n // 2

    # Count odd and even numbers in range [1, m]
    m_odd = (m + 1) // 2
    m_even = m // 2

    # Total pairs (x, y) where x + y is odd:
    # (x is odd AND y is even) OR (x is even AND y is odd)
    return (n_odd * m_even) + (n_even * m_odd)
