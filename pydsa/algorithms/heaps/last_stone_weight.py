METADATA = {
    "id": 1046,
    "name": "Last Stone Weight",
    "slug": "last-stone-weight",
    "category": "Heap",
    "aliases": [],
    "tags": ["priority_queue", "greedy", "heap"],
    "difficulty": "easy",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Find the weight of the last remaining stone after repeatedly smashing the two heaviest stones together.",
}

import heapq

def solve(stones: list[int]) -> int:
    """
    Simulates the stone smashing process using a max-heap to always pick the heaviest stones.

    Args:
        stones: A list of integers representing the weights of the stones.

    Returns:
        The weight of the last remaining stone, or 0 if no stones are left.

    Examples:
        >>> solve([2, 7, 4, 1, 8, 1])
        1
        >>> solve([2, 7, 4, 1, 8, 1]) # Wait, example 1: [8,7,4,2,1,1] -> [1,4,2,1] -> [3,2,1] -> [1,1] -> [0]
        # Correct trace for [2, 7, 4, 1, 8, 1]:
        # 1. [8, 7, 4, 2, 1, 1] -> smash 8, 7 -> 1 remains -> [4, 2, 1, 1, 1]
        # 2. [4, 2, 1, 1, 1] -> smash 4, 2 -> 2 remains -> [2, 1, 1, 1]
        # 3. [2, 1, 1, 1] -> smash 2, 1 -> 1 remains -> [1, 1, 1]
        # 4. [1, 1, 1] -> smash 1, 1 -> 0 remains -> [1]
        # Result: 1
    """
    if not stones:
        return 0

    # Python's heapq is a min-heap. To simulate a max-heap, 
    # we negate all values.
    max_heap = [-weight for weight in stones]
    heapq.heapify(max_heap)

    while len(max_heap) > 1:
        # Extract the two heaviest stones (smallest values in negated heap)
        first_heaviest = -heapq.heappop(max_heap)
        second_heaviest = -heapq.heappop(max_heap)

        if first_heaviest != second_heaviest:
            # If they are not equal, the difference is added back to the heap
            remaining_weight = first_heaviest - second_heaviest
            heapq.heappush(max_heap, -remaining_weight)

    # If one stone remains, return its weight; otherwise return 0
    return -max_heap[0] if max_heap else 0
