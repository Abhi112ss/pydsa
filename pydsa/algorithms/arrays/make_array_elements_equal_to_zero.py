METADATA = {
    "id": 3354,
    "name": "Make Array Elements Equal to Zero",
    "slug": "make-array-elements-equal-to-zero",
    "category": "Array",
    "aliases": [],
    "tags": ["difference_array", "greedy", "array"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Determine if an array can be transformed into all zeros by repeatedly choosing an index and subtracting 1 from it and its neighbors.",
}

def solve(nums: list[int]) -> bool:
    """
    Determines if the array can be made all zeros using the specified operation.
    
    The operation allows choosing an index i and subtracting 1 from nums[i-1], 
    nums[i], and nums[i+1] (if they exist). This is equivalent to saying 
    each element nums[i] must be covered by operations centered at i-1, i, or i+1.
    
    To solve this greedily, we iterate through the array. For each element nums[i],
    if it is greater than 0, the only way to reduce it to 0 without affecting 
    elements before it (which are already processed) is to apply the operation 
    centered at i+1.

    Args:
        nums: A list of non-negative integers.

    Returns:
        True if the array can be made all zeros, False otherwise.

    Examples:
        >>> solve([1, 2, 1])
        True
        >>> solve([1, 1, 1])
        True
        >>> solve([1, 2, 3])
        False
    """
    n = len(nums)
    if n == 0:
        return True
    
    # current_diff tracks the cumulative effect of operations applied to 
    # the previous elements that still affect the current element.
    # Since an operation at i affects i-1, i, and i+1, an operation at i-1
    # affects i. An operation at i-2 affects i-1, but not i.
    # However, the standard greedy approach for this specific problem 
    # (where we decide the operation at i+1 based on nums[i]) 
    # is to treat it as: nums[i] must be zeroed out by operations at i-1, i, or i+1.
    
    # Let's use a simpler greedy: 
    # For each i from 0 to n-2:
    # If nums[i] > 0, we MUST apply the operation at i+1 to reduce nums[i] to 0.
    # This operation will reduce nums[i], nums[i+1], and nums[i+2].
    
    # We need to track how many operations are currently active on the current index.
    # active_ops_at_i tracks operations centered at i-1 and i.
    # But since we only care about the current index, we can just modify the array.
    
    # To keep space O(1), we modify nums in place.
    for i in range(n - 1):
        if nums[i] < 0:
            # If we ever encounter a negative number, it's impossible
            return False
        
        if nums[i] > 0:
            count = nums[i]
            # Apply 'count' operations centered at i+1
            # This affects i, i+1, and i+2
            nums[i] -= count
            nums[i + 1] -= count
            if i + 2 < n:
                nums[i + 2] -= count
                
    # After the loop, the only element that could be non-zero is the last one.
    # However, the last element nums[n-1] must also be exactly 0.
    # We also need to check if any element became negative during the process.
    
    # Re-check the whole array for any non-zero or negative values.
    # Actually, the loop above handles the reduction. We just need to check 
    # if the final state is all zeros.
    for val in nums:
        if val != 0:
            return False
            
    return True
