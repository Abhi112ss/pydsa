METADATA = {
    "id": 1906,
    "name": "Minimum Absolute Difference Queries",
    "slug": "minimum-absolute-difference-queries",
    "category": "Array",
    "aliases": [],
    "tags": ["binary_search", "sorted_array"],
    "difficulty": "medium",
    "time_complexity": "O((n + q) log n)",
    "space_complexity": "O(n)",
    "description": "Find the minimum absolute difference between a query value and any element in a given array.",
}

import bisect

def solve(nums: list[int], queries: list[int]) -> list[int]:
    """
    Calculates the minimum absolute difference for each query against the nums array.

    Args:
        nums: A list of integers.
        queries: A list of integers representing the query values.

    Returns:
        A list of integers where each element is the minimum absolute difference 
        found for the corresponding query.

    Examples:
        >>> solve([4, 5, 8, 1, 2], [3, 10])
        [1, 2]
        >>> solve([1, 10, 100], [50])
        [49]
    """
    # Sorting allows us to use binary search to find the closest neighbors
    sorted_nums = sorted(nums)
    n = len(sorted_nums)
    results = []

    for query in queries:
        # Find the insertion point to maintain order
        # idx is the index of the first element >= query
        idx = bisect.bisect_left(sorted_nums, query)

        # Case 1: query is smaller than or equal to the smallest element
        if idx == 0:
            results.append(abs(sorted_nums[0] - query))
        # Case 2: query is larger than the largest element
        elif idx == n:
            results.append(abs(sorted_nums[-1] - query))
        # Case 3: query is between two elements in the array
        else:
            # The closest value must be either the element at idx or idx - 1
            diff_right = abs(sorted_nums[idx] - query)
            diff_left = abs(sorted_nums[idx - 1] - query)
            results.append(min(diff_left, diff_right))

    return results
