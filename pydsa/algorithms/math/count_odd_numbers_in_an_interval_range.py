METADATA = {
    "id": 1523,
    "name": "Count Odd Numbers in an Interval Range",
    "slug": "count_odd_numbers_in_an_interval_range",
    "category": "Math",
    "aliases": [],
    "tags": ["math"],
    "difficulty": "easy",
    "time_complexity": "O(1)",
    "space_complexity": "O(1)",
    "description": "Return the count of odd numbers within the inclusive interval [low, high].",
}


def solve(low: int, high: int) -> int:
    """Count odd numbers in the inclusive interval [low, high].

    Args:
        low: The lower bound of the interval (inclusive).
        high: The upper bound of the interval (inclusive).

    Returns:
        The number of odd integers between low and high inclusive.

    Examples:
        >>> solve(3, 7)
        3
        >>> solve(8, 10)
        1
    """
    # Count of odd numbers from 1 up to high.
    odd_up_to_high = (high + 1) // 2
    # Count of odd numbers from 1 up to low - 1.
    odd_up_to_before_low = low // 2
    # Difference gives odds within [low, high].
    return odd_up_to_high - odd_up_to_before_low