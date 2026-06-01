METADATA = {
    "id": 2529,
    "name": "Maximum Count of Positive Integer and Negative Integer",
    "slug": "maximum_count_of_positive_integer_and_negative_integer",
    "category": "array",
    "aliases": [],
    "tags": ["binary_search", "arrays"],
    "difficulty": "easy",
    "time_complexity": "O(log n)",
    "space_complexity": "O(1)",
    "description": "Return the larger count between negative and positive integers in a sorted array.",
}


def solve(nums: list[int]) -> int:
    """Count the maximum between negative and positive integers in a sorted list.

    Args:
        nums: A list of integers sorted in non‑decreasing order.

    Returns:
        The larger of the count of negative numbers and the count of positive numbers.

    Examples:
        >>> solve([-2, -1, -1, 0, 1, 2])
        3
        >>> solve([-3, -2, -1])
        3
        >>> solve([0, 0, 0])
        0
    """
    n = len(nums)

    # Find first index where value >= 0 (i.e., start of non‑negative numbers)
    left, right = 0, n
    while left < right:
        mid = (left + right) // 2
        if nums[mid] >= 0:
            right = mid
        else:
            left = mid + 1
    first_non_negative = left  # number of negative elements

    # Find first index where value > 0 (i.e., start of positive numbers)
    left, right = 0, n
    while left < right:
        mid = (left + right) // 2
        if nums[mid] > 0:
            right = mid
        else:
            left = mid + 1
    first_positive = left  # index of first positive element

    count_negative = first_non_negative
    count_positive = n - first_positive

    return max(count_negative, count_positive)