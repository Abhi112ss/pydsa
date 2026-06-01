METADATA = {
    "id": 3355,
    "name": "Zero Array Transformation I",
    "slug": "zero-array-transformation-i",
    "category": "Array",
    "aliases": [],
    "tags": ["difference_array", "greedy", "array"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Determine if it is possible to make all elements of an array zero by applying a given number of operations that subtract values from ranges.",
}

def solve(nums: list[int], queries: list[list[int]]) -> bool:
    """
    Determines if the nums array can be transformed into an all-zero array 
    using the provided queries. Each query allows subtracting 1 from 
    nums[start...end].

    Args:
        nums: A list of non-negative integers.
        queries: A list of [start, end] pairs representing ranges.

    Returns:
        True if all elements in nums can be reduced to zero or less, False otherwise.

    Examples:
        >>> solve([1, 1, 1], [[0, 2], [0, 0]])
        True
        >>> solve([2, 3, 0, 1, 2], [[0, 2], [0, 2], [3, 4], [3, 4]])
        False
    """
    n = len(nums)
    # Use a difference array to track the number of operations applied to each index.
    # diff[i] stores the change in the number of active queries at index i.
    diff = [0] * (n + 1)

    for start, end in queries:
        diff[start] += 1
        if end + 1 < n:
            diff[end + 1] -= 1

    # current_coverage tracks the prefix sum of the difference array,
    # which represents the total number of queries covering the current index.
    current_coverage = 0
    for i in range(n):
        current_coverage += diff[i]
        
        # If the number of queries covering index i is less than the value 
        # required to zero out nums[i], it's impossible.
        if current_coverage < nums[i]:
            return False

    return True
