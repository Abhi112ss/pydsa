METADATA = {
    "id": 1054,
    "name": "Distant Barcodes",
    "slug": "distant-barcodes",
    "category": "Greedy",
    "aliases": [],
    "tags": ["greedy", "priority_queue", "counting"],
    "difficulty": "medium",
    "time_complexity": "O(n log k)",
    "space_complexity": "O(k)",
    "description": "Rearrange an array of barcodes such that no two adjacent barcodes are equal.",
}

import heapq
from collections import Counter

def solve(barcodes: list[int]) -> list[int]:
    """
    Rearranges the barcodes such that no two adjacent barcodes are the same.

    The algorithm uses a greedy approach with a max-priority queue. We always
    pick the most frequent remaining element to place in the next available
    slot. To ensure no two adjacent elements are the same, we use a 'wait' 
    mechanism where the last used element is only added back to the priority 
    queue after the next element has been placed.

    Args:
        barcodes: A list of integers representing the barcodes.

    Returns:
        A list of integers representing the rearranged barcodes.

    Examples:
        >>> solve([1, 1, 1, 2, 2, 3])
        [1, 2, 1, 2, 1, 3]
        >>> solve([1, 1, 1])
        []
    """
    n = len(barcodes)
    if n == 0:
        return []

    # Count frequencies of each barcode
    counts = Counter(barcodes)
    
    # Max-heap to store (-frequency, value)
    # Python's heapq is a min-heap, so we negate the frequency
    max_heap = [(-freq, val) for val, freq in counts.items()]
    heapq.heapify(max_heap)

    result = []
    # This variable holds the element we just used, preventing it from 
    # being picked immediately for the next position.
    prev_element = None

    while max_heap:
        # Get the most frequent element available
        neg_freq, val = heapq.heappop(max_heap)
        result.append(val)

        # If there was a previously used element waiting to be re-added,
        # add it back to the heap now that we've placed a different element.
        if prev_element:
            heapq.heappush(max_heap, prev_element)
            prev_element = None

        # If the current element still has remaining occurrences,
        # set it aside to be re-added in the next iteration.
        new_freq = neg_freq + 1
        if new_freq < 0:
            prev_element = (new_freq, val)

    # If the result length is not equal to input length, it means we 
    # couldn't place all elements without violating the adjacency rule.
    if len(result) != n:
        return []

    return result
