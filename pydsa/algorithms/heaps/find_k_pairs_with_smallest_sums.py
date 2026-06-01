METADATA = {
    "id": 373,
    "name": "Find K Pairs with Smallest Sums",
    "slug": "find-k-pairs-with-smallest-sums",
    "category": "Heap",
    "aliases": [],
    "tags": ["heap", "priority_queue", "sorting"],
    "difficulty": "medium",
    "time_complexity": "O(K log K)",
    "space_complexity": "O(K)",
    "description": "Given two integer arrays nums1 and nums2 sorted in ascending order and an integer k, return the k smallest pairs (u, v) where u is from nums1 and v is from nums2.",
}

import heapq

def solve(nums1: list[int], nums2: list[int], k: int) -> list[list[int]]:
    """
    Finds the k pairs with the smallest sums using a min-heap.

    Args:
        nums1: A sorted list of integers.
        nums2: A sorted list of integers.
        k: The number of smallest pairs to return.

    Returns:
        A list of lists, where each inner list contains a pair of integers.

    Examples:
        >>> solve([1, 7, 11], [2, 4, 6], 3)
        [[1, 2], [1, 4], [1, 6]]
        >>> solve([1, 1, 2], [1, 2, 3], 2)
        [[1, 1], [1, 1]]
    """
    if not nums1 or not nums2 or k <= 0:
        return []

    result: list[list[int]] = []
    # min_heap stores tuples of (sum, index_in_nums1, index_in_nums2)
    min_heap: list[tuple[int, int, int]] = []

    # Optimization: We only need to consider at most k elements from nums1
    # to find the k smallest pairs.
    for i in range(min(len(nums1), k)):
        # Initial pairs: (nums1[i], nums2[0])
        heapq.heappush(min_heap, (nums1[i] + nums2[0], i, 0))

    # Extract the smallest sum from the heap up to k times
    while min_heap and len(result) < k:
        current_sum, i, j = heapq.heappop(min_heap)
        result.append([nums1[i], nums2[j]])

        # If there is a next element in nums2 for the current element in nums1,
        # push the pair (nums1[i], nums2[j+1]) into the heap.
        # This ensures we explore the next smallest possible sum incrementally.
        if j + 1 < len(nums2):
            heapq.heappush(min_heap, (nums1[i] + nums2[j + 1], i, j + 1))

    return result
