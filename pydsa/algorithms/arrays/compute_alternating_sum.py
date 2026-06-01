METADATA = {
    "id": 3701,
    "name": "Compute Alternating Sum",
    "slug": "compute_alternating_sum",
    "category": "Arrays",
    "aliases": [],
    "tags": ["prefix_sum", "arrays", "math"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Calculate the alternating sum of an array where elements are added or subtracted based on their index parity.",
}

def solve(nums: list[int]) -> int:
    """
    Computes the alternating sum of the given array.
    
    The alternating sum is defined as: nums[0] - nums[1] + nums[2] - nums[3] + ...
    
    Args:
        nums: A list of integers.
        
    Returns:
        The resulting alternating sum as an integer.
        
    Examples:
        >>> solve([1, 2, 3, 4])
        -2  # (1 - 2 + 3 - 4)
        >>> solve([10, 5, 2])
        7   # (10 - 5 + 2)
    """
    alternating_sum = 0
    sign = 1
    
    for num in nums:
        # Add the current number multiplied by the current sign
        alternating_sum += sign * num
        
        # Flip the sign for the next element (1 becomes -1, -1 becomes 1)
        sign *= -1
        
    return alternating_sum
