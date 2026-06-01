METADATA = {
    "id": 2873,
    "name": "Maximum Value of an Ordered Triplet I",
    "slug": "maximum-value-of-an-ordered-triplet-i",
    "category": "Arrays",
    "aliases": [],
    "tags": ["arrays", "greedy"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the maximum value of nums[i] - nums[j] + nums[k] where i < j < k.",
}

def solve(nums: list[int]) -> int:
    """
    Calculates the maximum value of nums[i] - nums[j] + nums[k] for i < j < k.

    The algorithm uses a single pass to maintain the maximum possible values 
    for the sub-expressions encountered so far.

    Args:
        nums: A list of integers.

    Returns:
        The maximum value of the ordered triplet.

    Examples:
        >>> solve([12, 6, 1, 2, 7])
        10
        >>> solve([1, 1, 1, 1])
        1
    """
    # max_val tracks the largest nums[i] seen so far.
    max_val = float('-inf')
    
    # max_diff tracks the largest (nums[i] - nums[j]) seen so far where i < j.
    max_diff = float('-inf')
    
    # max_triplet tracks the largest (nums[i] - nums[j] + nums[k]) seen so far.
    max_triplet = float('-inf')

    for num in nums:
        # 1. Try to update the triplet value using the current number as nums[k].
        # This uses the best (nums[i] - nums[j]) found previously.
        if max_diff != float('-inf'):
            max_triplet = max(max_triplet, max_diff + num)
        
        # 2. Try to update the difference using the current number as nums[j].
        # This uses the best nums[i] found previously.
        if max_val != float('-inf'):
            max_diff = max(max_diff, max_val - num)
            
        # 3. Update the maximum single value seen so far to be used as nums[i].
        max_val = max(max_val, num)

    return int(max_triplet)
