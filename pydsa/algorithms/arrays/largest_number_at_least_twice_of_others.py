METADATA = {
    "id": 747,
    "name": "Largest Number At Least Twice of Others",
    "slug": "largest_number_at_least_twice_of_others",
    "category": "Array",
    "aliases": ["dominant_index", "largest_number_twice_others"],
    "tags": ["array_traversal"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Return the index of the largest element if it is at least twice as large as every other element, otherwise return -1.",
}


def solve(nums: list[int]) -> int:
    """Find the index of the dominant element that is at least twice all others.

    Args:
        nums: A list of non-negative integers with at least one element.

    Returns:
        The index of the largest element if it is at least twice every other element,
        or -1 if no such element exists.

    Examples:
        >>> solve([3, 6, 1, 0])
        1
        >>> solve([1, 2, 3, 4])
        -1
        >>> solve([1])
        0
        >>> solve([0, 0, 3, 2])
        -1
    """
    if len(nums) == 1:
        return 0

    # Track the largest and second-largest values and the index of the largest
    if nums[0] >= nums[1]:
        largest_val = nums[0]
        largest_idx = 0
        second_largest = nums[1]
    else:
        largest_val = nums[1]
        largest_idx = 1
        second_largest = nums[0]

    # Single pass: update largest and second-largest as we scan
    for i in range(2, len(nums)):
        current = nums[i]
        if current > largest_val:
            # New largest found; old largest becomes second-largest
            second_largest = largest_val
            largest_val = current
            largest_idx = i
        elif current > second_largest:
            second_largest = current

    # The largest must be at least twice the second-largest to dominate all others
    if largest_val >= 2 * second_largest:
        return largest_idx
    return -1