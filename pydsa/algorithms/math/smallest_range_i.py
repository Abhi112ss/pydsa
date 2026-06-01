METADATA = {
    "id": 908,
    "name": "Smallest Range I",
    "slug": "smallest_range_i",
    "category": "array",
    "aliases": [],
    "tags": ["math", "greedy"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the minimal possible difference between the maximum and minimum values after adjusting each element by at most k.",
}


def solve(nums: list[int], k: int) -> int:
    """Return the smallest possible range after modifying each element by at most k.

    Args:
        nums: List of integers representing the original array.
        k: Non‑negative integer indicating the maximum amount each element can be increased
           or decreased.

    Returns:
        The minimal possible difference between the maximum and minimum values of the
        array after the allowed modifications.

    Examples:
        >>> solve([1, 3, 6], 3)
        0
        >>> solve([0, 10, 5], 2)
        6
    """
    # Find current minimum and maximum in a single pass.
    current_min = nums[0]
    current_max = nums[0]
    for value in nums[1:]:
        if value < current_min:
            current_min = value
        elif value > current_max:
            current_max = value

    # The best we can do is raise the minimum by k and lower the maximum by k.
    # If the adjusted max is not greater than the adjusted min, the range can be zero.
    adjusted_range = current_max - current_min - 2 * k
    return max(0, adjusted_range)