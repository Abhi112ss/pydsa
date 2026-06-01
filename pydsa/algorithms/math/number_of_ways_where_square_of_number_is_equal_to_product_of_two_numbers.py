METADATA = {
    "id": 1577,
    "name": "Number of Ways Where Square of Number Is Equal to Product of Two Numbers",
    "slug": "number-of-ways-where-square-of-number-is-equal-to-product-of-two-numbers",
    "category": "Math",
    "aliases": [],
    "tags": ["math", "hash_map"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Count pairs (i, j) such that nums[i]^2 == nums[i] * nums[j], which simplifies to finding pairs where nums[i] == nums[j].",
}

def solve(nums: list[int]) -> int:
    """
    Calculates the number of pairs (i, j) such that nums[i]^2 == nums[i] * nums[j].
    
    The condition nums[i]^2 == nums[i] * nums[j] is equivalent to:
    nums[i] * nums[i] == nums[i] * nums[j]
    
    If nums[i] != 0, we can divide both sides by nums[i], resulting in:
    nums[i] == nums[j]
    
    If nums[i] == 0, the condition becomes 0 == 0, which is always true for any nums[j].
    However, the problem implies we are looking for pairs (i, j) where i != j.
    
    Args:
        nums: A list of integers.
        
    Returns:
        The total number of pairs (i, j) with i != j satisfying the condition.
        
    Examples:
        >>> solve([1, 2, 2, 1])
        4
        # Pairs: (0,3), (1,2), (2,1), (3,0) -> [1,1], [2,2], [2,2], [1,1]
        >>> solve([3, 1, 2, 1, 3])
        2
        # Pairs: (0,4), (3,1) -> [3,3], [1,1]
    """
    counts: dict[int, int] = {}
    for num in nums:
        counts[num] = counts.get(num, 0) + 1
    
    total_ways: int = 0
    
    # Case 1: nums[i] is not zero.
    # We need nums[i] == nums[j]. For a number appearing 'k' times, 
    # there are k * (k - 1) ways to pick two distinct indices i and j.
    for val, count in counts.items():
        if val != 0:
            total_ways += count * (count - 1)
            
    # Case 2: nums[i] is zero.
    # If nums[i] is 0, then 0^2 == 0 * nums[j] is 0 == 0, which is true for ALL j != i.
    # If there are 'z' zeros in the array, each zero can be paired with any of the 
    # (n - 1) other elements in the array.
    zero_count = counts.get(0, 0)
    if zero_count > 0:
        n = len(nums)
        total_ways += zero_count * (n - 1)
        
    return total_ways
