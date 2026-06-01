METADATA = {
    "id": 3396,
    "name": "Minimum Number of Operations to Make Elements in Array Distinct",
    "slug": "minimum-number-of-operations-to-make-elements-in-array-distinct",
    "category": "Greedy",
    "aliases": [],
    "tags": ["greedy", "sorting"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(1)",
    "description": "Find the minimum number of operations to make all elements in an array distinct by increasing elements.",
}

def solve(nums: list[int]) -> int:
    """
    Calculates the minimum number of operations to make all elements in the array distinct.
    An operation consists of increasing an element by 1.

    Args:
        nums: A list of integers.

    Returns:
        The minimum number of operations required.

    Examples:
        >>> solve([1, 2, 2])
        1
        >>> solve([3, 2, 1, 2, 7])
        2
    """
    # Sort the array to process elements in non-decreasing order
    nums.sort()
    
    total_operations = 0
    
    # Iterate through the array starting from the second element
    for i in range(1, len(nums)):
        # If the current element is not greater than the previous element,
        # it must be increased to at least (previous_element + 1)
        if nums[i] <= nums[i - 1]:
            # Calculate the target value for the current element
            target_value = nums[i - 1] + 1
            
            # The difference is the number of operations needed for this element
            diff = target_value - nums[i]
            total_operations += diff
            
            # Update the current element in the array to its new value
            nums[i] = target_value
            
    return total_operations
