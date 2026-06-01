METADATA = {
    "id": 3674,
    "name": "Minimum Operations to Equalize Array",
    "slug": "minimum-operations-to-equalize-array",
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
    An operation is defined as incrementing or decrementing an element by 1.
    
    The optimal target value to minimize the sum of absolute differences 
    (|x - target|) is the median of the array.

    Args:
        nums: A list of integers.

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
    # For both even and odd length arrays, the element at index n // 2 
    # serves as an optimal median for minimizing absolute deviations.
    median = nums[n // 2]
    
    total_operations = 0
    for value in nums:
        # The cost to change 'value' to 'median' is the absolute difference
        total_operations += abs(value - median)
        
    return total_operations
