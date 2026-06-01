METADATA = {
    "id": 253,
    "name": "Meeting Rooms II",
    "slug": "meeting-rooms-ii",
    "category": "Heap",
    "aliases": [],
    "tags": ["sorting", "heaps", "greedy"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Find the minimum number of conference rooms required to hold all meetings.",
}

import heapq

def solve(intervals: list[list[int]]) -> int:
    """
    Calculates the minimum number of conference rooms required.

    Args:
        intervals: A list of meeting time intervals where intervals[i] = [start_i, end_i].

    Returns:
        The minimum number of rooms required to accommodate all meetings.

    Examples:
        >>> solve([[0, 30], [5, 10], [15, 20]])
        2
        >>> solve([[7, 10], [2, 4]])
        1
    """
    if not intervals:
        return 0

    # Sort meetings by start time to process them chronologically
    intervals.sort(key=lambda x: x[0])

    # Min-heap to store the end times of meetings currently occupying a room.
    # The smallest end time is at the top, representing the room that frees up earliest.
    active_meetings_end_times = []

    # Add the end time of the first meeting
    heapq.heappush(active_meetings_end_times, intervals[0][1])

    for i in range(1, len(intervals)):
        current_start, current_end = intervals[i]

        # If the earliest room becomes free before or at the current meeting's start time,
        # we can reuse that room.
        if current_start >= active_meetings_end_times[0]:
            heapq.heappop(active_meetings_end_times)

        # Add the current meeting's end time to the heap.
        # If we reused a room, this replaces the old end time.
        # If we didn't, this increases the heap size (representing a new room).
        heapq.heappush(active_meetings_end_times, current_end)

    # The size of the heap represents the total number of rooms used.
    return len(active_meetings_end_times)
