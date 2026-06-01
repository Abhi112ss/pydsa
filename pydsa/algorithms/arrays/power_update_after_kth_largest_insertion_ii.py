METADATA = {
    "id": 3930,
    "name": "Power Update After K-th Largest Insertion II",
    "slug": "power-update-after-k-th-largest-insertion-ii",
    "category": "Heap",
    "aliases": [],
    "tags": ["heap", "sorting", "priority queue"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Calculate the power update after performing k-th largest insertions into a sequence.",
}

import heapq

def solve(nums: list[int], k: int, updates: list[list[int]]) -> list[int]:
    """
    Calculates the resulting power values after a series of k-th largest insertions.
    
    The problem asks us to maintain a collection of numbers and, for each update, 
    insert a new value and determine the value of the k-th largest element 
    in the current collection.

    Args:
        nums: The initial list of integers.
        k: The rank (k-th largest) to track.
        updates: A list of updates where each update is [value, index_to_ignore].
                 Note: In the context of this specific problem type, we treat 
                 updates as adding a new element to the set.

    Returns:
        A list of integers representing the k-th largest element after each update.

    Examples:
        >>> solve([1, 2, 3], 2, [[4], [0]])
        [3, 3]
    """
    # We need to find the k-th largest element.
    # A min-heap of size k will store the k largest elements seen so far.
    # The root of this min-heap (the smallest of the k largest) is the k-th largest.
    
    k_largest_heap: list[int] = []
    results: list[int] = []

    # Initialize the heap with the starting numbers
    # We sort them first to handle the initial state efficiently
    for num in nums:
        if len(k_largest_heap) < k:
            heapq.heappush(k_largest_heap, num)
        else:
            if num > k_largest_heap[0]:
                heapq.heapreplace(k_largest_heap, num)

    for update in updates:
        # In this version of the problem, an update is a single value to insert
        val_to_insert = update[0]
        
        # If we haven't reached k elements yet, just add it
        if len(k_largest_heap) < k:
            heapq.heappush(k_largest_heap, val_to_insert)
        else:
            # If the new value is larger than the current k-th largest, 
            # it displaces the current k-th largest.
            if val_to_insert > k_largest_heap[0]:
                heapq.heapreplace(k_largest_heap, val_to_insert)
        
        # The k-th largest is the minimum element in our min-heap of size k
        # If the heap has fewer than k elements, the problem definition 
        # usually implies returning the smallest available or a specific sentinel.
        # Based on standard k-th largest logic:
        if len(k_largest_heap) == k:
            results.append(k_largest_heap[0])
        else:
            # This case handles if k is larger than the total elements available
            results.append(-1) 

    return results
