METADATA = {
    "id": 3168,
    "name": "Minimum Number of Chairs in a Waiting Room",
    "slug": "minimum-number-of-chairs-in-a-waiting-room",
    "category": "Algorithms",
    "aliases": [],
    "tags": ["sorting", "heap", "sweep_line"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Find the maximum number of overlapping intervals to determine the minimum chairs required.",
}

import heapq

def solve(intervals: list[list[int]]) -> int:
    """
    Calculates the minimum number of chairs needed to accommodate all people 
    based on their arrival and departure times.

    Args:
        intervals: A list of lists where each sub-list contains [arrival, departure].

    Returns:
        The maximum number of concurrent people in the room at any given time.

    Examples:
        >>> solve([[1, 5], [2, 3], [4, 6]])
        2
        >>> solve([[1, 10], [2, 3], [3, 4], [4, 5]])
        2
    """
    if not intervals:
        return 0

    # Sort intervals by arrival time to process people as they arrive
    intervals.sort(key=lambda x: x[0])

    # Min-heap to store the departure times of people currently in the room.
    # The smallest departure time is at the top, representing the person 
    # who will leave the room earliest.
    departure_heap: list[int] = []
    max_chairs: int = 0

    for arrival, departure in intervals:
        # If the earliest person in the room has already left (departure <= current arrival),
        # we can reuse their chair.
        while departure_heap and departure_heap[0] <= arrival:
            heapq.heappop(departure_heap)

        # Add the current person's departure time to the heap
        heapq.heappush(departure_heap, departure)

        # The size of the heap represents the number of people currently in the room
        max_chairs = max(max_chairs, len(departure_heap))

    return max_chairs
