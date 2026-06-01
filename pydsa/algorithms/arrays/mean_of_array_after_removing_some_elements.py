METADATA = {
    "id": 1619,
    "name": "Mean of Array After Removing Some Elements",
    "slug": "mean_of_array_after_removing_some_elements",
    "category": "algorithms",
    "aliases": [],
    "tags": ["heaps", "greedy"],
    "difficulty": "easy",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Find the maximum possible mean after removing any number of smallest elements.",
}


import sys
import heapq
from typing import List


def solve() -> None:
    """Read an integer array from standard input and print the maximum possible mean.

    The input format is:
        n
        a1 a2 ... an

    Args:
        None (input is read from stdin).

    Returns:
        None (the result is printed to stdout).

    Example:
        >>> # input
        >>> 5
        >>> 3 1 2 4 5
        >>> # output
        >>> 4.5
    """
    data = sys.stdin.read().strip().split()
    if not data:
        return
    n = int(data[0])
    numbers: List[int] = list(map(int, data[1:1 + n]))

    # Build a min‑heap to efficiently remove the smallest elements one by one.
    min_heap: List[int] = numbers[:]
    heapq.heapify(min_heap)

    total_sum: int = sum(numbers)
    remaining_count: int = n
    max_mean: float = total_sum / remaining_count

    # Iteratively remove the smallest element and update the mean.
    while min_heap:
        smallest = heapq.heappop(min_heap)
        total_sum -= smallest
        remaining_count -= 1
        if remaining_count == 0:
            break
        current_mean = total_sum / remaining_count
        if current_mean > max_mean:
            max_mean = current_mean

    # Print the result with default float formatting.
    print(max_mean)
