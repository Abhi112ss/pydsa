METADATA = {
    "id": 3901,
    "name": "Good Subsequence Queries",
    "slug": "good_subsequence_queries",
    "category": "Data Structures",
    "aliases": [],
    "tags": ["prefix_sum", "binary_search", "math"],
    "difficulty": "medium",
    "time_complexity": "O((n + q) log n)",
    "space_complexity": "O(n)",
    "description": "Efficiently count occurrences of elements within specific ranges using frequency arrays and binary search.",
}

import bisect

def solve(nums: list[int], queries: list[list[int]]) -> list[int]:
    """
    Calculates the number of elements in nums that fall within the range [L, R] 
    for each query, where each query is [L, R].

    Args:
        nums: A list of integers representing the sequence.
        queries: A list of queries, where each query is a list [L, R].

    Returns:
        A list of integers representing the count of elements in nums 
        that satisfy L <= nums[i] <= R for each query.

    Examples:
        >>> solve([1, 2, 3, 4, 5], [[2, 4]])
        [3]
        >>> solve([1, 1, 1, 2, 2], [[1, 1], [2, 2], [1, 2]])
        [3, 2, 5]
    """
    # To answer range queries [L, R] on values efficiently, 
    # we sort the original array to enable binary search.
    sorted_nums = sorted(nums)
    n = len(sorted_nums)
    results = []

    for left_bound, right_bound in queries:
        # Find the first index where the value is >= left_bound
        # bisect_left returns the leftmost insertion point to maintain order
        start_idx = bisect.bisect_left(sorted_nums, left_bound)
        
        # Find the first index where the value is > right_bound
        # bisect_right returns the rightmost insertion point to maintain order
        end_idx = bisect.bisect_right(sorted_nums, right_bound)
        
        # The number of elements in the range [left_bound, right_bound]
        # is the difference between the two indices.
        count = end_idx - start_idx
        results.append(count)

    return results
