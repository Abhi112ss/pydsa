METADATA = {
    "id": 3151,
    "name": "Special Array I",
    "slug": "special-array-i",
    "category": "Arrays",
    "aliases": [],
    "tags": ["arrays", "implementation"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Determine if an array is special, meaning every element is either strictly greater than or strictly less than its neighbors.",
}

def solve(nums: list[int]) -> bool:
    """
    Determines if the given array is 'special'. 
    An array is special if every element is either strictly greater than 
    or strictly less than its immediate neighbors.

    Args:
        nums: A list of integers.

    Returns:
        True if the array is special, False otherwise.

    Examples:
        >>> solve([1, 2, 1, 2])
        True
        >>> solve([1, 2, 3])
        False
        >>> solve([1, 1])
        False
    """
    n = len(nums)
    
    # An array with fewer than 2 elements is vacuously special 
    # based on the definition of neighbors, but constraints usually imply n >= 2.
    if n < 2:
        return True

    # Iterate through the array and check the relationship between adjacent elements.
    # For an array to be special, the direction of the inequality must flip 
    # at every step (e.g., up, down, up, down OR down, up, down, up).
    # This is equivalent to saying no two adjacent elements are equal 
    # AND no three consecutive elements are monotonic.
    
    # A simpler way to check the "strictly greater or strictly less" condition:
    # For every index i from 0 to n-2, nums[i] must not equal nums[i+1].
    # Additionally, the pattern must alternate.
    
    for i in range(n - 1):
        # If any two adjacent elements are equal, it's not special.
        if nums[i] == nums[i + 1]:
            return False
        
        # If we are not at the last pair, check if the direction changes.
        # The direction (up or down) between i and i+1 must be different 
        # from the direction between i+1 and i+2.
        if i < n - 2:
            # Check if the sequence is monotonic (e.g., 1 < 2 < 3 or 3 > 2 > 1)
            # If (nums[i+1] - nums[i]) and (nums[i+2] - nums[i+1]) have the same sign,
            # it means the direction did not flip.
            is_increasing = nums[i] < nums[i + 1] < nums[i + 2]
            is_decreasing = nums[i] > nums[i + 1] > nums[i + 2]
            
            if is_increasing or is_decreasing:
                return False
                
    return True
