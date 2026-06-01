METADATA = {
    "id": 3880,
    "name": "Minimum Absolute Difference Between Two Values",
    "slug": "minimum-absolute-difference-between-two-values",
    "category": "Array",
    "aliases": [],
    "tags": ["sorting", "arrays"],
    "difficulty": "easy",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(1)",
    "description": "Find the minimum absolute difference between any two elements in an array.",
}

def solve(nums: list[int]) -> int:
    """
    Finds the minimum absolute difference between any two elements in the given list.

    Args:
        nums: A list of integers.

    Returns:
        The minimum absolute difference found between any two elements.

    Examples:
        >>> solve([4, 2, 1, 3])
        1
        >>> solve([10, 20, 30, 40])
        10
        >>> solve([1, 1, 1])
        0
    """
    if len(nums) < 2:
        return 0

    # Sort the array to ensure that the closest values are adjacent
    nums.sort()

    # Initialize min_diff with a very large value
    min_diff = float('inf')

    # Iterate through the sorted array and compare adjacent elements
    for i in range(len(nums) - 1):
        current_diff = nums[i + 1] - nums[i]
        if current_diff < min_diff:
            min_diff = current_diff
            
        # Optimization: if we find a difference of 0, it's the smallest possible
        if min_diff == 0:
            return 0

    return int(min_diff)
