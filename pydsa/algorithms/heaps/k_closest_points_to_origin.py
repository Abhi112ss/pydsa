METADATA = {
    "id": 973,
    "name": "K Closest Points to Origin",
    "slug": "k-closest-points-to-origin",
    "category": "Heap / Quickselect",
    "aliases": [],
    "tags": ["priority_queue", "quickselect", "heap"],
    "difficulty": "medium",
    "time_complexity": "O(n log k)",
    "space_complexity": "O(k)",
    "description": "Find the k points in a 2D plane that are closest to the origin (0, 0).",
}

import heapq

def solve(points: list[list[int]], k: int) -> list[list[int]]:
    """
    Finds the k points closest to the origin using a max-heap.

    Args:
        points: A list of [x, y] coordinates.
        k: The number of closest points to return.

    Returns:
        A list of the k points closest to the origin.

    Examples:
        >>> solve([[1, 3], [-2, 2]], 1)
        [[-2, 2]]
        >>> solve([[3, 3], [5, -1], [-2, 4]], 2)
        [[3, 3], [-2, 4]]
    """
    # We use a max-heap to keep track of the 'k' smallest distances.
    # Since Python's heapq is a min-heap, we store distances as negative values.
    # This allows the largest distance among the current k points to be at the root.
    max_heap: list[tuple[int, int, int]] = []

    for x, y in points:
        # Calculate squared Euclidean distance to avoid floating point issues
        # dist = x^2 + y^2
        dist_sq = x * x + y * y
        
        if len(max_heap) < k:
            # If heap isn't full, push the current point
            # Format: (-distance, x, y)
            heapq.heappush(max_heap, (-dist_sq, x, y))
        else:
            # If current point is closer than the furthest point in our heap
            # (max_heap[0][0] is the negative of the largest distance seen so far)
            if -dist_sq > max_heap[0][0]:
                heapq.heapreplace(max_heap, (-dist_sq, x, y))

    # Extract the coordinates from the heap
    return [[x, y] for _, x, y in max_heap]
