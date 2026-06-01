METADATA = {
    "id": 3862,
    "name": "Find the Smallest Balanced Index",
    "slug": "find_the_smallest_balanced_index",
    "category": "Array",
    "aliases": [],
    "tags": ["prefix_sum", "array"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the smallest index such that the sum of elements before it equals the sum of elements after it.",
}

def solve(nums: list[int]) -> int:
    """
    Finds the smallest index such that the sum of elements to the left 
    of the index is equal to the sum of elements to the right.

    Args:
        nums: A list of integers.

    Returns:
        The smallest balanced index if it exists, otherwise -1.

    Examples:
        >>> solve([1, 7, 3, 6, 5, 6])
        3
        >>> solve([1, 2, 3])
        -1
        >>> solve([2, 1, -1])
        0
    """
    total_sum = sum(nums)
    left_sum = 0

    for index, current_value in enumerate(nums):
        # The right sum is the total sum minus the left sum and the current element
        right_sum = total_sum - left_sum - current_value

        # Check if the equilibrium condition is met
        if left_sum == right_sum:
            return index

        # Update the running prefix sum for the next iteration
        left_sum += current_value

    return -1
