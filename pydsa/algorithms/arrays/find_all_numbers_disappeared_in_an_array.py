METADATA = {
    "id": 448,
    "name": "Find All Numbers Disappeared in an Array",
    "slug": "find_all_numbers_disappeared_in_an_array",
    "category": "Array",
    "aliases": [],
    "tags": ["hash_map", "in_place"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Return all numbers in the range [1, n] that do not appear in the array.",
}


def solve(nums: list[int]) -> list[int]:
    """Find all numbers that are missing from the array.

    Args:
        nums: A list of integers where 1 ≤ nums[i] ≤ n (n = len(nums)).
              The list may contain duplicates.

    Returns:
        A list of the integers in the range [1, n] that do not appear in `nums`.
        The result is returned in ascending order.

    Examples:
        >>> solve([4,3,2,7,8,2,3,1])
        [5, 6]
        >>> solve([1,1])
        [2]
    """
    # First pass: use the sign of each element to record the presence of numbers.
    for index in range(len(nums)):
        value = abs(nums[index])
        target_index = value - 1
        # Mark the element at target_index as negative to indicate the number (target_index+1) exists.
        if nums[target_index] > 0:
            nums[target_index] = -nums[target_index]

    # Second pass: collect indices with positive values; those indices+1 are missing.
    missing_numbers: list[int] = []
    for index, value in enumerate(nums):
        if value > 0:
            missing_numbers.append(index + 1)

    return missing_numbers