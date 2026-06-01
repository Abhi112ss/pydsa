METADATA = {
    "id": 2602,
    "name": "Minimum Operations to Make All Array Elements Equal",
    "slug": "minimum-operations-to-make-all-array-elements-equal",
    "category": "Math",
    "aliases": [],
    "tags": ["math", "greedy"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the minimum number of operations to make all elements in an array equal, where an operation consists of incrementing or decrementing an element by 1.",
}

def solve(nums: list[int]) -> int:
    """
    Calculates the minimum number of operations to make all elements in the array equal.
    
    The problem is equivalent to finding a value 'x' that minimizes the sum of 
    absolute differences: sum(|nums[i] - x|). This value 'x' is the median of the array.
    Since the array is already sorted, the median is the middle element.

    Args:
        nums: A sorted list of integers.

    Returns:
        The minimum number of operations required.

    Examples:
        >>> solve([1, 3, 5])
        4
        >>> solve([1, 2, 3, 4])
        4
    """
    n = len(nums)
    # The median of a sorted array minimizes the sum of absolute deviations.
    # For an even number of elements, any value between the two middle elements works.
    median_index = n // 2
    median_value = nums[median_index]
    
    total_operations = 0
    for value in nums:
        # Sum the distance of each element from the median.
        total_operations += abs(value - median_value)
        
    return total_operations
