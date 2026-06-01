METADATA = {
    "id": 1642,
    "name": "Furthest Building You Can Reach",
    "slug": "furthest_building_you_can_reach",
    "category": "Greedy",
    "aliases": [],
    "tags": ["greedy", "heap", "priority_queue"],
    "difficulty": "medium",
    "time_complexity": "O(n log k)",
    "space_complexity": "O(k)",
    "description": "Return the furthest building index reachable using given bricks and ladders.",
}


import heapq
from typing import List


def solve(buildings: List[int], bricks: int, ladders: int) -> int:
    """Greedy algorithm to determine the furthest building that can be reached.

    Args:
        buildings: A list of integers where each value represents the height of a building.
        bricks: The total number of bricks available to climb height differences.
        ladders: The total number of ladders available to bypass height differences.

    Returns:
        The index (0‑based) of the furthest building that can be reached.

    Examples:
        >>> solve([4,2,7,6,9,14,12], 5, 1)
        4
        >>> solve([4,12,2,7,3,18,20,3,19], 10, 2)
        7
    """
    # Min‑heap stores the height differences where ladders are currently used.
    ladder_allocations: List[int] = []

    for current_index in range(len(buildings) - 1):
        height_diff = buildings[current_index + 1] - buildings[current_index]

        # No resources needed if the next building is not higher.
        if height_diff <= 0:
            continue

        # Assume we use a ladder for this climb and push the diff onto the heap.
        heapq.heappush(ladder_allocations, height_diff)

        # If we have used more ladders than available, replace the smallest ladder
        # usage with bricks.
        if len(ladder_allocations) > ladders:
            smallest_diff = heapq.heappop(ladder_allocations)
            bricks -= smallest_diff

        # If bricks run out, we cannot reach the next building.
        if bricks < 0:
            return current_index

    # All buildings are reachable.
    return len(buildings) - 1