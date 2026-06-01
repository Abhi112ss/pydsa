METADATA = {
    "id": 1413,
    "name": "Minimum Value to Get Positive Step by Step Sum",
    "slug": "minimum-value-to-get-positive-step-by-step-sum",
    "category": "Array",
    "aliases": [],
    "tags": ["array", "prefix sum"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the minimum positive starting value such that the step-by-step sum remains at least 1 throughout the array traversal.",
}

def solve(nums: list[int]) -> int:
    """
    Calculates the minimum positive starting value required to ensure 
    the running sum never drops below 1.

    Args:
        nums: A list of integers representing the step changes.

    Returns:
        The minimum positive integer starting value.

    Examples:
        >>> solve([-3, 2, -3, 4, 2])
        5
        >>> solve([1, 2])
        1
        >>> solve([1, -2, -3])
        5
    """
    current_running_sum = 0
    min_prefix_sum = 0

    # Iterate through the array to track the lowest point the sum reaches
    for change in nums:
        current_running_sum += change
        if current_running_sum < min_prefix_sum:
            min_prefix_sum = current_running_sum

    # If the minimum prefix sum is negative, we need a starting value 
    # that offsets it to at least 1. 
    # If min_prefix_sum is 0 or positive, the minimum starting value is 1.
    # Formula: start_value + min_prefix_sum >= 1  =>  start_value >= 1 - min_prefix_sum
    return max(1, 1 - min_prefix_sum)
