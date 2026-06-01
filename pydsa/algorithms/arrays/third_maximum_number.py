METADATA = {
    "id": 414,
    "name": "Third Maximum Number",
    "slug": "third_maximum_number",
    "category": "Array",
    "aliases": [],
    "tags": ["sorting", "set"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Return the third distinct maximum number in an array, or the maximum if fewer than three distinct numbers exist.",
}


def solve(nums: list[int]) -> int:
    """Find the third distinct maximum number in a list.

    Args:
        nums: List of integers.

    Returns:
        The third distinct maximum integer if it exists; otherwise, the maximum integer.

    Examples:
        >>> solve([3, 2, 1])
        1
        >>> solve([1, 2])
        2
        >>> solve([2, 2, 3, 1])
        1
    """
    first_max: int | None = None
    second_max: int | None = None
    third_max: int | None = None

    for number in nums:
        # Skip duplicates of any of the top three values
        if number == first_max or number == second_max or number == third_max:
            continue

        if first_max is None or number > first_max:
            # Shift down the previous maxima
            third_max = second_max
            second_max = first_max
            first_max = number
        elif second_max is None or number > second_max:
            third_max = second_max
            second_max = number
        elif third_max is None or number > third_max:
            third_max = number

    # If third distinct maximum does not exist, return the first maximum
    return third_max if third_max is not None else first_max  # type: ignore