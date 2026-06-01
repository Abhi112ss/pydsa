METADATA = {
    "id": 80,
    "name": "Remove Duplicates from Sorted Array II",
    "slug": "remove-duplicates-from-sorted-array-ii",
    "category": "Array",
    "aliases": [],
    "tags": ["two_pointer", "array"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Given a sorted array, remove duplicates in-place such that each unique element appears at most twice.",
}

def solve(nums: list[int]) -> int:
    """
    Removes duplicates from a sorted array in-place such that each unique 
    element appears at most twice.

    Args:
        nums: A list of integers sorted in non-decreasing order.

    Returns:
        The number of elements in the modified array after removing duplicates.

    Examples:
        >>> nums = [1, 1, 1, 2, 2, 3]
        >>> solve(nums)
        5
        >>> nums[:5]
        [1, 1, 2, 2, 3]

        >>> nums = [0, 0, 1, 1, 1, 1, 2, 3, 3]
        >>> solve(nums)
        7
        >>> nums[:7]
        [0, 0, 1, 1, 2, 3, 3]
    """
    # If the array has 2 or fewer elements, it already satisfies the condition.
    if len(nums) <= 2:
        return len(nums)

    # 'write_index' tracks the position where the next valid element should be placed.
    # We start from index 2 because the first two elements are always allowed.
    write_index = 2

    # Iterate through the array starting from the third element.
    for read_index in range(2, len(nums)):
        # Compare the current element with the element two positions behind 
        # the current write position. If they are different, it means the 
        # current element has appeared at most once in the 'valid' portion.
        if nums[read_index] != nums[write_index - 2]:
            nums[write_index] = nums[read_index]
            write_index += 1

    return write_index
