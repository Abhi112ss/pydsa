METADATA = {
    "id": 2089,
    "name": "Find Target Indices After Sorting Array",
    "slug": "find-target-indices-after-sorting-array",
    "category": "Array",
    "aliases": [],
    "tags": ["array", "sorting"],
    "difficulty": "easy",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(1)",
    "description": "Return the indices of a target value in an array after the array has been sorted in non-decreasing order.",
}

def solve(nums: list[int], target: int) -> list[int]:
    """
    Finds the indices of the target value in the array after sorting it.

    Args:
        nums: A list of integers.
        target: The integer value to find the indices for.

    Returns:
        A list of indices where the target value is located in the sorted array.

    Examples:
        >>> solve([1, 2, 3, 4, 5], 3)
        [2]
        >>> solve([1, 2, 3, 4, 5], 6)
        []
        >>> solve([1, 2, 3, 4, 5], 1)
        [0]
    """
    # Sort the array in-place to achieve non-decreasing order
    nums.sort()
    
    result_indices: list[int] = []
    
    # Iterate through the sorted array to find all occurrences of the target
    for current_index in range(len(nums)):
        if nums[current_index] == target:
            result_indices.append(current_index)
        # Optimization: since the array is sorted, if we exceed the target, we can stop
        elif nums[current_index] > target:
            break
            
    return result_indices
