METADATA = {
    "id": 152,
    "name": "Maximum Product Subarray",
    "slug": "maximum-product-subarray",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dynamic_programming", "arrays"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find a contiguous non-empty subarray within an array that has the largest product.",
}

def solve(nums: list[int]) -> int:
    """
    Finds the contiguous subarray within an array that has the largest product.

    Args:
        nums: A list of integers.

    Returns:
        The maximum product found in any contiguous subarray.

    Examples:
        >>> solve([2, 3, -2, 4])
        6
        >>> solve([-2, 0, -1])
        0
        >>> solve([-2])
        -2
    """
    if not nums:
        return 0

    # Initialize the global maximum, and the running max/min products
    # We track the minimum because a negative number multiplied by a 
    # very small negative number can become a very large positive number.
    max_so_far = nums[0]
    min_so_far = nums[0]
    result = nums[0]

    for i in range(1, len(nums)):
        current_val = nums[i]

        # If the current value is negative, the max and min swap roles
        # when multiplied, so we swap them beforehand to simplify logic.
        if current_val < 0:
            max_so_far, min_so_far = min_so_far, max_so_far

        # The new max/min at this position is either the current element itself
        # (starting a new subarray) or the current element times the previous max/min.
        max_so_far = max(current_val, max_so_far * current_val)
        min_so_far = min(current_val, min_so_far * current_val)

        # Update the global maximum found across all subarrays
        result = max(result, max_so_far)

    return result
