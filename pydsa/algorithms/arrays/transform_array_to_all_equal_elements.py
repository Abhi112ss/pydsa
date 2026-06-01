METADATA = {
    "id": 3576,
    "name": "Transform Array to All Equal Elements",
    "slug": "transform-array-to-all-equal-elements",
    "category": "Greedy",
    "aliases": [],
    "tags": ["greedy", "math", "sorting"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(1)",
    "description": "Find the minimum number of operations to make all elements in an array equal, where an operation consists of incrementing or decrementing an element by 1.",
}

def solve(nums: list[int]) -> int:
    """
    Calculates the minimum number of operations to make all elements in the array equal.
    
    The problem is equivalent to finding a value 'x' that minimizes the sum of 
    abs(nums[i] - x). This value 'x' is the median of the array.

    Args:
        nums: A list of integers representing the initial array.

    Returns:
        The minimum number of operations required.

    Examples:
        >>> solve([1, 2, 3])
        2
        >>> solve([1, 10, 2, 9])
        16
    """
    if not nums:
        return 0

    # Sort the array to easily find the median
    # Sorting takes O(n log n) time
    nums.sort()
    
    n = len(nums)
    # The median minimizes the sum of absolute differences.
    # For even length, any value between the two middle elements works.
    median = nums[n // 2]
    
    total_operations = 0
    for value in nums:
        # Sum the absolute distance of each element from the median
        total_operations += abs(value - median)
        
    return total_operations
