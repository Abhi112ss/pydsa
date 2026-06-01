METADATA = {
    "id": 3152,
    "name": "Special Array II",
    "slug": "special-array-ii",
    "category": "Arrays",
    "aliases": [],
    "tags": ["arrays", "greedy"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Determine if an array is special such that for every index i, nums[i] > nums[i+1] or nums[i] < nums[i+1] in an alternating pattern.",
}

def solve(nums: list[int]) -> bool:
    """
    Determines if the given array is 'special'. 
    An array is special if for every index i (0 <= i < n-1), 
    the comparison sign between nums[i] and nums[i+1] is different 
    from the comparison sign between nums[i+1] and nums[i+2].
    
    Note: The problem definition implies that no two adjacent elements 
    can be equal, and the direction of inequality must alternate.

    Args:
        nums: A list of integers.

    Returns:
        True if the array follows the alternating inequality pattern, False otherwise.

    Examples:
        >>> solve([1, 4, 2, 5, 3])
        True
        >>> solve([1, 2, 3])
        False
        >>> solve([1, 1, 1])
        False
    """
    n = len(nums)
    if n < 2:
        return True

    # We track the direction of the previous comparison.
    # direction: 1 if nums[i] < nums[i+1], -1 if nums[i] > nums[i+1], 0 if equal.
    prev_direction = 0

    for i in range(n - 1):
        # Determine current direction
        if nums[i] < nums[i + 1]:
            current_direction = 1
        elif nums[i] > nums[i + 1]:
            current_direction = -1
        else:
            # If any two adjacent elements are equal, it's not special
            return False

        # If this isn't the first comparison, check if it flips from the previous one
        if prev_direction != 0 and current_direction == prev_direction:
            return False
        
        # Update the direction for the next iteration
        prev_direction = current_direction

    return True
