METADATA = {
    "id": 1317,
    "name": "Convert Integer to the Sum of Two No-Zero Integers",
    "slug": "convert_integer_to_the_sum_of_two_no_zero_integers",
    "category": "math",
    "aliases": [],
    "tags": ["math", "simulation"],
    "difficulty": "easy",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(1)",
    "description": "Find two positive integers without zero digits that sum to n.",
}


def solve(n: int) -> list[int]:
    """Return a pair of positive integers whose sum equals ``n`` and
    neither integer contains the digit ``0``.

    Args:
        n: The target sum (1 ≤ n ≤ 10⁹).

    Returns:
        A list ``[a, b]`` such that ``a + b == n`` and both ``a`` and ``b``
        have no zero digit. The pair is guaranteed to exist.

    Examples:
        >>> solve(101)
        [99, 2]
        >>> solve(1000)
        [999, 1]
    """
    def contains_zero(number: int) -> bool:
        """Check whether ``number`` has any digit equal to zero."""
        while number:
            if number % 10 == 0:
                return True
            number //= 10
        return False

    # Iterate from 1 up to n//2; the first valid pair can be returned immediately.
    for candidate in range(1, n // 2 + 1):
        complement = n - candidate
        # Ensure both numbers have no zero digit.
        if not contains_zero(candidate) and not contains_zero(complement):
            return [candidate, complement]

    # According to the problem statement a solution always exists,
    # but the loop above should have returned already.
    raise ValueError("No valid pair found for the given input.")