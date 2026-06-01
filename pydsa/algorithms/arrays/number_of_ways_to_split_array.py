METADATA = {
    "id": 2270,
    "name": "Number of Ways to Split Array",
    "slug": "number-of-ways-to-split-array",
    "category": "Array",
    "aliases": [],
    "tags": ["prefix_sum", "array"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Count the number of ways to split an array into two non-empty parts such that the sum of the first part is greater than or equal to the sum of the second part.",
}

def solve(nums: list[int]) -> int:
    """
    Calculates the number of ways to split the array into two non-empty parts
    where the sum of the left part is greater than or equal to the sum of the right part.

    Args:
        nums: A list of integers representing the array.

    Returns:
        The total number of valid split indices.

    Examples:
        >>> solve([10, 4, -8, 7])
        2
        >>> solve([1, 2, 3, 4, 5])
        0
    """
    # Calculate the total sum of the array first to avoid O(n^2) complexity
    total_sum = sum(nums)
    
    left_sum = 0
    valid_splits = 0
    
    # We iterate up to len(nums) - 1 because the right part must be non-empty
    for i in range(len(nums) - 1):
        left_sum += nums[i]
        
        # The right sum is simply the total sum minus the current left sum
        right_sum = total_sum - left_sum
        
        # Check the condition specified in the problem
        if left_sum >= right_sum:
            valid_splits += 1
            
    return valid_splits
