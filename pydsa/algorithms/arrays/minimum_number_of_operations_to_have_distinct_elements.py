METADATA = {
    "id": 3779,
    "name": "Minimum Number of Operations to Have Distinct Elements",
    "slug": "minimum-number-of-operations-to-have-distinct-elements",
    "category": "Greedy",
    "aliases": [],
    "tags": ["greedy", "sorting"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(1)",
    "description": "Find the minimum number of operations to make all elements in an array distinct by incrementing elements.",
}

def solve(nums: list[int]) -> int:
    """
    Calculates the minimum number of operations to make all elements in the array distinct.
    An operation consists of incrementing an element by 1.

    Args:
        nums: A list of integers.

    Returns:
        The minimum number of operations required.

    Examples:
        >>> solve([1, 2, 2, 3])
        1
        >>> solve([1, 1, 1, 1])
        6
    """
    if not nums:
        return 0

    # Sort the array to process elements in non-decreasing order
    # This allows us to greedily ensure each element is greater than the previous one
    nums.sort()
    
    operations_count = 0
    
    # Iterate through the array starting from the second element
    for i in range(1, len(nums)):
        # If the current element is not strictly greater than the previous element
        if nums[i] <= nums[i - 1]:
            # Calculate the target value (previous element + 1)
            target_value = nums[i - 1] + 1
            # The number of operations is the difference between target and current
            diff = target_value - nums[i]
            operations_count += diff
            # Update the current element to its new value
            nums[i] = target_value
            
    return operations_count
