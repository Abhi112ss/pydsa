METADATA = {
    "id": 1671,
    "name": "Minimum Number of Removals to Make Mountain Array",
    "slug": "minimum-number-of-removals-to-make-mountain-array",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dp", "lis"],
    "difficulty": "hard",
    "time_complexity": "O(n^2)",
    "space_complexity": "O(n)",
    "description": "Find the minimum number of elements to remove from an array to make it a mountain array.",
}

def solve(nums: list[int]) -> int:
    """
    Calculates the minimum number of removals to transform the input array into a mountain array.
    
    A mountain array is an array that strictly increases to a peak and then strictly decreases.
    The peak must have at least one element to its left and at least one element to its right.

    Args:
        nums: A list of integers representing the input array.

    Returns:
        The minimum number of elements to remove.

    Examples:
        >>> solve([2, 1, 1, 5, 6, 2, 3, 1])
        3
        >>> solve([2, 2, 2])
        2
    """
    n = len(nums)
    if n < 3:
        return 0

    # left_lis[i] stores the length of the Longest Increasing Subsequence ending at index i
    left_lis = [1] * n
    for i in range(n):
        for j in range(i):
            if nums[i] > nums[j]:
                left_lis[i] = max(left_lis[i], left_lis[j] + 1)

    # right_lis[i] stores the length of the Longest Decreasing Subsequence starting at index i
    # (which is the same as the LIS ending at i if we traverse from right to left)
    right_lis = [1] * n
    for i in range(n - 1, -1, -1):
        for j in range(n - 1, i, -1):
            if nums[i] > nums[j]:
                right_lis[i] = max(right_lis[i], right_lis[j] + 1)

    max_mountain_len = 0

    # A valid mountain peak must have elements on both sides (lis > 1 and rlis > 1)
    for i in range(n):
        if left_lis[i] > 1 and right_lis[i] > 1:
            # The total length of the mountain subsequence with peak at i
            # is the sum of LIS from left and LIS from right, minus the peak itself (counted twice)
            current_mountain_len = left_lis[i] + right_lis[i] - 1
            max_mountain_len = max(max_mountain_len, current_mountain_len)

    # The minimum removals is the total length minus the longest mountain subsequence found
    return n - max_mountain_len
