METADATA = {
    "id": 2460,
    "name": "Apply Operations to an Array",
    "slug": "apply_operations_to_an_array",
    "category": "array",
    "aliases": [],
    "tags": ["arrays"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Multiply adjacent equal elements, set the second to zero, then shift all zeros to the end.",
}


def solve(nums: list[int]) -> list[int]:
    """Apply the defined operations to the input array.

    Args:
        nums: A list of integers representing the original array.

    Returns:
        The array after performing the multiplication pass and shifting all zeros
        to the end while preserving the order of non‑zero elements.

    Examples:
        >>> solve([2,2,1,0])
        [4,1,0,0]
        >>> solve([0,1,2,3,4])
        [0,1,2,3,4]
        >>> solve([1,1,1,1])
        [2,2,0,0]
    """
    length = len(nums)

    # First pass: multiply adjacent equal elements and zero out the second one.
    for i in range(length - 1):
        if nums[i] == nums[i + 1]:
            nums[i] *= 2
            nums[i + 1] = 0

    # Second pass: shift all non‑zero values to the front using two‑pointer technique.
    write_index = 0
    for value in nums:
        if value != 0:
            nums[write_index] = value
            write_index += 1

    # Fill the remaining positions with zeros.
    while write_index < length:
        nums[write_index] = 0
        write_index += 1

    return nums