METADATA = {
    "id": 2733,
    "name": "Neither Minimum nor Maximum",
    "slug": "neither-minimum-nor-maximum",
    "category": "Arrays",
    "aliases": [],
    "tags": ["arrays"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find an element in an array that is neither the minimum nor the maximum value.",
}

def solve(nums: list[int]) -> int:
    """
    Finds an element in the list that is neither the minimum nor the maximum.

    Args:
        nums: A list of integers where len(nums) >= 3 and all elements are distinct.

    Returns:
        An integer that is not the minimum and not the maximum of the list.

    Examples:
        >>> solve([1, 2, 3, 4])
        2
        >>> solve([10, 5, 20])
        5
    """
    # Initialize min and max with the first element
    current_min = nums[0]
    current_max = nums[0]

    # Single pass to find the global minimum and maximum
    for num in nums:
        if num < current_min:
            current_min = num
        if num > current_max:
            current_max = num

    # Iterate again to find the first element that satisfies the condition
    # Since len(nums) >= 3 and elements are distinct, such an element must exist
    for num in nums:
        if current_min < num < current_max:
            return num

    # This part is unreachable given the problem constraints
    return -1