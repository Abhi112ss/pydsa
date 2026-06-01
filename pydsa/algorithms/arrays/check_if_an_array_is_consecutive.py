METADATA = {
    "id": 2229,
    "name": "Check if an Array Is Consecutive",
    "slug": "check_if_an_array_is_consecutive",
    "category": "Array",
    "aliases": [],
    "tags": ["hash_set", "math"],
    "difficulty": "Easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Determine whether an array can be reordered to form a consecutive sequence of integers.",
}

def solve(nums: list[int]) -> bool:
    """Check if the given array can be reordered to form a consecutive sequence.

    Args:
        nums: List of integers.

    Returns:
        True if the array contains unique elements and the range between the
        maximum and minimum element equals len(nums) - 1; otherwise False.

    Examples:
        >>> solve([5, 2, 3, 4])
        True
        >>> solve([1, 2, 4, 5])
        False
        >>> solve([1, 1, 2, 3])
        False
    """
    if not nums:
        return True  # empty array trivially satisfies the condition

    unique_elements = set()
    minimum_value = nums[0]
    maximum_value = nums[0]

    for number in nums:
        # track min and max while building the set
        if number < minimum_value:
            minimum_value = number
        elif number > maximum_value:
            maximum_value = number
        unique_elements.add(number)

    # condition 1: all elements must be unique
    if len(unique_elements) != len(nums):
        return False

    # condition 2: range must match length-1 for a consecutive sequence
    return maximum_value - minimum_value == len(nums) - 1