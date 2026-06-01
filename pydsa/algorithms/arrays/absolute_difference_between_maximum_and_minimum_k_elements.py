METADATA = {
    "id": 3774,
    "name": "Absolute Difference Between Maximum and Minimum K Elements",
    "slug": "absolute-difference-between-maximum-and-minimum-k-elements",
    "category": "Array",
    "aliases": [],
    "tags": ["sorting", "sliding_window"],
    "difficulty": "easy",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(1)",
    "description": "Find the minimum absolute difference between the maximum and minimum elements in any subarray of size k after sorting.",
}

def solve(nums: list[int], k: int) -> int:
    """
    Finds the minimum absolute difference between the maximum and minimum 
    elements in any subset of size k.

    The problem asks for the minimum difference between the max and min of 
    k elements. To minimize this difference, we should pick k elements 
    that are closest to each other in value. Sorting the array allows us 
    to consider only contiguous windows of size k.

    Args:
        nums: A list of integers.
        k: The number of elements to select.

    Returns:
        The minimum absolute difference between the maximum and minimum 
        elements among any k elements.

    Examples:
        >>> solve([10, 1, 5, 20, 15], 3)
        5
        >>> solve([1, 2, 3, 4], 2)
        1
    """
    n = len(nums)
    if k <= 1:
        return 0

    # Sort the array to bring elements with similar values close to each other
    nums.sort()

    # Initialize min_diff with a very large value
    min_diff = float('inf')

    # Use a sliding window of size k. 
    # In a sorted array, for any window [i, i + k - 1], 
    # the minimum is nums[i] and the maximum is nums[i + k - 1].
    for i in range(n - k + 1):
        current_diff = nums[i + k - 1] - nums[i]
        if current_diff < min_diff:
            min_diff = current_diff

    return int(min_diff)
