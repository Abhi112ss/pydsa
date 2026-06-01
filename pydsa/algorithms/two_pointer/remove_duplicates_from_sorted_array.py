METADATA = {
    "id": 26,
    "name": "Remove Duplicates from Sorted Array",
    "slug": "remove-duplicates-from-sorted-array",
    "category": "Arrays",
    "aliases": [],
    "tags": ["two_pointer", "arrays"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Remove duplicates in-place from a sorted array such that each unique element appears only once.",
}

def solve(nums: list[int]) -> int:
    """
    Removes duplicates from a sorted array in-place and returns the count of unique elements.

    The function uses a two-pointer approach to modify the input list such that the 
    first 'k' elements contain the unique elements in their original order.

    Args:
        nums: A list of integers sorted in non-decreasing order.

    Returns:
        int: The number of unique elements in the array.

    Examples:
        >>> nums = [1, 1, 2]
        >>> solve(nums)
        2
        >>> nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
        >>> solve(nums)
        5
    """
    if not nums:
        return 0

    # 'unique_index' tracks the position where the next unique element should be placed.
    # We start at 0 because the first element is always unique relative to nothing.
    unique_index = 0

    # 'scan_index' iterates through the array starting from the second element.
    for scan_index in range(1, len(nums)):
        # If the current element is different from the last unique element found...
        if nums[scan_index] != nums[unique_index]:
            # ...increment the unique pointer and update the value at that position.
            unique_index += 1
            nums[unique_index] = nums[scan_index]

    # The number of unique elements is the index + 1.
    return unique_index + 1
