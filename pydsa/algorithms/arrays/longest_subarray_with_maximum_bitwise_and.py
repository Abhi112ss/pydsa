METADATA = {
    "id": 2419,
    "name": "Longest Subarray With Maximum Bitwise AND",
    "slug": "longest_subarray_with_maximum_bitwise_and",
    "category": "array",
    "aliases": [],
    "tags": ["arrays"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the length of the longest consecutive subarray whose bitwise AND equals the maximum element in the array.",
}


def solve(nums: list[int]) -> int:
    """Return the length of the longest subarray whose bitwise AND equals the maximum value.

    Args:
        nums: List of non‑negative integers.

    Returns:
        The maximum length of a contiguous subarray where the bitwise AND of all
        elements equals the largest element in ``nums``. If ``nums`` is empty,
        returns ``0``.

    Examples:
        >>> solve([1,2,3,3,2,3,3,3])
        3
        >>> solve([0,0,0])
        3
        >>> solve([5,1,5,5,2,5])
        2
    """
    if not nums:
        return 0

    # The maximum possible bitwise AND is simply the maximum element.
    max_value = max(nums)

    longest = 0
    current = 0
    for number in nums:
        if number == max_value:
            # Extend the current run of maximum values.
            current += 1
            if current > longest:
                longest = current
        else:
            # Reset when the run is broken.
            current = 0

    return longest