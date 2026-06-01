METADATA = {
    "id": 1846,
    "name": "Maximum Element After Decreasing and Rearranging",
    "slug": "maximum-element-after-decreasing-and-rearranging",
    "category": "Array",
    "aliases": [],
    "tags": ["greedy", "array", "sorting"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(1)",
    "description": "Maximize the maximum element of an array after rearranging and decreasing elements such that the difference between adjacent elements is at most 1.",
}

def solve(nums: list[int]) -> int:
    """
    Finds the maximum element possible after rearranging and decreasing elements.
    
    The strategy is to sort the array and then iterate through it, ensuring 
    that each element is at most 1 greater than the previous element. 
    If an element is too large, we decrease it to (previous_element + 1).

    Args:
        nums: A list of integers.

    Returns:
        The maximum element in the modified array.

    Examples:
        >>> solve([4, 2, 1])
        3
        >>> solve([1, 1, 1])
        1
        >>> solve([1, 5, 10])
        3
    """
    if not nums:
        return 0

    # Sort the array to process elements in non-decreasing order
    # This allows us to greedily build the sequence with minimum reductions
    nums.sort()

    # The first element remains unchanged as it's the starting point
    current_max = nums[0]

    for i in range(1, len(nums)):
        # If the current element is greater than the previous + 1,
        # we must decrease it to satisfy the condition (diff <= 1).
        # Otherwise, we keep it as is to maximize the potential peak.
        if nums[i] > current_max + 1:
            current_max += 1
        else:
            # If it's already within the range [current_max, current_max + 1],
            # we update current_max to the current element to keep the sequence growing.
            current_max = nums[i]

    return current_max
