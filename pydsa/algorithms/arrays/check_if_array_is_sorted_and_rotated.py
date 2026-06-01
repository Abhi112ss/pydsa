METADATA = {
    "id": 1752,
    "name": "Check if Array Is Sorted and Rotated",
    "slug": "check_if_array_is_sorted_and_rotated",
    "category": "array",
    "aliases": [],
    "tags": ["array"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Determine whether a given array is sorted in non‑decreasing order and possibly rotated.",
}


def solve(nums: list[int]) -> bool:
    """Check if the given array is sorted in non-decreasing order and possibly rotated.

    Args:
        nums: List of integers to evaluate.

    Returns:
        True if the array can be obtained by taking a non-decreasing sorted array
        and rotating it any number of times (including zero); otherwise False.

    Examples:
        >>> solve([3, 4, 5, 1, 2])
        True
        >>> solve([2, 1, 3, 4])
        False
        >>> solve([1, 2, 3])
        True
    """
    # An array with 0 or 1 elements is trivially sorted and rotated.
    if len(nums) <= 1:
        return True

    drop_count = 0
    for index in range(len(nums) - 1):
        # Count positions where the current element is greater than the next.
        if nums[index] > nums[index + 1]:
            drop_count += 1
            # Early exit if more than one drop is found.
            if drop_count > 1:
                return False

    # Check the wrap‑around case: last element compared to first element.
    if nums[-1] > nums[0]:
        drop_count += 1

    # The array is valid if there is at most one drop in total.
    return drop_count <= 1