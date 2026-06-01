METADATA = {
    "id": 1228,
    "name": "Missing Number In Arithmetic Progression",
    "slug": "missing_number_in_arithmetic_progression",
    "category": "array",
    "aliases": [],
    "tags": ["math", "binary_search", "array"],
    "difficulty": "easy",
    "time_complexity": "O(log n)",
    "space_complexity": "O(1)",
    "description": "Find the missing element in an arithmetic progression represented by a sorted array.",
}


def solve(nums: list[int]) -> int:
    """Find the missing number in a sorted arithmetic progression.

    Args:
        nums: A list of unique integers forming an arithmetic progression
              with exactly one element missing. The list is sorted in
              ascending order.

    Returns:
        The integer value that is missing from the original progression.

    Examples:
        >>> solve([1, 3, 5, 7, 9, 11, 13, 15, 19])
        17
        >>> solve([5, 7, 9, 11, 13, 15, 17, 19])
        21
        >>> solve([2, 4, 6, 8, 10, 12, 14, 18])
        16
    """
    length = len(nums)
    if length == 0:
        raise ValueError("Input list must contain at least one element.")

    # The common difference of the original full progression.
    common_diff = (nums[-1] - nums[0]) // length

    left, right = 0, length - 1
    while left <= right:
        mid = (left + right) // 2
        expected_value = nums[0] + mid * common_diff

        if nums[mid] == expected_value:
            # Missing element is to the right of mid.
            left = mid + 1
        else:
            # Missing element is at mid or to the left.
            right = mid - 1

    # 'left' points to the position where the deviation occurs.
    return nums[0] + left * common_diff