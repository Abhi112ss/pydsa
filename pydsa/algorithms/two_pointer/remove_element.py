METADATA = {
    "id": 27,
    "name": "Remove Element",
    "slug": "remove_element",
    "category": "Arrays",
    "aliases": [],
    "tags": ["two_pointer", "arrays"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Remove all occurrences of a specific value in an array in-place and return the new length.",
}

def solve(nums: list[int], val: int) -> int:
    """
    Removes all occurrences of 'val' in 'nums' in-place and returns the new length.

    The function uses a two-pointer approach where one pointer iterates through 
    the array and the other tracks the position for the next valid (non-target) element.

    Args:
        nums: A list of integers to be modified in-place.
        val: The integer value to be removed from the list.

    Returns:
        int: The number of elements in 'nums' which are not equal to 'val'.

    Examples:
        >>> nums = [3, 2, 2, 3]
        >>> solve(nums, 3)
        2
        >>> nums[:2]  # Output could be [2, 2]
        [2, 2]

        >>> nums = [0, 1, 2, 2, 3, 0, 4, 2]
        >>> solve(nums, 2)
        5
        >>> nums[:5]  # Output could be [0, 1, 3, 0, 4]
        [0, 1, 3, 0, 4]
    """
    # 'write_index' tracks the position where the next non-target element should be placed
    write_index = 0

    for current_index in range(len(nums)):
        # If the current element is not the value we want to remove
        if nums[current_index] != val:
            # Move the valid element to the write_index position
            nums[write_index] = nums[current_index]
            # Increment the write_index to prepare for the next valid element
            write_index += 1

    return write_index
