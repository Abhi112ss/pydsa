METADATA = {
    "id": 945,
    "name": "Minimum Increment to Make Array Unique",
    "slug": "minimum-increment-to-make-array-unique",
    "category": "Greedy",
    "aliases": [],
    "tags": ["sorting", "greedy"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(1)",
    "description": "Find the minimum number of increments needed to make all elements in an array unique.",
}

def solve(nums: list[int]) -> int:
    """
    Calculates the minimum number of increments required to make all elements in the array unique.

    The algorithm sorts the array first. Then, it iterates through the sorted array, 
    ensuring that each element is at least one greater than the previous element. 
    If an element is not greater, it is incremented to (previous_element + 1), 
    and the difference is added to the total count.

    Args:
        nums: A list of integers.

    Returns:
        The total number of increments performed.

    Examples:
        >>> solve([3, 2, 1, 2, 1, 7])
        6
        >>> solve([3, 2, 1, 2, 1, 7]) # Explanation: [1, 2, 3, 4, 5, 7], increments: 0+0+0+2+4+0 = 6
        >>> solve([1, 1, 1])
        3
    """
    if not nums:
        return 0

    # Sort the array to handle elements in non-decreasing order
    nums.sort()
    
    total_increments = 0
    
    # Iterate from the second element to the end
    for i in range(1, len(nums)):
        # If the current element is not strictly greater than the previous one
        if nums[i] <= nums[i - 1]:
            # Calculate what the current element should be to be unique
            target_value = nums[i - 1] + 1
            
            # The number of increments needed is the difference
            increments_needed = target_value - nums[i]
            total_increments += increments_needed
            
            # Update the current element in the array to reflect the increment
            nums[i] = target_value
            
    return total_increments
