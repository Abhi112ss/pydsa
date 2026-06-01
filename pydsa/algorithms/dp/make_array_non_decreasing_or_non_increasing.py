METADATA = {
    "id": 2263,
    "name": "Make Array Non-decreasing or Non-increasing",
    "slug": "make-array-non-decreasing-or-non-increasing",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dp", "binary_search"],
    "difficulty": "hard",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Find the minimum number of elements to remove to make an array either non-decreasing or non-increasing.",
}

import bisect

def solve(nums: list[int]) -> int:
    """
    Calculates the minimum number of elements to remove to make the array 
    either non-decreasing or non-increasing.

    The problem is equivalent to finding the length of the Longest Non-Decreasing 
    Subsequence (LNDS) and the Longest Non-Increasing Subsequence (LNIS). 
    The answer is the total length minus the maximum of these two lengths.

    Args:
        nums: A list of integers.

    Returns:
        The minimum number of removals required.

    Examples:
        >>> solve([1, 2, 3])
        0
        >>> solve([3, 2, 1])
        0
        >>> solve([1, 3, 2, 4])
        1
    """
    if not nums:
        return 0

    def get_lnds_length(arr: list[int]) -> int:
        """
        Finds the length of the Longest Non-Decreasing Subsequence using O(n log n) approach.
        """
        tails: list[int] = []
        for x in arr:
            # bisect_right finds the first element strictly greater than x
            # This allows duplicate values to be part of the non-decreasing sequence
            idx = bisect.bisect_right(tails, x)
            if idx < len(tails):
                tails[idx] = x
            else:
                tails.append(x)
        return len(tails)

    # Case 1: Make the array non-decreasing
    # We find the Longest Non-Decreasing Subsequence
    lnds_len = get_lnds_length(nums)

    # Case 2: Make the array non-increasing
    # This is equivalent to finding the Longest Non-Decreasing Subsequence 
    # on the reversed array or by negating the values.
    # We'll use the negation approach for clarity.
    negated_nums = [-x for x in nums]
    lnis_len = get_lnds_length(negated_nums)

    # The minimum removals is the total length minus the longest valid subsequence found
    max_subsequence_len = max(lnds_len, lnis_len)
    return len(nums) - max_subsequence_len
