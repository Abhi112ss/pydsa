METADATA = {
    "id": 217,
    "name": "Contains Duplicate",
    "slug": "contains_duplicate",
    "category": "Array",
    "aliases": [],
    "tags": ["hash_set", "sorting"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.",
}


def solve(nums: list[int]) -> bool:
    """Determine if the array contains any duplicate elements.

    Args:
        nums: An integer array to check for duplicates.

    Returns:
        True if any value appears at least twice, False if all elements are distinct.

    Examples:
        >>> solve([1, 2, 3, 1])
        True
        >>> solve([1, 2, 3, 4])
        False
        >>> solve([1, 1, 1, 3, 3, 4, 3, 2, 4, 2])
        True
    """
    seen = set()
    for num in nums:
        # If the element is already in the set, we found a duplicate
        if num in seen:
            return True
        seen.add(num)
    return False