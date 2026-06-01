METADATA = {
    "id": 3422,
    "name": "Minimum Operations to Make Subarray Elements Equal",
    "slug": "minimum-operations-to-make-subarray-elements-equal",
    "category": "Array",
    "aliases": [],
    "tags": ["array", "median", "greedy"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(1)",
    "description": "Find the minimum operations to make all elements in a subarray equal by choosing a target value.",
}

def solve(nums: list[int], left: int, right: int) -> int:
    """
    Calculates the minimum operations to make all elements in the subarray 
    nums[left...right] equal. The optimal target value is the median.

    Args:
        nums: The input list of integers.
        left: The starting index of the subarray (inclusive).
        right: The ending index of the subarray (inclusive).

    Returns:
        The minimum number of operations (absolute differences) required.

    Examples:
        >>> solve([1, 2, 3, 4, 5], 0, 2)
        2
        >>> solve([1, 10, 100], 0, 2)
        99
    """
    # Extract the subarray defined by the range [left, right]
    subarray = nums[left : right + 1]
    
    # Sort the subarray to find the median efficiently
    # Sorting takes O(k log k) where k is the length of the subarray
    subarray.sort()
    
    # The median minimizes the sum of absolute differences
    # For an even number of elements, any value between the two middle elements works
    median_index = len(subarray) // 2
    median_value = subarray[median_index]
    
    total_operations = 0
    for value in subarray:
        # Sum the absolute distance of each element from the median
        total_operations += abs(value - median_value)
        
    return total_operations
