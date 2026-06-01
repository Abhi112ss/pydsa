METADATA = {
    "id": 3229,
    "name": "Minimum Operations to Make Array Equal to Target",
    "slug": "minimum-operations-to-make-array-equal-to-target",
    "category": "Arrays",
    "aliases": [],
    "tags": ["arrays", "greedy", "math"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the minimum number of operations to make an array equal to a target array where an operation consists of incrementing a subarray by 1.",
}

def solve(nums: list[int], target: list[int]) -> int:
    """
    Calculates the minimum number of operations to transform nums into target.
    An operation consists of choosing a subarray and incrementing all its elements by 1.

    Args:
        nums: The initial array of integers.
        target: The target array of integers.

    Returns:
        The minimum number of operations required.

    Raises:
        ValueError: If target[i] < nums[i] for any index i, as we can only increment.

    Examples:
        >>> solve([1, 2, 3], [2, 3, 4])
        1
        >>> solve([1, 1, 1], [2, 3, 2])
        3
    """
    n = len(nums)
    total_operations = 0
    current_needed_diff = 0

    for i in range(n):
        # Calculate how much each element needs to be increased
        diff = target[i] - nums[i]
        
        if diff < 0:
            raise ValueError("Target element cannot be smaller than the initial element.")

        # If the current required difference is greater than the previous one,
        # it means we must start 'diff - current_needed_diff' new subarray operations.
        if diff > current_needed_diff:
            total_operations += (diff - current_needed_diff)
        
        # Update the current active increment level for the next iteration.
        # If diff < current_needed_diff, the existing subarray operations 
        # simply 'end' at this index, so we don't add to total_operations.
        current_needed_diff = diff

    return total_operations
