METADATA = {
    "id": 2805,
    "name": "Custom Interval",
    "slug": "custom-interval",
    "category": "Implementation",
    "aliases": [],
    "tags": ["intervals", "implementation"],
    "difficulty": "easy",
    "time_complexity": "O(1)",
    "space_complexity": "O(1)",
    "description": "Given a custom interval [start, end], return the number of integers in the interval that are divisible by a given divisor.",
}


def solve(start: int, end: int, divisor: int) -> int:
    """
    Calculates the number of integers in the range [start, end] inclusive 
    that are divisible by the given divisor.

    Args:
        start: The starting integer of the interval.
        end: The ending integer of the interval.
        divisor: The integer to check divisibility against.

    Returns:
        The count of integers in [start, end] divisible by divisor.

    Examples:
        >>> solve(1, 10, 3)
        3
        >>> solve(10, 20, 5)
        3
        >>> solve(1, 1, 1)
        1
    """
    # The number of integers divisible by 'divisor' in the range [1, n] 
    # can be calculated using floor division: n // divisor.
    
    # To find the count in [start, end], we calculate the count up to 'end'
    # and subtract the count up to 'start - 1'.
    
    def count_divisible_up_to(n: int, d: int) -> int:
        if n < 0:
            return 0
        return n // d

    # We use the principle of inclusion-exclusion for ranges: 
    # Count(start, end) = Count(1, end) - Count(1, start - 1)
    return count_divisible_up_to(end, divisor) - count_divisible_up_to(start - 1, divisor)
