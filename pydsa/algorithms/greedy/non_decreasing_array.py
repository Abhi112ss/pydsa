METADATA = {
    "id": 665,
    "name": "Non-decreasing Array",
    "slug": "non-decreasing-array",
    "category": "Array",
    "aliases": [],
    "tags": ["greedy", "arrays"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Determine if an array can become non-decreasing by modifying at most one element.",
}

def solve(nums: list[int]) -> bool:
    """
    Determines if the array can become non-decreasing by modifying at most one element.

    Args:
        nums: A list of integers.

    Returns:
        True if the array can be made non-decreasing by modifying at most one element, 
        False otherwise.

    Examples:
        >>> solve([4, 2, 3])
        True
        >>> solve([4, 3, 2, 1])
        False
    """
    modification_count = 0
    
    for i in range(1, len(nums)):
        # Check if the current element violates the non-decreasing property
        if nums[i] < nums[i - 1]:
            modification_count += 1
            
            # If we have already modified an element, we cannot modify another
            if modification_count > 1:
                return False
            
            # We have two choices to fix the violation nums[i-1] > nums[i]:
            # 1. Lower nums[i-1] to match nums[i] (if nums[i-2] <= nums[i])
            # 2. Raise nums[i] to match nums[i-1] (if nums[i-1] <= nums[i+1])
            
            # Check if we can lower the previous element without breaking the sequence
            # This is possible if i is the first element (i=1) or if the element 
            # before the previous one is less than or equal to the current element.
            if i >= 2 and nums[i - 2] > nums[i]:
                # If we can't lower nums[i-1], we must raise nums[i]
                nums[i] = nums[i - 1]
            else:
                # Otherwise, we greedily lower nums[i-1] to nums[i] to keep 
                # the values as small as possible for future elements.
                nums[i - 1] = nums[i]
                
    return True
