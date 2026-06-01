METADATA = {
    "id": 1471,
    "name": "The k Strongest Values in an Array",
    "slug": "the-k-strongest-values-in-an-array",
    "category": "Heap",
    "aliases": [],
    "tags": ["heap", "sorting"],
    "difficulty": "easy",
    "time_complexity": "O(n log k)",
    "space_complexity": "O(k)",
    "description": "Find the k strongest values in an array where strength is defined by absolute value, then by actual value.",
}

import heapq

def solve(arr: list[int], k: int) -> list[int]:
    """
    Finds the k strongest values in an array using a min-heap.
    
    Strength is determined by:
    1. Absolute value (higher is stronger).
    2. If absolute values are equal, the actual value (higher is stronger).

    Args:
        arr: A list of integers.
        k: The number of strongest values to return.

    Returns:
        A list of the k strongest integers in non-decreasing order.

    Examples:
        >>> solve([2, -1, -3, 4], 2)
        [-1, 4]
        >>> solve([1, 2, 3, 4, 5], 4)
        [2, 3, 4, 5]
    """
    # We use a min-heap to keep track of the 'k' strongest elements.
    # To handle the tie-breaking rule (if abs(a) == abs(b), then a > b),
    # we store tuples in the heap: (abs_value, actual_value).
    # A min-heap will naturally discard the smallest (abs_value, actual_value) 
    # when it exceeds size k, leaving the k largest behind.
    min_heap: list[tuple[int, int]] = []

    for num in arr:
        strength_tuple = (abs(num), num)
        
        if len(min_heap) < k:
            heapq.heappush(min_heap, strength_tuple)
        else:
            # If current element is stronger than the weakest in our top-k heap, replace it.
            # Comparison in Python tuples is lexicographical: first by abs(num), then by num.
            if strength_tuple > min_heap[0]:
                heapq.heapreplace(min_heap, strength_tuple)

    # Extract the actual values from the heap and sort them as per problem requirement.
    result = sorted([val[1] for val in min_heap])
    return result
