METADATA = {
    "id": 3478,
    "name": "Choose K Elements With Maximum Sum",
    "slug": "choose_k_elements_with_maximum_sum",
    "category": "Heap",
    "aliases": [],
    "tags": ["heap", "sorting", "greedy"],
    "difficulty": "medium",
    "time_complexity": "O(n log k)",
    "space_complexity": "O(k)",
    "description": "Find the maximum sum possible by choosing exactly k elements from an array.",
}

import heapq

def solve(nums: list[int], k: int) -> int:
    """
    Calculates the maximum sum possible by selecting exactly k elements from the input list.

    Args:
        nums: A list of integers.
        k: The number of elements to select.

    Returns:
        The maximum sum of k elements.

    Examples:
        >>> solve([1, 5, 2, 8, 3], 3)
        16
        >>> solve([-1, -5, -2, -8, -3], 2)
        -3
    """
    if k <= 0:
        return 0
    
    # We use a min-heap to maintain the k largest elements seen so far.
    # The smallest of these k largest elements will be at the root (index 0).
    min_heap: list[int] = []
    
    for num in nums:
        if len(min_heap) < k:
            heapq.heappush(min_heap, num)
        else:
            # If the current number is larger than the smallest element in our 
            # top-k set, replace the smallest with the current number.
            if num > min_heap[0]:
                heapq.heapreplace(min_heap, num)
                
    # The sum of the elements remaining in the heap is the maximum sum.
    return sum(min_heap)
