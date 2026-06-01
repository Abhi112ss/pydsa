METADATA = {
    "id": 2702,
    "name": "Minimum Operations to Make Numbers Non-positive",
    "slug": "minimum_operations_to_make_numbers_non_positive",
    "category": "math",
    "aliases": [],
    "tags": ["math", "greedy"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Return the minimum number of operations to make all numbers non‑positive by repeatedly subtracting a fixed value.",
}


def solve(nums: list[int], x: int) -> int:
    """Calculate the minimum number of operations required to make all numbers
    in ``nums`` non‑positive by repeatedly subtracting ``x`` from any element.

    Args:
        nums: List of integers representing the initial values.
        x: Positive integer that is subtracted in each operation.

    Returns:
        The total minimum number of operations needed so that every element in
        ``nums`` becomes less than or equal to zero.

    Examples:
        >>> solve([1, 5, 2], 5)
        2
        >>> solve([10, 10, 10], 3)
        10
        >>> solve([-1, -2, -3], 4)
        0
    """
    total_operations = 0
    for value in nums:
        if value > 0:
            # Each positive value needs ceil(value / x) subtractions.
            operations_needed = (value + x - 1) // x
            total_operations += operations_needed
    return total_operations