METADATA = {
    "id": 218,
    "name": "The Skyline Problem",
    "slug": "the-skyline-problem",
    "category": "Hard",
    "aliases": [],
    "tags": ["heap", "segment_tree", "divide_and_conquer"],
    "difficulty": "hard",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Given the locations and heights of buildings, return the skyline formed by these buildings.",
}

import heapq

def solve(buildings: list[list[int]]) -> list[list[int]]:
    """
    Args:
        buildings: A list of lists where each sub-list contains [left, right, height].

    Returns:
        A list of key points [x, y] that define the skyline.
    """
    events = []
    for left, right, height in buildings:
        events.append((left, -height, right))
        events.append((right, 0, 0))

    events.sort()

    result = [[0, 0]]
    max_heap = [(0, float('inf'))]

    for x, negative_height, right in events:
        if negative_height != 0:
            heapq.heappush(max_heap, (negative_height, right))

        while max_heap[0][1] <= x:
            heapq.heappop(max_heap)

        current_max_height = -max_heap[0][0]

        if result[-1][1] != current_max_height:
            if result[-1][0] == x:
                result[-1][1] = current_max_height
            else:
                result.append([x, current_max_height])

    return result[1:]