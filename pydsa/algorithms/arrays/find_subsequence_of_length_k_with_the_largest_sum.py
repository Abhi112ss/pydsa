METADATA = {
    "id": 2099,
    "name": "Find Subsequence of Length K With the Largest Sum",
    "slug": "find-subsequence-of-length-k-with-the-largest-sum",
    "category": "Arrays",
    "aliases": [],
    "tags": ["arrays", "heaps"],
    "difficulty": "medium",
    "time_complexity": "O(n log k)",
    "space_complexity": "O(k)",
    "description": "Find a subsequence of length k with the largest sum, maintaining the original relative order.",
}

import heapq

def solve(nums: list[int], k: int) -> list[int]:
    """
    Finds a subsequence of length k with the largest sum.

    The algorithm uses a min-heap to track the k largest values in the array.
    After identifying the k largest values, it filters the original array 
    to maintain the original relative order of these elements.

    Args:
        nums: A list of integers.
        k: The required length of the subsequence.

    Returns:
        A list of k integers that form the subsequence with the largest sum.

    Examples:
        >>> solve([2, 1, 3, 3], 2)
        [3, 3]
        >>> solve([-1, -2, -3, -4], 2)
        [-1, -2]
    """
    # Use a min-heap to keep track of the k largest elements.
    # The heap will store tuples of (value, original_index) to handle 
    # duplicate values correctly and allow for sorting by index later.
    min_heap: list[tuple[int, int]] = []

    for index, value in enumerate(nums):
        if len(min_heap) < k:
            heapq.heappush(min_heap, (value, index))
        else:
            # If current value is larger than the smallest in our top-k heap, replace it.
            if value > min_heap[0][0]:
                heapq.heapreplace(min_heap, (value, index))

    # Extract the k largest elements and their original indices.
    # We need the indices to restore the original relative order.
    top_k_elements = []
    for value, index in min_heap:
        top_k_elements.append((index, value))

    # Sort the selected elements by their original index to satisfy the subsequence property.
    top_k_elements.sort()

    # Return only the values.
    return [value for index, value in top_k_elements]
