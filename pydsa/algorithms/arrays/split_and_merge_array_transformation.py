METADATA = {
    "id": 3690,
    "name": "Split and Merge Array Transformation",
    "slug": "split-and-merge-array-transformation",
    "category": "Arrays",
    "aliases": [],
    "tags": ["greedy", "arrays"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Minimize operations to transform an array by identifying contiguous segments that can be merged.",
}

def solve(nums: list[int]) -> int:
    """
    Calculates the minimum number of operations to transform the array.
    
    The problem asks to minimize operations by identifying contiguous segments 
    that can be merged. An operation is defined as splitting or merging. 
    The optimal strategy is to count how many contiguous segments of 
    identical elements exist, as each segment can be treated as a single unit.

    Args:
        nums: A list of integers representing the array.

    Returns:
        int: The minimum number of operations required.

    Examples:
        >>> solve([1, 1, 2, 2, 2, 3, 3])
        2
        >>> solve([1, 2, 3])
        2
        >>> solve([1, 1, 1])
        0
    """
    if not nums:
        return 0

    # The number of operations is essentially the number of transitions 
    # between different values. Each transition represents a point where 
    # a merge or a split must occur to maintain the target structure.
    operations = 0
    n = len(nums)

    for i in range(1, n):
        # If the current element is different from the previous one,
        # it marks the boundary of a new segment.
        if nums[i] != nums[i - 1]:
            operations += 1

    return operations
