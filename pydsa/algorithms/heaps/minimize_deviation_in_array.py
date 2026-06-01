METADATA = {
    "id": 1675,
    "name": "Minimize Deviation in Array",
    "slug": "minimize_deviation_in_array",
    "category": "array",
    "aliases": [],
    "tags": ["greedy", "heap", "math"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Find the smallest possible deviation between the maximum and minimum array values after allowed operations.",
}


import heapq
from typing import List


def solve(nums: List[int]) -> int:
    """Return the minimum possible deviation in the array after allowed operations.

    Args:
        nums: List of positive integers.

    Returns:
        The smallest achievable difference between the maximum and minimum values.

    Examples:
        >>> solve([1,2,3,4])
        1
        >>> solve([4,1,5,20,3])
        3
    """
    # Convert all numbers to even values; odd numbers are multiplied by 2.
    even_nums: List[int] = []
    current_min: int = float("inf")
    for value in nums:
        if value % 2 == 1:
            value *= 2
        even_nums.append(value)
        if value < current_min:
            current_min = value

    # Build a max‑heap using negative values.
    max_heap: List[int] = [-v for v in even_nums]
    heapq.heapify(max_heap)

    # Initial deviation.
    current_max: int = -max_heap[0]
    best_deviation: int = current_max - current_min

    # Repeatedly reduce the current maximum element.
    while True:
        current_max = -heapq.heappop(max_heap)
        # Update the best deviation seen so far.
        if current_max - current_min < best_deviation:
            best_deviation = current_max - current_min

        # If the maximum is odd, it cannot be reduced further.
        if current_max % 2 == 1:
            break

        # Reduce the maximum by dividing by 2 and push it back.
        reduced = current_max // 2
        if reduced < current_min:
            current_min = reduced
        heapq.heappush(max_heap, -reduced)

    return best_deviation