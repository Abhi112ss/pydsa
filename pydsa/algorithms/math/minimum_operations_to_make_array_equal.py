METADATA = {
    "id": 1551,
    "name": "Minimum Operations to Make Array Equal",
    "slug": "minimum_operations_to_make_array_equal",
    "category": "array",
    "aliases": [],
    "tags": ["math", "greedy"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Calculate the minimal number of unit transfer operations to make all array elements equal.",
}


def solve(nums: list[int]) -> int:
    """Calculate the minimum number of operations required to make all elements of the array equal.

    Args:
        nums: List of integers representing the array.

    Returns:
        The minimal number of operations as an integer.

    Examples:
        >>> solve([1, 2, 3])
        1
        >>> solve([3, 2, 3])
        0
        >>> solve([1, 1, 1, 1])
        0
    """
    n = len(nums)
    total_sum = sum(nums)
    target = total_sum // n  # average value; problem guarantees divisibility
    # Each operation moves one unit from a larger element to a smaller one.
    # Summing excesses over the target gives the required number of operations.
    operations_needed = sum(num - target for num in nums if num > target)
    return operations_needed