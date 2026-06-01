METADATA = {
    "id": 3891,
    "name": "Minimum Increase to Maximize Special Indices",
    "slug": "minimum-increase-to-maximize-special-indices",
    "category": "Greedy",
    "aliases": [],
    "tags": ["greedy", "arrays"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the minimum total increment needed to make all special indices strictly increasing.",
}

def solve(nums: list[int]) -> int:
    """
    Calculates the minimum total increment required to make all special indices 
    in the array strictly increasing.

    A special index is defined as an index 'i' such that 'i' is even and 
    'nums[i]' is greater than all previous elements in the array. However, 
    the problem context implies we need to ensure that for all even indices 'i', 
    nums[i] > nums[i-1] (if i > 0) and specifically that the sequence of 
    values at special indices is strictly increasing.

    Args:
        nums: A list of integers representing the input array.

    Returns:
        The minimum total increment needed.

    Examples:
        >>> solve([1, 2, 3, 4, 5])
        0
        >>> solve([5, 4, 3, 2, 1])
        10
    """
    total_increment = 0
    # The problem asks to ensure that for every even index i, 
    # nums[i] is greater than the previous special index's value.
    # We track the 'current_required_min' which is the value the 
    # current special index must at least be.
    current_required_min = -float('inf')

    for i in range(len(nums)):
        # Special indices are defined as even indices in this context
        if i % 2 == 0:
            # If the current value is not greater than the previous special index value,
            # we must increase it to current_required_min + 1
            if nums[i] <= current_required_min:
                needed_value = current_required_min + 1
                diff = needed_value - nums[i]
                total_increment += diff
                # Update the current element's value conceptually
                current_val = needed_value
            else:
                current_val = nums[i]
            
            # The next special index must be strictly greater than this one
            current_required_min = current_val
            
    return total_increment
