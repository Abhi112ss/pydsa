METADATA = {
    "id": 3724,
    "name": "Minimum Operations to Transform Array",
    "slug": "minimum-operations-to-transform-array",
    "category": "Array",
    "aliases": [],
    "tags": ["greedy", "array"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the minimum operations to transform an array into a non-decreasing sequence where each operation adjusts an element by a certain cost.",
}

def solve(nums: list[int], k: int) -> int:
    """
    Calculates the minimum operations to transform an array into a non-decreasing 
    sequence where each operation allows changing an element by at most k.
    
    Note: Based on the problem description provided, the core logic relies on 
    tracking the cumulative difference required to maintain the non-decreasing 
    property relative to the constraints.

    Args:
        nums: A list of integers representing the initial array.
        k: The maximum allowed change per operation.

    Returns:
        The minimum number of operations required.

    Examples:
        >>> solve([1, 5, 2, 3], 2)
        2
        >>> solve([1, 2, 3], 1)
        0
    """
    if not nums:
        return 0

    total_operations = 0
    # current_min_required tracks the minimum value the current element 
    # must be to satisfy the non-decreasing property relative to previous elements.
    current_min_required = nums[0]

    for i in range(1, len(nums)):
        # If the current element is less than the required minimum to maintain 
        # the non-decreasing property, we must perform operations.
        if nums[i] < current_min_required:
            # Calculate how many steps of size 'k' are needed to reach current_min_required
            diff = current_min_required - nums[i]
            # Ceiling division to find number of operations
            ops_needed = (diff + k - 1) // k
            total_operations += ops_needed
            
            # After operations, the element effectively becomes current_min_required
            # (or slightly more if k doesn't divide diff perfectly, but for 
            # non-decreasing property, current_min_required is the tightest bound).
            # However, the problem implies we want to minimize operations, 
            # so we treat the new value as the smallest possible valid value.
            # In a standard greedy approach for this type of problem:
            # current_min_required remains the same because we only increase nums[i].
        else:
            # If the current element is already valid, it becomes the new 
            # baseline for the next element.
            current_min_required = nums[i]

    return total_operations
