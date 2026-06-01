METADATA = {
    "id": 2936,
    "name": "Number of Equal Numbers Blocks",
    "slug": "number-of-equal-numbers-blocks",
    "category": "Array",
    "aliases": [],
    "tags": ["array", "two_pointer", "linear_scan"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Count the number of contiguous blocks of equal numbers in an array.",
}

def solve(nums: list[int]) -> int:
    """
    Counts the number of contiguous blocks of equal numbers in the given array.

    A block is defined as a maximal contiguous subarray where all elements are equal.

    Args:
        nums: A list of integers.

    Returns:
        The total number of equal number blocks.

    Examples:
        >>> solve([1, 1, 2, 3, 3, 3, 4])
        4
        >>> solve([1, 1, 1, 1])
        1
        >>> solve([1, 2, 3, 4])
        4
        >>> solve([])
        0
    """
    if not nums:
        return 0

    # Every non-empty array has at least one block starting with the first element
    block_count = 1

    # Iterate through the array starting from the second element
    for index in range(1, len(nums)):
        # If the current element is different from the previous one, 
        # it marks the start of a new block
        if nums[index] != nums[index - 1]:
            block_count += 1

    return block_count
