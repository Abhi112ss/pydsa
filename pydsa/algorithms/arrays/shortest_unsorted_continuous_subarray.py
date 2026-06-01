METADATA = {
    "id": 581,
    "name": "Shortest Unsorted Continuous Subarray",
    "slug": "shortest-unsorted-continuous-subarray",
    "category": "Array",
    "aliases": [],
    "tags": ["two_pointer", "sorting", "stack"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the length of the shortest continuous subarray that, if sorted, would make the entire array sorted.",
}

def solve(nums: list[int]) -> int:
    """
    Finds the length of the shortest continuous subarray that, if sorted, 
    makes the entire array sorted.

    The algorithm works by finding the boundaries of the unsorted region.
    An element is part of the unsorted region if it is not in its correct 
    sorted position relative to the global minimum and maximum values 
    encountered during a single pass.

    Args:
        nums: A list of integers.

    Returns:
        The length of the shortest unsorted continuous subarray. 
        Returns 0 if the array is already sorted.

    Examples:
        >>> solve([2, 6, 4, 8, 10, 9, 15])
        5
        >>> solve([1, 2, 3, 4])
        0
        >>> solve([1])
        0
    """
    n = len(nums)
    if n <= 1:
        return 0

    # Initialize boundaries for the unsorted subarray
    # left_boundary will be the first index where the element is smaller than 
    # the maximum seen so far from the left.
    # right_boundary will be the last index where the element is larger than 
    # the minimum seen so far from the right.
    left_boundary = -1
    right_boundary = -1

    # Pass 1: Find the leftmost index that is out of order.
    # An element is out of order if it is smaller than the maximum element 
    # encountered to its left.
    max_so_far = float('-inf')
    for i in range(n):
        if nums[i] < max_so_far:
            left_boundary = i
        else:
            max_so_far = nums[i]

    # If left_boundary remains -1, the array is already sorted.
    if left_boundary == -1:
        return 0

    # Pass 2: Find the rightmost index that is out of order.
    # An element is out of order if it is larger than the minimum element 
    # encountered to its right.
    min_so_far = float('inf')
    for i in range(n - 1, -1, -1):
        if nums[i] > min_so_far:
            right_boundary = i
        else:
            min_so_far = nums[i]

    # The length is the distance between the identified boundaries.
    return right_boundary - left_boundary + 1
