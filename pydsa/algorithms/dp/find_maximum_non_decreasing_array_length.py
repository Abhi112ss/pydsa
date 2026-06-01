METADATA = {
    "id": 2945,
    "name": "Find Maximum Non-decreasing Array Length",
    "slug": "find-maximum-non-decreasing-array-length",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dp", "binary_search"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Find the length of the longest non-decreasing subsequence that can be formed by selecting elements from the array.",
}

import bisect

def solve(nums: list[int]) -> int:
    """
    Finds the length of the longest non-decreasing subsequence in the given array.

    This implementation uses the Patience Sorting algorithm (a variation of the 
    Longest Increasing Subsequence algorithm) which utilizes binary search 
    to maintain a list of the smallest possible tail elements for all 
    increasing subsequences of various lengths.

    Args:
        nums: A list of integers.

    Returns:
        The length of the longest non-decreasing subsequence.

    Examples:
        >>> solve([10, 9, 2, 5, 3, 7, 101, 18])
        4
        >>> solve([1, 1, 1, 1])
        4
        >>> solve([5, 4, 3, 2, 1])
        1
    """
    if not nums:
        return 0

    # tails[i] will store the smallest tail of all non-decreasing 
    # subsequences of length i + 1.
    tails: list[int] = []

    for x in nums:
        # To find the longest NON-DECREASING subsequence, we use 
        # bisect_right. This allows duplicate values to extend the 
        # subsequence (e.g., [1, 1, 1]).
        # If we wanted strictly increasing, we would use bisect_left.
        idx = bisect.bisect_right(tails, x)

        if idx < len(tails):
            # If x is not larger than all elements in tails, 
            # replace the first element that is strictly greater than x.
            # This maintains the property that tails[i] is as small as possible.
            tails[idx] = x
        else:
            # If x is greater than or equal to all elements in tails,
            # it extends the longest non-decreasing subsequence found so far.
            tails.append(x)

    return len(tails)
