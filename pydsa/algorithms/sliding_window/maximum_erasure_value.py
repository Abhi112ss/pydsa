METADATA = {
    "id": 1695,
    "name": "Maximum Erasure Value",
    "slug": "maximum_erasure_value",
    "category": "array",
    "aliases": [],
    "tags": ["sliding_window", "hash_set"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Find the maximum sum of a subarray with all unique elements.",
}


def solve(nums: list[int]) -> int:
    """Return the maximum sum of a subarray containing only unique elements.

    Args:
        nums: List of non‑negative integers.

    Returns:
        The largest possible sum of a contiguous subarray where each element
        appears at most once.

    Examples:
        >>> solve([4,2,4,5,6])
        17
        >>> solve([5,2,1,2,5,2,1,2,5])
        8
    """
    left_index: int = 0
    current_sum: int = 0
    max_sum: int = 0
    seen: set[int] = set()

    for right_index, value in enumerate(nums):
        # If value already in the window, shrink from the left until it is removed.
        while value in seen:
            left_value = nums[left_index]
            seen.remove(left_value)
            current_sum -= left_value
            left_index += 1
        # Add the new unique value to the window.
        seen.add(value)
        current_sum += value
        # Update the answer with the best sum seen so far.
        if current_sum > max_sum:
            max_sum = current_sum

    return max_sum