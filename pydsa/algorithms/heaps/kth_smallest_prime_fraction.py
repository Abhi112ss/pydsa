METADATA = {
    "id": 786,
    "name": "K-th Smallest Prime Fraction",
    "slug": "kth-smallest-prime-fraction",
    "category": "Heap / Binary Search",
    "aliases": [],
    "tags": ["binary_search", "heap", "two_pointer"],
    "difficulty": "medium",
    "time_complexity": "O(N log N + K log N) or O(N log(max_val))",
    "space_complexity": "O(N)",
    "description": "Find the k-th smallest fraction formed by two prime numbers from a given sorted list.",
}

import heapq

def solve(arr: list[int], k: int) -> list[float]:
    """
    Finds the k-th smallest fraction formed by elements in the sorted list 'arr'.

    The algorithm uses a Min-Heap to efficiently extract the smallest fractions.
    We initialize the heap with fractions formed by each prime and the smallest 
    possible denominator (the last element in the array). However, to ensure 
    we find the k-th smallest, we actually start by pairing each prime with 
    the element immediately following it in the sorted list.

    Args:
        arr: A sorted list of prime numbers.
        k: The rank of the fraction to find (1-indexed).

    Returns:
        A list containing two elements [numerator, denominator] representing 
        the k-th smallest fraction.

    Examples:
        >>> solve([2, 3, 5], 3)
        [2, 5]
        >>> solve([1, 2, 3, 5], 3)
        [2, 5]
    """
    n = len(arr)
    # Min-heap stores tuples: (fraction_value, numerator_index, denominator_index)
    # We use the actual value for comparison, then indices to track progress.
    min_heap = []

    # Initialize the heap with fractions arr[i] / arr[i+1]
    # This represents the smallest possible fraction for each numerator.
    for i in range(n - 1):
        heapq.heappush(min_heap, (arr[i] / arr[i + 1], i, i + 1))

    # Extract the smallest element from the heap k-1 times
    for _ in range(k - 1):
        _, numerator_idx, denominator_idx = heapq.heappop(min_heap)

        # If there is a larger denominator available for the current numerator,
        # push the next fraction (arr[numerator_idx] / arr[denominator_idx + 1])
        if denominator_idx + 1 < n:
            next_denominator_idx = denominator_idx + 1
            next_val = arr[numerator_idx] / arr[next_denominator_idx]
            heapq.heappush(min_heap, (next_val, numerator_idx, next_denominator_idx))

    # The k-th element is now at the top of the heap
    _, final_num_idx, final_den_idx = heapq.heappop(min_heap)
    
    return [float(arr[final_num_idx]), float(arr[final_den_idx])]
